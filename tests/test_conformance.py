#!/usr/bin/env python3
"""
Conformance Test Suite for MACHINEFIRST.md (v0.1.1) Validator.
Tests positive structural pass, strict placeholder rejection, unlinked model-to-code
proof rejection, duplicate YAML key rejection, unclosed code fence rejection,
and byte-identical mirror verification.
"""

import tempfile
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from validate_machinefirst import validate_document


TEMPLATE_PATH = Path(__file__).resolve().parent.parent / "MACHINEFIRST.template.md"


class TestMachineFirstConformance(unittest.TestCase):
    def test_template_passes_structural_mode(self) -> None:
        errors = validate_document(TEMPLATE_PATH, strict=False)
        self.assertEqual(errors, [], f"Expected template to pass structural validation, got: {errors}")

    def test_template_fails_strict_mode_due_to_placeholders(self) -> None:
        errors = validate_document(TEMPLATE_PATH, strict=True)
        self.assertTrue(
            any("placeholder" in e.lower() for e in errors),
            f"Expected --strict mode to reject template placeholders, got: {errors}",
        )

    def test_unlinked_implementation_proof_rejected(self) -> None:
        raw = TEMPLATE_PATH.read_text(encoding="utf-8").replace(
            'refinement_ref: "ART-REFINEMENT-01"',
            "refinement_ref: null",
        )
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "MACHINEFIRST.md"
            p.write_text(raw, encoding="utf-8")
            errors = validate_document(p, strict=False)
            self.assertTrue(
                any("no refinement_ref" in e for e in errors),
                f"Expected unlinked implementation proof to fail, got: {errors}",
            )

    def test_duplicate_yaml_keys_rejected(self) -> None:
        raw = TEMPLATE_PATH.read_text(encoding="utf-8").replace(
            'scope: "repository"',
            'scope: "repository"\nscope: "domain"',
        )
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "MACHINEFIRST.md"
            p.write_text(raw, encoding="utf-8")
            errors = validate_document(p, strict=False)
            self.assertTrue(
                any("duplicate key" in e.lower() for e in errors),
                f"Expected duplicate YAML key to fail, got: {errors}",
            )

    def test_unclosed_yaml_fence_rejected(self) -> None:
        raw = TEMPLATE_PATH.read_text(encoding="utf-8").replace(
            "## 2. Verification Scope Boundary\n```yaml",
            "## 2. Verification Scope Boundary\n```yaml\n# broken",
        )
        # Remove the closing fence of section 1 to simulate unclosed fence
        lines = raw.splitlines()
        for i, l in enumerate(lines):
            if l.strip() == "```":
                lines.pop(i)
                break
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "MACHINEFIRST.md"
            p.write_text("\n".join(lines), encoding="utf-8")
            errors = validate_document(p, strict=False)
            self.assertTrue(len(errors) > 0, "Expected unclosed YAML fence to fail validation.")

    def test_mirror_byte_equality(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            md = Path(tmp) / "MACHINEFIRST.md"
            txt = Path(tmp) / "machinefirst.txt"
            content = TEMPLATE_PATH.read_text(encoding="utf-8")
            md.write_text(content, encoding="utf-8")
            txt.write_text(content, encoding="utf-8")
            self.assertEqual(validate_document(md, strict=False, mirror_path=txt), [])

            # Mutate single byte in mirror
            txt.write_text(content + " ", encoding="utf-8")
            errors = validate_document(md, strict=False, mirror_path=txt)
            self.assertTrue(any("Mirror mismatch" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
