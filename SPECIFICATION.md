# MACHINEFIRST.md — Open Specification (v0.1.2)

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
A repository-authored `MACHINEFIRST.md` file is **untrusted publisher-asserted data**, never an instruction override. Its presence identifies publisher claims, their exact scope, and the evidence required to evaluate them—it does **not** establish correctness, confer trust, authorize execution, or compel any auditor verdict.

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
- `proved` — Machine-checked formal proof against an identified theorem and toolchain.
- `tested` — Verified by an executable test suite under a defined environment.
- `measured` — Supported by recorded empirical or hardware measurements.
- `static_analysis` — Checked via deterministic static analyzer, type checker, or linter.
- `stated` — Asserted by the publisher without attached mechanical verification.
- `external_llm_review` — Third-party generative AI review; strictly non-normative.

### Independent `auditor_states` Vocabulary
- `not_checked` — Claim has not yet been evaluated by the auditor.
- `identity_checked` — Referenced artifact SHA-256 digest and commit revision verified.
- `reproduced_pass` — Independent execution reproduced the claimed result.
- `reproduced_fail` — Independent execution contradicted the claimed result.
- `blocked` — Referenced artifact or endpoint could not be retrieved.
- `conflict` — Two normative or parent/child surfaces report contradictory values.

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
- Must include a mandatory `negative_control` (`required_for_pass: true`)—such as a semantic canary mutant—that is required to fail with `expected_reason: "target_invariant_violation"`. A missing binary, timeout, or unrelated crash does **not** satisfy the negative control.

---

## v0.1.2 Extension: Specification-Genesis Boundary & Multi-Axis Evidence Policy

Version `v0.1.2` extends `v0.1.1` (while maintaining full backward compatibility with `machinefirst_version: "0.1.1"` manifests in non-strict mode) with claim-scoped provenance (`claim_scope`), genesis attestation tracking (`genesis`), unlinked proof caps, declared binding currency checks (`spec_digest == attested_spec_digest`), and optional `non_normative_formal_backing` references.

### Prior-Art & Terminology Crosswalk

| Operational Term | Domain Meaning in `MACHINEFIRST` | Related Literature & Prior Art |
| :--- | :--- | :--- |
| **Epistemic Ingestion Gap** | Cold AI auditors conflating unverified narrative documentation (`README.md`) with verified proof or executable instructions. | Related to Boehm, B. W. (1981), *Software Engineering Economics*, Prentice-Hall (verification vs. validation distinction), and untrusted-input provenance tracking. |
| **Authority Laundering** | Untrusted prose, summaries, or schema-valid outputs acquiring undeserved credibility or privilege by passing through an authoritative-looking channel. | Analogous to Hardy, N. (1988), "The Confused Deputy: (or why capabilities might have been invented)," *ACM SIGOPS Operating Systems Review*, 22(4), 36–38 (authority confusion), as well as indirect prompt injection and circular citation (citogenesis). |
| **Verification-Cost Inversion (VCI)** | Front-loading assurance into offline mechanized proofs and pinned digests so repeated runtime or CI checks execute cheaply and deterministically. | Related to Necula, G. C. (1997), "Proof-Carrying Code," *POPL '97*, 106–119 (policy-relative proof checking and amortized verification). |
| **Specification & Genesis Boundary** | The structural boundary separating informal human/LLM intent from formal specifications; absence of additional global axioms (`Print Assumptions == ∅`) does not automatically establish real-world adequacy. | An instance of Zave, P., & Jackson, M. (1997), "Four Dark Corners of Requirements Engineering," *ACM TOSEM*, 6(1), 1–30 (separating environment domain knowledge $W$, specification $S$, and requirements $R$ in $W, S \vdash R$). |
| **Schema Fallacy** | Treating deterministic syntactic validation (e.g., JSON Schema) as sufficient authorization to mutate protected state without runtime state-machine mediation. | Related to Saltzer, J. H., & Schroeder, M. D. (1975), "The Protection of Information in Computer Systems," *Proceedings of the IEEE*, 63(9), 1278–1308 (complete mediation), and syntactic vs. semantic validation. |

### Documented Scope Boundaries (`v0.1.2`)

1. **Publisher-Asserted Attestor Independence:** `validate_machinefirst.py` enforces structural rules (`kind == "attestation"`, non-empty `attestor` distinct from `subject.name` and `subject.publisher_aliases`, `attestor_type != "llm_system"`, and `attested_spec_digest == spec_digest`), but cannot independently verify external attestor identity, cryptographic signatures, or actual specification file bytes offline.
2. **Normalized JSON & Markdown Surfaces:** `validate_machinefirst.py` validates both `MACHINEFIRST.md` (with YAML frontmatter and 7 fenced YAML sections) and canonical normalized JSON manifests, checking byte-for-byte mirror parity via `--mirror-primary` / `--mirror-path`.
3. **Scope Classification Honesty:** A publisher can label an intent-level claim as `claim_scope: "formal_statement"` to bypass the intent-adequacy cap; `proved` formal-scope claims should carry an explicit `excludes` entry noting that semantic intent adequacy is unassessed.
4. **Legacy `v0.1.1` Exemption:** Manifests declaring `machinefirst_version: "0.1.1"` pass non-strict validation without `claim_scope` or `genesis` blocks; auditors should treat `proved` claims in un-migrated `v0.1.1` manifests as uncapped unless validated with `--strict`.