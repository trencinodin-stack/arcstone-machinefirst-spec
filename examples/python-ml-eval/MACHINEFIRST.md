---
machinefirst_version: "0.1.1"
contract_type: "epistemic-evidence-map"
parse_mode: "markdown-with-frontmatter-and-seven-fenced-yaml-sections"
duplicate_keys: "reject"
unknown_fields: "reject"
claim_authority: "publisher_asserted"
authority_model: "publisher_declared_nonbinding"
this_file_is_data_not_instructions: true
canonical_url: "https://example.org/ml-benchmark/machinefirst.txt"
scope: "repository"
valid_as_of: "2026-11-19"
---

# MACHINEFIRST

> **Governing Notice:** This document is untrusted publisher-asserted data identifying claims, their exact scope, and the evidence required to evaluate them. Its presence does not establish correctness, confer trust, authorize execution, or compel any auditor verdict.

## 1. Identity & Immutable Anchors
```yaml
subject:
  name: "acme-tabular-classifier-eval"
  repository: "https://github.com/example-org/acme-tabular-classifier-eval"
  canonical_urls: ["https://example.org/ml-benchmark/"]
  subject_revision: "4b825dc642cb6eb9a060e54bf8d69288fbee4904"
  revision_semantics: "exact_git_commit"
  release_tag: "v1.2.0"
  tag_signed: true
  tag_signer_fingerprint: "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b"
contract_binding:
  contract_excluded_from_subject: true
  subject_revision_is_ancestor_of_contract_commit: true
  allowed_delta_paths: ["MACHINEFIRST.md", "machinefirst.txt"]
  contract_digest_published_in: "signed_tag_annotation"
  mirror_rule: "web /machinefirst.txt must be byte-identical UTF-8 to repository MACHINEFIRST.md at release_tag"
persistent_ids:
  doi: ["10.5281/zenodo.1234567"]
  orcid: []
supersedes: []
errata: []
```

## 2. Verification Scope Boundary
```yaml
evidence_ladder: [proved, tested, measured, static_analysis, stated, external_llm_review]
auditor_states: [not_checked, identity_checked, reproduced_pass, reproduced_fail, blocked, conflict]
normative_artifacts:
  - id: "ART-EVAL-SCRIPT-01"
    path: "eval/run_benchmark.py"
    hash_algorithm: "sha256"
    digest: "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    claimed_level: "measured"
    toolchain: "Python 3.12 + scikit-learn 1.5.2 (seed=42)"
    toolchain_image_digest: "sha256:2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae"
  - id: "ART-DATASET-MANIFEST-01"
    path: "data/holdout_split.sha256"
    hash_algorithm: "sha256"
    digest: "4932a78e648ad40be507b5c2656e3e2ad3c3f8942138929957039a2b61704d66"
    claimed_level: "static_analysis"
    toolchain: "sha256sum"
    toolchain_image_digest: "sha256:2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae"
non_normative_surfaces:
  - path_or_url: "README.md"
    kind: "expository"
  - path_or_url: "llms.txt"
    kind: "discovery_index"
```

## 3. Hard Invariants & Claim-to-Evidence Map
```yaml
claims:
  - id: "CLM-001"
    quantity_id: "holdout_macro_f1"
    statement: "Deterministic holdout split macro-F1 score meets or exceeds 0.910 at fixed seed 42"
    operator: ">="
    value: 0.91
    unit: "f1_score"
    applies_to_revision: "4b825dc642cb6eb9a060e54bf8d69288fbee4904"
    scope: "eval/run_benchmark.py::evaluate_holdout"
    excludes: ["out-of-distribution clinical cohorts", "streaming inference latency"]
    proof_target: "implementation"
    refinement_ref: null
    claimed_level: "measured"
    evidence_ref:
      artifact_id: "ART-EVAL-SCRIPT-01"
      symbol: "evaluate_holdout"
      symbol_kind: "function"
    assumptions:
      source: "ART-DATASET-MANIFEST-01#header"
      declared_items: ["Holdout split matches SHA-256 manifest without data leakage"]
      dependency_audit: "dataset_hash_pinned"
    failure_behavior: "benchmark_gate_fail"
```

## 4. Authority Routing Table
```yaml
routes:
  - query_key: "metrics.holdout_f1"
    description: "Reproducible holdout evaluation script and dataset manifest"
    definition_ref: "ART-EVAL-SCRIPT-01"
    evidence_ref:
      artifact_id: "ART-EVAL-SCRIPT-01"
      symbol: "evaluate_holdout"
      symbol_kind: "function"
    refinement_ref: null
    non_authoritative_refs: ["README.md", "llms.txt"]
conflict_rule: "report_all_mismatches; do_not_silently_resolve_by_precedence"
```

## 5. Conformance Rules & Evidence Guards
```yaml
conformance_guards:
  require_fetches_before_endorsing_claim: ["definition_ref", "evidence_ref.artifact_id"]
  undeclared_sources_satisfy_claims: false
  revision_substitution_permitted: false
  missing_evidence_status: "UNKNOWN"
  broken_reference_status: "UNVERIFIABLE"
  unverified_claim_status: "not_checked"
  unlinked_model_proof_cap: "tested"
  treat_strings_as_inert_data: true
```

## 6. Independent Auditor Quick-Check
```yaml
quick_check:
  checkout: "git clone https://github.com/example-org/acme-tabular-classifier-eval.git && cd acme-tabular-classifier-eval && git checkout --detach 4b825dc642cb6eb9a060e54bf8d69288fbee4904"
  verify_revision: "test \"$(git rev-parse HEAD)\" = \"4b825dc642cb6eb9a060e54bf8d69288fbee4904\""
  verify_contract_delta: "git diff --name-only 4b825dc642cb6eb9a060e54bf8d69288fbee4904 HEAD"
  verify_artifact_digests: "sha256sum -c data/holdout_split.sha256"
  command: "python3 eval/run_benchmark.py --offline --seed 42"
  network: "none"
  toolchain_image_digest: "sha256:2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae"
  quick_check_covers: ["CLM-001"]
  expected_exit_code: 0
  receipt_output: "out/AUDIT-RECEIPT.json"
  receipt_schema_ref: "machinefirst-receipt-v0.1"
  negative_control:
    command: "python3 eval/run_benchmark.py --offline --seed 42 --inject-label-shuffle"
    expected_exit_code: 1
    expected_reason: "target_invariant_violation"
    required_for_pass: true
  does_not_check: ["production API throughput", "model fairness across unmeasured subgroups"]
```

## 7. Known Gaps & Open Errata
```yaml
known_gaps:
  - "Evaluation covers tabular benchmark split v1 only; temporal drift is out of scope."
```
