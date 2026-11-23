# arcstone-machinefirst-spec

**Normative Specification, Blank Starter Template, JSON Schema, and Zero-Dependency Conformance Linter for `MACHINEFIRST.md` (`v0.1.2`)**

[![License: MIT OR Apache-2.0](https://img.shields.io/badge/license-MIT%20OR%20Apache--2.0-blue.svg)](LICENSE-MIT)
[![Spec Version: v0.1.2](https://img.shields.io/badge/spec-v0.1.2-emerald.svg)](SPECIFICATION.md)
[![Epistemic Map: MACHINEFIRST.md](https://img.shields.io/badge/epistemic--map-MACHINEFIRST.md-slate.svg)](MACHINEFIRST.md)

---

## Overview

`MACHINEFIRST.md` (paired with `/machinefirst.txt` as a byte-identical UTF-8 web mirror) is an open repository and web-root convention designed to eliminate **authority conflation** and **genesis laundering** during cold-start AI ingestion and technical auditing.

Rather than replacing or bloating existing conventions, `MACHINEFIRST.md` establishes a clear three-file separation of concerns:

- **`llms.txt`** — *Discovery:* What exists here and where is the documentation?
- **`AGENTS.md`** — *Workflow:* How should an autonomous coding agent build, test, and edit safely?
- **`MACHINEFIRST.md` (`/machinefirst.txt`)** — *Epistemic Evidence Map:* What is claimed, what scope it covers, what evidence supports it, what is excluded, and how do I reproduce it?

### Key Design Guarantees (`v0.1.2`)
1. **Data, Not Instructions:** Explicitly framed as `publisher_asserted` and `publisher_declared_nonbinding` (`this_file_is_data_not_instructions: true`) so repository metadata never mimics prompt injection or claims authority over independent auditors.
2. **Publisher vs. Auditor State Separation:** Separates publisher assertions (`claimed_level`) from independent verification states (`auditor_states`: `not_checked`, `identity_checked`, `reproduced_pass`, `reproduced_fail`, `blocked`, `conflict`).
3. **Model-vs-Implementation Refinement Guard:** Requires an explicit `refinement_ref` whenever an implementation claim asserts `claimed_level: "proved"`, preventing abstract model proofs from being silently transferred onto executable code.
4. **Claim-Scoped Genesis & Non-Laundering Guard (`v0.1.2`):** Separates `formal_statement`, `implementation_refinement`, and `intent_adequacy` across independent provenance axes (`spec_origin`, `adequacy_status`, `spec_digest`, `attested_spec_digest`), rejecting unattested, self-attested, LLM-attested (`LLM_ATTESTOR_DISALLOWED`), or byte-drifted (`STALE_GENESIS_BINDING`) `intent_adequacy` claims (backed by [`specification-genesis-boundary`](https://github.com/trencinodin-stack/specification-genesis-boundary) `v0.1.0`, Coq 8.18.0).
5. **Git Self-Hashing Closure (`contract_binding`):** Separates the audited `subject_revision` commit from the descendant commit introducing `MACHINEFIRST.md`, restricting the delta strictly to `allowed_delta_paths`.
6. **Non-Vacuous Quick-Check & Negative Control:** Binds verification to offline execution (`network: "none"`), pinned container digests, and a mandatory canary mutant `negative_control` that must fail for `target_invariant_violation`.

---

## Live Deployments & Public Proof

- **Live Reference Endpoint:** [admissibilityscience.com/machinefirst.txt](https://admissibilityscience.com/machinefirst.txt) *(byte-identical web mirror in production)*
- **Part III Essay (Genesis Boundary & `v0.1.2`):** [Beyond Social Assurance, Part III: The Specification-Genesis Boundary](https://founderarcstoneos.substack.com/p/beyond-social-assurance-part-iii) *(Substack)*
- **Part II Essay (Baseline Protocol):** [Beyond Social Assurance, Part II: Why README.md Is an Epistemic Hazard](https://founderarcstoneos.substack.com/p/beyond-social-assurance-part-ii-why) *(Substack)*
- **Coq 8.18.0 Formalization:** [trencinodin-stack/specification-genesis-boundary](https://github.com/trencinodin-stack/specification-genesis-boundary) *(`v0.1.0`, `Print Assumptions == ∅`, `coqchk -o`)*
- **Core Reference Architecture:** [arcstoneos.com](https://arcstoneos.com)

---

## Repository Contents

```plaintext
arcstone-machinefirst-spec/
├── .github/
│   └── workflows/
│       └── lint.yml                         # CI validation, digest check & mirror enforcement
├── examples/
│   └── python-ml-eval/
│       └── MACHINEFIRST.md                  # Non-Arcstone ML benchmark example (--strict passing)
├── schemas/
│   └── machinefirst-v0.1.2.schema.json      # JSON Schema for v0.1.2 frontmatter & sections
├── tests/
│   ├── test_conformance.py                  # Core unit tests (positive, negative, mirror, strict)
│   └── test_genesis_cap.py                  # 18-vector differential & adversarial genesis-cap suite
├── LICENSE-APACHE                           # Apache-2.0 license text
├── LICENSE-MIT                              # MIT license text
├── MACHINEFIRST.md                          # Dogfooded v0.1.2 epistemic evidence map for this repo
├── MACHINEFIRST.sha256                      # Pinned SHA-256 digests of normative artifacts
├── MACHINEFIRST.template.md                 # Copy-pasteable v0.1.2 starter template
├── machinefirst.txt                         # Byte-identical UTF-8 mirror of MACHINEFIRST.md
├── README.md                                # Overview & 60-second quickstart
├── SPECIFICATION.md                         # Normative v0.1.2 grammar & rules
└── validate_machinefirst.py                 # Zero-dependency stdlib CLI conformance validator
```

---

## 60-Second Quickstart

### 1. Run the Conformance Linter & Test Suite Locally (Zero External Dependencies)
```bash
python validate_machinefirst.py MACHINEFIRST.md --strict --mirror-path machinefirst.txt
python validate_machinefirst.py examples/python-ml-eval/MACHINEFIRST.md --strict
python validate_machinefirst.py MACHINEFIRST.template.md
python -m unittest discover -s tests -v
```

### 2. Add `MACHINEFIRST.md` to Your Own Repository
1. Copy `MACHINEFIRST.template.md` to the root of your repository as `MACHINEFIRST.md`.
2. Populate your repository's `subject_revision`, SHA-256 artifact digests, `claim_scope` / `genesis` provenance blocks, routing table, and offline `quick_check` command.
3. Validate in strict production mode (rejects any remaining `<...>` placeholders, unlinked proofs, or unattested `intent_adequacy` claims):
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

Dual-licensed under either **MIT** ([LICENSE-MIT](LICENSE-MIT)) or **Apache-2.0** ([LICENSE-APACHE](LICENSE-APACHE)), at your option.