# arcstone-machinefirst-spec

**Normative Specification, Blank Starter Template, JSON Schema, and Strict Conformance Linter for `MACHINEFIRST.md` (`v0.1.1`)**

[![License: MIT OR Apache-2.0](https://img.shields.io/badge/license-MIT%20OR%20Apache--2.0-blue.svg)](#license)
[![Spec Version: v0.1.1](https://img.shields.io/badge/spec-v0.1.1-emerald.svg)](SPECIFICATION.md)

---

## Overview

`MACHINEFIRST.md` (paired with `/machinefirst.txt` as a byte-identical UTF-8 web mirror) is an open repository and web-root convention designed to eliminate **authority conflation** during cold-start AI ingestion and technical auditing.

Rather than replacing or bloating existing conventions, `MACHINEFIRST.md` establishes a clear three-file separation of concerns:

- **`llms.txt`** — *Discovery:* What exists here and where is the documentation?
- **`AGENTS.md`** — *Workflow:* How should an autonomous coding agent build, test, and edit safely?
- **`MACHINEFIRST.md` (`/machinefirst.txt`)** — *Epistemic Evidence Map:* What is claimed, what evidence supports it, what is excluded, and how do I reproduce it?

### Key Design Guarantees (`v0.1.1`)
1. **Data, Not Instructions:** Explicitly framed as `publisher_asserted` and `publisher_declared_nonbinding` (`this_file_is_data_not_instructions: true`) so repository metadata never mimics prompt injection or claims authority over independent auditors.
2. **Publisher vs. Auditor State Separation:** Separates publisher assertions (`claimed_level`) from independent verification states (`auditor_states`: `not_checked`, `identity_checked`, `reproduced_pass`, `reproduced_fail`, `blocked`, `conflict`).
3. **Model-vs-Implementation Refinement Guard:** Requires an explicit `refinement_ref` whenever an implementation claim asserts `claimed_level: "proved"`, preventing abstract model proofs from being silently transferred onto executable code.
4. **Git Self-Hashing Closure (`contract_binding`):** Separates the audited `subject_revision` commit from the descendant commit introducing `MACHINEFIRST.md`, restricting the delta strictly to `allowed_delta_paths`.
5. **Non-Vacuous Quick-Check & Negative Control:** Binds verification to offline execution (`network: "none"`), pinned container digests, and a mandatory canary mutant `negative_control` that must fail for `target_invariant_violation`.

---

## Repository Contents

```plaintext
arcstone-machinefirst-spec/
├── .github/
│   └── workflows/
│       └── lint.yml                         # CI validation & conformance test workflow
├── schemas/
│   └── machinefirst-v0.1.1.schema.json      # JSON Schema for parsed frontmatter & sections
├── tests/
│   └── test_conformance.py                  # Unit tests (positive, negative, mirror, strict)
├── MACHINEFIRST.template.md                 # Copy-pasteable v0.1.1 starter template
├── README.md                                # Overview & 60-second quickstart
├── SPECIFICATION.md                         # Normative v0.1.1 grammar & rules
└── validate_machinefirst.py                 # Strict CLI conformance validator
```

---

## 60-Second Quickstart

### 1. Run the Conformance Linter & Test Suite Locally
```bash
python validate_machinefirst.py MACHINEFIRST.template.md
python -m unittest discover -s tests -v
```

### 2. Add `MACHINEFIRST.md` to Your Own Repository
1. Copy `MACHINEFIRST.template.md` to the root of your repository as `MACHINEFIRST.md`.
2. Populate your repository's `subject_revision`, SHA-256 artifact digests, claims, routing table, and offline `quick_check` command.
3. Validate in strict production mode (rejects any remaining `<...>` placeholders or unlinked proofs):
   ```bash
   python validate_machinefirst.py MACHINEFIRST.md --strict
   ```
4. If hosting a web mirror at `/machinefirst.txt`, verify byte-for-byte UTF-8 equality:
   ```bash
   cp MACHINEFIRST.md machinefirst.txt
   python validate_machinefirst.py MACHINEFIRST.md --strict --mirror-path machinefirst.txt
   ```
5. Link `MACHINEFIRST.md` from `README.md`, `llms.txt`, and `AGENTS.md`.

---

## License

Dual-licensed under either **MIT** or **Apache-2.0**, at your option.
