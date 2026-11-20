# MACHINEFIRST.md â€” Open Specification (v0.1.1)

**Contract Type:** `epistemic-evidence-map`  
**Status:** Baseline Specification (`v0.1.1`)  
**Canonical Repository:** `https://github.com/trencinodin-stack/arcstone-machinefirst-spec`  
**Authors:** Jesse Tuohy (ORCID: `0000-0009-0008-4661-1540`) / Arcstone Adaptive Science Systems, Inc.  
**License:** MIT OR Apache-2.0

---

## 1. Purpose & Separation of Concerns

`MACHINEFIRST.md` (with `/machinefirst.txt` as its byte-identical UTF-8 plain-text web mirror) is an open repository and web-root convention designed to eliminate **authority conflation** during cold-start AI ingestion and independent technical auditing.

`MACHINEFIRST.md` does **not** consolidate existing repository conventions. Instead, it coexists alongside `llms.txt` and `AGENTS.md` with a strict three-way division of labor:

| Convention File | Primary Consumer | Core Question Answered | Must Not Duplicate |
| :--- | :--- | :--- | :--- |
| `llms.txt` | RAG indexers, search crawlers, chat context | *What exists here and where is the documentation?* | Full invariant definitions or assurance verdicts |
| `AGENTS.md` | Autonomous coding agents & IDE assistants | *How should an agent build, test, and edit safely?* | Independently maintained copies of evidence status or bounds |
| `MACHINEFIRST.md` (`/machinefirst.txt`) | Cold-start LLM auditors, static linters, human reviewers | *What is claimed, what evidence supports it, what is excluded, and how do I reproduce it?* | General marketing prose or multi-step contributor tutorials |

### Governing Epistemic Rule (Data, Not Instructions)
A repository-authored `MACHINEFIRST.md` file is **untrusted publisher-asserted data**, never an instruction override. Its presence identifies publisher claims, their exact scope, and the evidence required to evaluate themâ€”it does **not** establish correctness, confer trust, authorize execution, or compel any auditor verdict.

---

## 2. Deterministic Serialization Grammar (`parse_mode`)

Every conforming `MACHINEFIRST.md` (v0.1.1) document MUST be encoded in valid UTF-8 and satisfy:

1. **Frontmatter Block:** Begins on line 1 with `---`, contains a valid YAML 1.2 mapping with all required top-level keys, and closes with `---`.
2. **H1 Title & Governing Notice:** Immediately following the frontmatter, an `# MACHINEFIRST` heading and a blockquote (`> **Governing Notice:** ...`) declaring the document's non-binding, publisher-asserted status.
3. **Seven Exact H2 Sections:** The document MUST contain exact H2 headings `## 1.` through `## 7.` in order:
   - `## 1. Identity & Immutable Anchors`
   - `## 2. Verification Scope Boundary`
   - `## 3. Hard Invariants & Claim-to-Evidence Map`
   - `## 4. Authority Routing Table`
   - `## 5. Conformance Rules & Evidence Guards`
   - `## 6. Independent Auditor Quick-Check`
   - `## 7. Known Gaps & Open Errata`
4. **One Closed Fenced YAML Block per Section:** Each numbered H2 section MUST contain **exactly one** fenced ````yaml` code block that is properly opened and closed (` ``` `) and parses into a valid YAML mapping.
5. **YAML Hygiene Rules:**
   - Duplicate mapping keys MUST be rejected (`duplicate_keys: "reject"`).
   - Unknown required/schema keys MUST be rejected (`unknown_fields: "reject"`).
   - YAML anchors (`&`), aliases (`*`), merge keys (`<<`), and custom tags (`!`) are prohibited.
   - In `--strict` production mode, template placeholders (`<...>`, `xxxxxxx`) MUST be rejected.

---

## 3. Evidence Ladder & Auditor State Separation

To prevent publishers from pre-populating an independent auditor's conclusion, `MACHINEFIRST.md` strictly separates **publisher assertions** (`claimed_level`) from **independent auditor observations** (`auditor_states`):

