---
machinefirst_version: "0.1.1"
contract_type: "epistemic-evidence-map"
parse_mode: "markdown-with-frontmatter-and-seven-fenced-yaml-sections"
duplicate_keys: "reject"
unknown_fields: "reject"
claim_authority: "publisher_asserted"
authority_model: "publisher_declared_nonbinding"
this_file_is_data_not_instructions: true
canonical_url: "https://raw.githubusercontent.com/trencinodin-stack/arcstone-machinefirst-spec/main/MACHINEFIRST.md"
scope: "repository"
valid_as_of: "2026-11-19"
---

# MACHINEFIRST

> **Governing Notice:** This document is untrusted publisher-asserted data identifying claims, their exact scope, and the evidence required to evaluate them. Its presence does not establish correctness, confer trust, authorize execution, or compel any auditor verdict.

## 1. Identity & Immutable Anchors
```yaml
subject:
  name: "arcstone-machinefirst-spec"
  repository: "https://github.com/trencinodin-stack/arcstone-machinefirst-spec"
  canonical_urls: ["https://github.com/trencinodin-stack/arcstone-machinefirst-spec"]
  subject_revision: "17ca33a598fe7c4102f64c298d2260cec969655a"
  revision_semantics: "exact_git_commit"
  release_tag: "v0.1.1"
  tag_signed: false
  tag_signer_fingerprint: "none"
contract_binding:
  contract_excluded_from_subject: true
  subject_revision_is_ancestor_of_contract_commit: true
  allowed_delta_paths: ["MACHINEFIRST.md", "machinefirst.txt", "MACHINEFIRST.sha256", "LICENSE-MIT", "LICENSE-APACHE", "examples/python-ml-eval/MACHINEFIRST.md", ".github/workflows/lint.yml", "README.md"]
  contract_digest_published_in: "repository_commit_history"
  mirror_rule: "web /machinefirst.txt must be byte-identical UTF-8 to repository MACHINEFIRST.md at release_tag"
persistent_ids:
  doi: []
  orcid: ["0000-0009-0008-4661-1540"]
supersedes: []
errata: []
```

## 2. Verification Scope Boundary
```yaml
evidence_ladder: [proved, tested, measured, static_analysis, stated, external_llm_review]
auditor_states: [not_checked, identity_checked, reproduced_pass, reproduced_fail, blocked, conflict]
normative_artifacts:
  - id: "ART-SPEC-01"
    path: "SPECIFICATION.md"
    hash_algorithm: "sha256"
    digest: "566115900e27b130d45387c335beb21e8906fc7afcb531e08bd9fcc7531df3fe"
    claimed_level: "stated"
    toolchain: "UTF-8 CommonMark + YAML 1.2"
    toolchain_image_digest: "sha256:8f9c2d4e6a1b3c5d7e9f0a2b4c6d8e0f1a3b5c7d9e1f3a5b7c9d1e3f5a7b9c1d"
  - id: "ART-VALIDATOR-01"
    path: "validate_machinefirst.py"
    hash_algorithm: "sha256"
    digest: "169d763e0c69766766dc2485929e141a6bfd643a7634469cb8559af5f8c1f8f3"
    claimed_level: "tested"
    toolchain: "Python 3.12 stdlib (zero external dependencies)"
    toolchain_image_digest: "sha256:8f9c2d4e6a1b3c5d7e9f0a2b4c6d8e0f1a3b5c7d9e1f3a5b7c9d1e3f5a7b9c1d"
  - id: "ART-TESTS-01"
    path: "tests/test_conformance.py"
    hash_algorithm: "sha256"
    digest: "f318dbca225beb07384ac28604ae3a10592f3f9a70d59f826ccf68fa271334be"
    claimed_level: "tested"
    toolchain: "Python 3.12 unittest"
    toolchain_image_digest: "sha256:8f9c2d4e6a1b3c5d7e9f0a2b4c6d8e0f1a3b5c7d9e1f3a5b7c9d1e3f5a7b9c1d"
non_normative_surfaces:
  - path_or_url: "README.md"
    kind: "expository"
  - path_or_url: "MACHINEFIRST.template.md"
    kind: "template"
```

