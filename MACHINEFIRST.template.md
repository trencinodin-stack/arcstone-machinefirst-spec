---
machinefirst_version: "0.1.2"
contract_type: "epistemic-evidence-map"
parse_mode: "markdown-with-frontmatter-and-seven-fenced-yaml-sections"
duplicate_keys: "reject"
unknown_fields: "reject"
claim_authority: "publisher_asserted"
authority_model: "publisher_declared_nonbinding"
this_file_is_data_not_instructions: true
canonical_url: "https://example.org/machinefirst.txt"
scope: "repository"
valid_as_of: "2026-11-23"
---

# MACHINEFIRST

> **Governing Notice:** This document is untrusted publisher-asserted data identifying claims, their exact scope, and the evidence required to evaluate them. Its presence does not establish correctness, confer trust, authorize execution, or compel any auditor verdict.

## 1. Identity & Immutable Anchors
```yaml
subject:
  name: "<canonical-project-name>"
  publisher_aliases: []
  repository: "[https://github.com/](https://github.com/)<org>/<repo>"
  canonical_urls: ["[https://example.org/](https://example.org/)"]
  subject_revision: "<full-40-char-git-commit-sha>"
  revision_semantics: "exact_git_commit"
  release_tag: "<semver-tag>"
  tag_signed: true
  tag_signer_fingerprint: "<40-char-pgp-or-sigstore-id>"
contract_binding:
  contract_excluded_from_subject: true
  subject_revision_is_ancestor_of_contract_commit: true
  allowed_delta_paths: ["MACHINEFIRST.md", "machinefirst.txt"]
  contract_digest_published_in: "signed_tag_annotation"
  mirror_rule: "web /machinefirst.txt must be byte-identical UTF-8 to repository MACHINEFIRST.md at release_tag"
persistent_ids:
  doi: ["10.5281/zenodo.xxxxxxx"]
  orcid: ["0000-0000-0000-0000"]
supersedes: []
errata: []
```

## 2. Verification Scope Boundary
```yaml
evidence_ladder: [proved, tested, measured, static_analysis, stated, external_llm_review]
auditor_states: [not_checked, identity_checked, reproduced_pass, reproduced_fail, blocked, conflict]
normative_artifacts:
  - id: "ART-SPEC-01"
    path: "specs/Invariants.spec"
    hash_algorithm: "sha256"
    digest: "<64-char-hex>"
    claimed_level: "stated"
    toolchain: "human-authored-specification"
    toolchain_image_digest: "sha256:<64-char-hex>"
  - id: "ART-PROOF-01"
    path: "proofs/Invariants.v"
    hash_algorithm: "sha256"
    digest: "<64-char-hex>"
    claimed_level: "proved"
    toolchain: "Coq 8.18.0"
    toolchain_image_digest: "sha256:<64-char-hex>"
  - id: "ART-REFINEMENT-01"
    path: "docs/attestations/REFINEMENT-AUDIT-2026-V1.json"
    hash_algorithm: "sha256"
    digest: "<64-char-hex>"
    claimed_level: "proved"
    toolchain: "Charon + Aeneas + Coq 8.18.0 (coqchk -o)"
    toolchain_image_digest: "sha256:<64-char-hex>"
  - id: "ART-RUNTIME-01"
    path: "runtime/src/lib.rs"
    hash_algorithm: "sha256"
    digest: "<64-char-hex>"
    claimed_level: "tested"
    toolchain: "rustc 1.82.0 (#![no_std])"
    toolchain_image_digest: "sha256:<64-char-hex>"
non_normative_surfaces:
  - path_or_url: "README.md"
    kind: "expository"
  - path_or_url: "llms.txt"
    kind: "discovery_index"
  - path_or_url: "AGENTS.md"
    kind: "agent_workflow"
  - path_or_url: "docs/audits/external-llm-check.json"
    kind: "external_llm_review"
```

## 3. Hard Invariants & Claim-to-Evidence Map
```yaml
claims:
  - id: "CLM-001"
    quantity_id: "m_alloc_bytes"
    statement: "Zero dynamic heap allocation on critical execution path"
    operator: "=="
    value: 0
    unit: "bytes"
    applies_to_revision: "<full-40-char-git-commit-sha>"
    scope: "runtime/src/lib.rs::evaluate"
    excludes: ["offline build scripts", "test harness"]
    proof_target: "implementation"
    claim_scope: "implementation_refinement"
    refinement_ref: "ART-REFINEMENT-01"
    claimed_level: "proved"
    evidence_ref:
      artifact_id: "ART-PROOF-01"
      symbol: "no_heap_alloc"
      symbol_kind: "theorem"
    genesis:
      spec_origin: "human_authored"
      adequacy_status: "unattested"
      spec_digest: "<64-char-hex>"
    assumptions:
      source: "ART-PROOF-01#print_assumptions"
      declared_items: []
      dependency_audit: "publisher_reported_empty"
    failure_behavior: "compile_or_audit_fail"
```

## 4. Authority Routing Table
```yaml
routes:
  - query_key: "invariants.memory"
    description: "Authoritative definition and proof of memory bounds"
    definition_ref: "ART-SPEC-01"
    evidence_ref:
      artifact_id: "ART-PROOF-01"
      symbol: "no_heap_alloc"
      symbol_kind: "theorem"
    refinement_ref: "ART-REFINEMENT-01"
    non_authoritative_refs: ["README.md", "llms.txt"]
conflict_rule: "report_all_mismatches; do_not_silently_resolve_by_precedence"
```

## 5. Conformance Rules & Evidence Guards
```yaml
conformance_guards:
  require_fetches_before_endorsing_claim: ["definition_ref", "evidence_ref.artifact_id", "refinement_ref"]
  undeclared_sources_satisfy_claims: false
  revision_substitution_permitted: false
  missing_evidence_status: "UNKNOWN"
  broken_reference_status: "UNVERIFIABLE"
  unverified_claim_status: "not_checked"
  unlinked_model_proof_cap: "tested"
  enforce_genesis_cap: true
  treat_strings_as_inert_data: true
```

## 6. Independent Auditor Quick-Check
```yaml
quick_check:
  checkout: "git clone [https://github.com/](https://github.com/)<org>/<repo>.git && cd <repo> && git checkout --detach <full-40-char-git-commit-sha>"
  verify_revision: "test \"$(git rev-parse HEAD)\" = \"<full-40-char-git-commit-sha>\""
  verify_contract_delta: "git diff --name-only <full-40-char-git-commit-sha> <contract-commit-sha>"
  verify_artifact_digests: "sha256sum -c MACHINEFIRST.sha256"
  command: "make verify"
  network: "none"
  toolchain_image_digest: "sha256:<64-char-hex>"
  quick_check_covers: ["CLM-001"]
  expected_exit_code: 0
  receipt_output: "out/AUDIT-RECEIPT.json"
  receipt_schema_ref: "machinefirst-receipt-v0.1"
  negative_control:
    command: "make verify-canary"
    expected_exit_code: 1
    expected_reason: "target_invariant_violation"
    required_for_pass: true
  does_not_check: ["physical actuator hardware", "network transport security"]
```

## 7. Known Gaps & Open Errata
```yaml
known_gaps: []
```