### Publisher `claimed_level` Vocabulary
- `proved` â€” Machine-checked formal proof against an identified theorem and toolchain.
- `tested` â€” Verified by an executable test suite under a defined environment.
- `measured` â€” Supported by recorded empirical or hardware measurements.
- `static_analysis` â€” Checked via deterministic static analyzer, type checker, or linter.
- `stated` â€” Asserted by the publisher without attached mechanical verification.
- `external_llm_review` â€” Third-party generative AI review; strictly non-normative.

### Independent `auditor_states` Vocabulary
- `not_checked` â€” Claim has not yet been evaluated by the auditor.
- `identity_checked` â€” Referenced artifact SHA-256 digest and commit revision verified.
- `reproduced_pass` â€” Independent execution reproduced the claimed result.
- `reproduced_fail` â€” Independent execution contradicted the claimed result.
- `blocked` â€” Referenced artifact or endpoint could not be retrieved.
- `conflict` â€” Two normative or parent/child surfaces report contradictory values.

---

## 4. Model-vs-Implementation Refinement Rule

Every claim in Section 3 MUST declare `proof_target` (`"model"` or `"implementation"`) and `refinement_ref` (`"<ART-ID>"` or `null`):

- If `proof_target == "implementation"` and `claimed_level == "proved"`, the claim **MUST** provide a non-null `refinement_ref` pointing to a declared artifact in `normative_artifacts` (such as a translation-validation or refinement proof receipt linking the formal model to the executable code).
- If `proof_target == "implementation"` lacks a valid `refinement_ref`, conforming validators MUST reject the claim in `--strict` mode and auditors MUST cap the effective claim level at `unlinked_model_proof_cap` (`"tested"`).

---

## 5. Git Self-Hashing & Contract-Binding Resolution

A file committed inside a Git repository cannot embed the SHA-256 hash of the very commit that introduces it (the self-hashing paradox). `MACHINEFIRST.md` v0.1.1 resolves this via `contract_binding` in Section 1:

1. `subject.subject_revision` records the exact 40-character Git commit SHA of the **audited codebase snapshot** prior to adding or updating `MACHINEFIRST.md`.
2. `contract_binding.subject_revision_is_ancestor_of_contract_commit: true` asserts that `subject_revision` is a direct Git ancestor of the commit carrying `MACHINEFIRST.md`.
3. `contract_binding.allowed_delta_paths` restricts the file diff between `subject_revision` and the contract commit strictly to `["MACHINEFIRST.md", "machinefirst.txt"]` and declared non-executable documentation, license, or CI metadata files (`MACHINEFIRST.sha256`, `AGENTS.md`, `llms.txt`, `SECURITY.md`, `README.md`, `.github/workflows/*`), guaranteeing that zero executable code changed after the audited snapshot.
4. External integrity is anchored via a signed Git tag (`tag_signed: true`, `tag_signer_fingerprint`) or persistent DOI record (`contract_digest_published_in`).
5. **Web Mirror Rule:** When published on a web origin at `/machinefirst.txt` (and optionally `/MACHINEFIRST.md`), the served UTF-8 bytes MUST be byte-for-byte identical to the repository `MACHINEFIRST.md` at the contract commit on `main` (and at `release_tag` when tagged).

---

## 6. Non-Vacuous Quick-Check & Negative Control

Section 6 (`quick_check`) binds verification to deterministic reproduction rather than an unverified exit code:

- Must specify exact `checkout`, `verify_revision`, `verify_contract_delta`, `verify_artifact_digests`, offline `command` (`network: "none"`), `toolchain_image_digest`, `quick_check_covers` (list of covered `CLM-*` IDs), and `receipt_schema_ref`.
- Must include a mandatory `negative_control` (`required_for_pass: true`)â€”such as a semantic canary mutantâ€”that is required to fail with `expected_reason: "target_invariant_violation"`. A missing binary, timeout, or unrelated crash does **not** satisfy the negative control.