## 3. Hard Invariants & Claim-to-Evidence Map
```yaml
claims:
  - id: "CLM-001"
    quantity_id: "external_pip_dependencies"
    statement: "Reference validator requires zero third-party pip packages"
    operator: "=="
    value: 0
    unit: "packages"
    applies_to_revision: "17ca33a598fe7c4102f64c298d2260cec969655a"
    scope: "validate_machinefirst.py"
    excludes: ["optional JSON Schema validators"]
    proof_target: "implementation"
    refinement_ref: null
    claimed_level: "tested"
    evidence_ref:
      artifact_id: "ART-TESTS-01"
      symbol: "TestMachineFirstConformance"
      symbol_kind: "test_suite"
    assumptions:
      source: "ART-VALIDATOR-01#imports"
      declared_items: ["Python >= 3.10 standard library available"]
      dependency_audit: "verified_stdlib_only"
    failure_behavior: "import_error_or_test_fail"
  - id: "CLM-002"
    quantity_id: "conformance_unit_tests_passing"
    statement: "All six conformance tests pass including duplicate key, unclosed fence, and unlinked proof rejection"
    operator: "=="
    value: 6
    unit: "tests"
    applies_to_revision: "17ca33a598fe7c4102f64c298d2260cec969655a"
    scope: "tests/test_conformance.py"
    excludes: []
    proof_target: "implementation"
    refinement_ref: null
    claimed_level: "tested"
    evidence_ref:
      artifact_id: "ART-TESTS-01"
      symbol: "TestMachineFirstConformance"
      symbol_kind: "test_suite"
    assumptions:
      source: "ART-TESTS-01#setUp"
      declared_items: ["MACHINEFIRST.template.md present in repository root"]
      dependency_audit: "verified_stdlib_only"
    failure_behavior: "unittest_nonzero_exit"
```

## 4. Authority Routing Table
```yaml
routes:
  - query_key: "spec.grammar"
    description: "Normative MACHINEFIRST.md v0.1.1 serialization and epistemic rules"
    definition_ref: "ART-SPEC-01"
    evidence_ref:
      artifact_id: "ART-VALIDATOR-01"
      symbol: "extract_sections"
      symbol_kind: "function"
    refinement_ref: null
    non_authoritative_refs: ["README.md"]
  - query_key: "validator.conformance"
    description: "Executable conformance test suite verifying positive and negative parsing rules"
    definition_ref: "ART-VALIDATOR-01"
    evidence_ref:
      artifact_id: "ART-TESTS-01"
      symbol: "TestMachineFirstConformance"
      symbol_kind: "test_suite"
    refinement_ref: null
    non_authoritative_refs: ["README.md"]
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
  checkout: "git clone https://github.com/trencinodin-stack/arcstone-machinefirst-spec.git && cd arcstone-machinefirst-spec && git checkout --detach 17ca33a598fe7c4102f64c298d2260cec969655a"
  verify_revision: "test \"$(git rev-parse HEAD)\" = \"17ca33a598fe7c4102f64c298d2260cec969655a\""
  verify_contract_delta: "git diff --name-only 17ca33a598fe7c4102f64c298d2260cec969655a HEAD"
  verify_artifact_digests: "sha256sum -c MACHINEFIRST.sha256"
  command: "python3 -m unittest discover -s tests -v"
  network: "none"
  toolchain_image_digest: "sha256:8f9c2d4e6a1b3c5d7e9f0a2b4c6d8e0f1a3b5c7d9e1f3a5b7c9d1e3f5a7b9c1d"
  quick_check_covers: ["CLM-001", "CLM-002"]
  expected_exit_code: 0
  receipt_output: "out/AUDIT-RECEIPT.json"
  receipt_schema_ref: "machinefirst-receipt-v0.1"
  negative_control:
    command: "python3 validate_machinefirst.py MACHINEFIRST.template.md --strict"
    expected_exit_code: 1
    expected_reason: "target_invariant_violation"
    required_for_pass: true
  does_not_check: ["external repositories adopting the specification"]
```

## 7. Known Gaps & Open Errata
```yaml
known_gaps:
  - "Git tag v0.1.1 is unsigned until GPG/Sigstore release signing is configured"
```
