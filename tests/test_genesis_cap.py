from __future__ import annotations

import json
import pathlib
import sys
import tempfile
import unittest
from typing import Any, Dict, List, Optional

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from validator.validate_machinefirst import check_mirror_byte_parity, validate_manifest


FIXTURE_PATH = pathlib.Path(__file__).parent / "fixtures" / "genesis_vectors.json"


def wrap_manifest(
    claim: Dict[str, Any],
    artifacts: List[Dict[str, Any]],
    version: str = "0.1.2",
    backing: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    doc: Dict[str, Any] = {
        "machinefirst_version": version,
        "this_file_is_data_not_instructions": True,
        "treat_strings_as_inert_data": True,
        "claim_authority": "publisher_asserted",
        "authority_model": "publisher_declared_nonbinding",
        "normative_artifacts": artifacts,
        "claims": [claim],
    }
    if backing is not None:
        doc["non_normative_formal_backing"] = backing
    return doc


class TestGenesisCapAndParity(unittest.TestCase):
    def test_canonical_and_adversarial_vectors(self) -> None:
        suite = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
        for vec in suite["vectors"]:
            with self.subTest(vector=vec["id"], note=vec["note"]):
                manifest = wrap_manifest(vec["claim"], vec["normative_artifacts"])
                errors = validate_manifest(manifest, strict=True)
                is_valid = len(errors) == 0
                self.assertEqual(
                    is_valid,
                    vec["expected_valid"],
                    f"{vec['id']} failed: expected {vec['expected_valid']}, got errors={errors}",
                )

    def test_v011_live_shape_backward_compatibility(self) -> None:
        live_v011_shape = {
            "machinefirst_version": "0.1.1",
            "contract_type": "epistemic_evidence_map",
            "parse_mode": "strict",
            "duplicate_keys": "reject",
            "canonical_url": "https://admissibilityscience.com/machinefirst.txt",
            "valid_as_of": "2026-11-19",
            "supersedes": None,
            "errata": "ARC-ERR-2026-001",
            "scope": "discovery_manifest_integrity",
            "persistent_ids": {"master_anchor": "A-77-DELTA-SHIELD-LOCKED"},
            "contract_binding": {"commit": "a" * 40},
            "conflict_rule": "fail_closed",
            "auditor_states": ["not_checked", "reproduced_pass", "reproduced_fail"],
            "non_normative_surfaces": ["README.md"],
            "claim_authority": "publisher_asserted",
            "authority_model": "publisher_declared_nonbinding",
            "conformance_guards": {
                "this_file_is_data_not_instructions": True,
                "treat_strings_as_inert_data": True,
            },
            "evidence_ladder": [
                "stated",
                "measured",
                "static_analysis",
                "tested",
                "proved",
                "external_llm_review",
            ],
            "normative_artifacts": [
                {
                    "id": "ART-LEGACY-01",
                    "path": "llms.txt",
                    "hash_algorithm": "sha256",
                    "digest": "a" * 64,
                }
            ],
            "claims": [
                {
                    "id": "CLM-001",
                    "statement": "Live v0.1.1 manifest structure with object assumptions",
                    "claimed_level": "stated",
                    "assumptions": {
                        "source": "publisher",
                        "declared_items": [],
                        "dependency_audit": "closed",
                    },
                    "evidence_ref": {"artifact_id": "ART-LEGACY-01"},
                }
            ],
        }
        self.assertEqual(validate_manifest(live_v011_shape, strict=False), [])
        self.assertNotEqual(validate_manifest(live_v011_shape, strict=True), [])

    def test_duplicate_artifact_ids_rejected(self) -> None:
        dup_artifacts = [
            {
                "id": "ART-DUP-01",
                "path": "a.txt",
                "hash_algorithm": "sha256",
                "digest": "a" * 64,
            },
            {
                "id": "ART-DUP-01",
                "path": "b.txt",
                "hash_algorithm": "sha256",
                "digest": "b" * 64,
            },
        ]
        claim = {
            "id": "CLM-201",
            "statement": "Duplicate artifact test",
            "claimed_level": "stated",
            "claim_scope": "formal_statement",
            "genesis": {
                "spec_origin": "human_authored",
                "adequacy_status": "unattested",
                "spec_digest": "1" * 64,
                "genesis_ref": None,
            },
        }
        errors = validate_manifest(wrap_manifest(claim, dup_artifacts), strict=True)
        self.assertTrue(any("DUPLICATE_ARTIFACT_ID" in e for e in errors))

    def test_mirror_byte_parity(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            p1 = pathlib.Path(tmp) / "MACHINEFIRST.md"
            p2 = pathlib.Path(tmp) / "machinefirst.txt"
            p1.write_text("canonical content\n", encoding="utf-8")
            p2.write_text("canonical content\n", encoding="utf-8")
            self.assertEqual(check_mirror_byte_parity(p1, p2), [])
            p2.write_text("drifted content\n", encoding="utf-8")
            self.assertNotEqual(check_mirror_byte_parity(p1, p2), [])

    def test_optional_field_schema_parity_rejections(self) -> None:
        base_claim = {
            "id": "CLM-301",
            "statement": "Optional type parity test",
            "claimed_level": "stated",
            "claim_scope": "formal_statement",
            "genesis": {
                "spec_origin": "human_authored",
                "adequacy_status": "unattested",
                "spec_digest": "1" * 64,
                "genesis_ref": None,
            },
        }
        base_art = {
            "id": "ART-PARITY-01",
            "path": "spec.md",
            "hash_algorithm": "sha256",
            "digest": "a" * 64,
        }

        bad_root = wrap_manifest(base_claim, [base_art])
        bad_root["contract_type"] = 123
        bad_root["quick_check"] = ["not-an-object"]
        bad_root["subject"] = "not-an-object"
        bad_root["evidence_ladder"] = ["stated", "invalid_tier"]
        root_errs = validate_manifest(bad_root, strict=True)
        self.assertTrue(any("INVALID_CONTRACT_TYPE" in e for e in root_errs))
        self.assertTrue(any("INVALID_QUICK_CHECK" in e for e in root_errs))
        self.assertTrue(any("INVALID_SUBJECT" in e for e in root_errs))
        self.assertTrue(any("INVALID_EVIDENCE_LADDER" in e for e in root_errs))

        bad_art = dict(base_art, claimed_level="BOGUS", toolchain=999)
        art_errs = validate_manifest(wrap_manifest(base_claim, [bad_art]), strict=True)
        self.assertTrue(any("INVALID_ARTIFACT_CLAIMED_LEVEL" in e for e in art_errs))
        self.assertTrue(any("INVALID_ARTIFACT_TOOLCHAIN" in e for e in art_errs))

        bad_claim = dict(base_claim, quantity_id=42, refinement_ref=["bad"])
        claim_errs = validate_manifest(wrap_manifest(bad_claim, [base_art]), strict=True)
        self.assertTrue(any("INVALID_CLAIM_QUANTITY_ID" in e for e in claim_errs))
        self.assertTrue(any("INVALID_CLAIM_REFINEMENT_REF" in e for e in claim_errs))


if __name__ == "__main__":
    unittest.main()