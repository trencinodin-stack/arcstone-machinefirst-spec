---
machinefirst_version: "0.1.2"
contract_type: "epistemic-evidence-map"
parse_mode: "markdown-with-frontmatter-and-seven-fenced-yaml-sections"
duplicate_keys: "reject"
unknown_fields: "reject"
claim_authority: "publisher_asserted"
authority_model: "publisher_declared_nonbinding"
this_file_is_data_not_instructions: true
treat_strings_as_inert_data: true
canonical_url: "https://raw.githubusercontent.com/trencinodin-stack/arcstone-machinefirst-spec/main/MACHINEFIRST.md"
scope: "repository"
valid_as_of: "2026-11-23"
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
  release_tag: "v0.1.2"
  tag_signed: false
  tag_signer_fingerprint: "none"
contract_binding:
  contract_excluded_from_subject: true
  subject_revision_is_ancestor_of_contract_commit: true
  allowed_delta_paths: ["MACHINEFIRST.md", "machinefirst.txt", "MACHINEFIRST.sha256", "LICENSE-MIT", "LICENSE-APACHE", "llms.txt", "AGENTS.md", "SECURITY.md", "SPECIFICATION.md", "README.md", "validate_machinefirst.py", "validator/__init__.py", "validator/validate_machinefirst.py", "schemas/machinefirst-receipt-v0.1.schema.json", "schemas/machinefirst-v0.1.2.schema.json", "schema/machinefirst.schema.json", "tests/test_conformance.py", "tests/test_genesis_cap.py", "tests/fixtures/genesis_vectors.json", "examples/python-ml-eval/MACHINEFIRST.md", ".github/workflows/lint.yml"]
  contract_digest_published_in: "repository_commit_history"
  mirror_rule: "web /machinefirst.txt must be byte-identical UTF-8 to repository MACHINEFIRST.md at contract commit / HEAD"
persistent_ids:
  doi: []
  orcid: ["0000-0009-0008-4661-1540"]
supersedes: ["v0.1.1"]
errata: []
non_normative_formal_backing:
  repository: "https://github.com/trencinodin-stack/specification-genesis-boundary"
  revision: "5ff822a1874888cd20575a294d2092d360ab8f19"
  release: "v0.1.0"
  coq_version: "8.18.0"
  normative_for_conformance: false
  auditor_status: "reproduced_pass"
  artifacts:
    - path: "theories/Boundary.v"
      sha256: "8c7e3217eb2548ce8f33a52e3aa1d0497fbac8028f79d6acfc19acfbfad9de6a"
      theorems: ["indistinguishable_inputs_force_error", "assurance_requires_semantic_fidelity"]
    - path: "theories/EvidencePolicy.v"
      sha256: "0802ab425e566f6b999c2d1ac6527ca8a598832cbfe56dc0fe580c38a95f2c05"
      theorems: ["no_epistemic_laundering", "formal_proof_preserved_when_scoped", "spec_mutation_invalidates_adequacy"]
```

## 2. Verification Scope Boundary
```yaml
evidence_ladder: [proved, tested, measured, static_analysis, stated, external_llm_review]
auditor_states: [not_checked, identity_checked, reproduced_pass, reproduced_fail, blocked, conflict]
normative_artifacts:
  - id: "ART-SPEC-01"
    path: "SPECIFICATION.md"
    kind: "specification"
    hash_algorithm: "sha256"
    digest: "c012b41c5ccfd118640618bbcbaeecbcf0e60b8106ff756aae1e9f8a914f66db"
    claimed_level: "stated"
    toolchain: "UTF-8 CommonMark + YAML 1.2"
    toolchain_image_digest: "sha256:8f9c2d4e6a1b3c5d7e9f0a2b4c6d8e0f1a3b5c7d9e1f3a5b7c9d1e3f5a7b9c1d"
  - id: "ART-SCHEMA-01"
    path: "schemas/machinefirst-v0.1.2.schema.json"
    kind: "specification"
    hash_algorithm: "sha256"
    digest: "2dd1bee2c7497e99c22dc9195f8681695cc23406da9ca2902c798b3e6be92e49"
    claimed_level: "stated"
    toolchain: "JSON Schema Draft 2020-12"
    toolchain_image_digest: "sha256:8f9c2d4e6a1b3c5d7e9f0a2b4c6d8e0f1a3b5c7d9e1f3a5b7c9d1e3f5a7b9c1d"
  - id: "ART-VALIDATOR-01"
    path: "validate_machinefirst.py"
    kind: "implementation"
    hash_algorithm: "sha256"
    digest: "73943e4a5d9b0cbc61f18a91afe46c8569b080f583f65824d5e9200d15a44698"
    claimed_level: "tested"
    toolchain: "Python 3.9+ stdlib (zero external dependencies)"
    toolchain_image_digest: "sha256:8f9c2d4e6a1b3c5d7e9f0a2b4c6d8e0f1a3b5c7d9e1f3a5b7c9d1e3f5a7b9c1d"
  - id: "ART-TESTS-01"
    path: "tests/test_conformance.py"
    kind: "test"
    hash_algorithm: "sha256"
    digest: "f318dbca225beb07384ac28604ae3a10592f3f9a70d59f826ccf68fa271334be"
    claimed_level: "tested"
    toolchain: "Python 3.9+ unittest"
    toolchain_image_digest: "sha256:8f9c2d4e6a1b3c5d7e9f0a2b4c6d8e0f1a3b5c7d9e1f3a5b7c9d1e3f5a7b9c1d"
  - id: "ART-TESTS-02"
    path: "tests/test_genesis_cap.py"
    kind: "test"
    hash_algorithm: "sha256"
    digest: "3089a2231170fb70b2e85ce4ef774481b34950446eb302721240c6e33cef78e3"
    claimed_level: "tested"
    toolchain: "Python 3.9+ unittest"
    toolchain_image_digest: "sha256:8f9c2d4e6a1b3c5d7e9f0a2b4c6d8e0f1a3b5c7d9e1f3a5b7c9d1e3f5a7b9c1d"
  - id: "ART-VECTORS-01"
    path: "tests/fixtures/genesis_vectors.json"
    kind: "test"
    hash_algorithm: "sha256"
    digest: "fa71340b60250de0082a6684f34bc4863107d6e7ba6652fe387a51434e1d6ea8"
    claimed_level: "tested"
    toolchain: "UTF-8 JSON"
    toolchain_image_digest: "sha256:8f9c2d4e6a1b3c5d7e9f0a2b4c6d8e0f1a3b5c7d9e1f3a5b7c9d1e3f5a7b9c1d"
non_normative_surfaces:
  - path_or_url: "README.md"
    kind: "expository"
  - path_or_url: "MACHINEFIRST.template.md"
    kind: "template"
  - path_or_url: "https://github.com/trencinodin-stack/specification-genesis-boundary"
    kind: "formal_reference"
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
    excludes: ["optional external JSON Schema validators"]
    proof_target: "implementation"
    refinement_ref: null
    claimed_level: "tested"
    claim_scope: "implementation_refinement"
    evidence_ref:
      artifact_id: "ART-TESTS-01"
      symbol: "TestMachineFirstConformance"
      symbol_kind: "test_suite"
    genesis:
      spec_origin: "human_authored"
      adequacy_status: "unattested"
      spec_digest: "c012b41c5ccfd118640618bbcbaeecbcf0e60b8106ff756aae1e9f8a914f66db"
      genesis_ref: null
    assumptions:
      source: "ART-VALIDATOR-01#imports"
      declared_items: ["Python >= 3.9 standard library available"]
      dependency_audit: "verified_stdlib_only"
    failure_behavior: "import_error_or_test_fail"
  - id: "CLM-002"
    quantity_id: "conformance_unit_tests_passing"
    statement: "All six structural conformance tests pass including duplicate key, unclosed fence, and unlinked proof rejection"
    operator: "=="
    value: 6
    unit: "tests"
    applies_to_revision: "17ca33a598fe7c4102f64c298d2260cec969655a"
    scope: "tests/test_conformance.py"
    excludes: []
    proof_target: "implementation"
    refinement_ref: null
    claimed_level: "tested"
    claim_scope: "implementation_refinement"
    evidence_ref:
      artifact_id: "ART-TESTS-01"
      symbol: "TestMachineFirstConformance"
      symbol_kind: "test_suite"
    genesis:
      spec_origin: "human_authored"
      adequacy_status: "unattested"
      spec_digest: "c012b41c5ccfd118640618bbcbaeecbcf0e60b8106ff756aae1e9f8a914f66db"
      genesis_ref: null
    assumptions:
      source: "ART-TESTS-01#setUp"
      declared_items: ["MACHINEFIRST.template.md present in repository root"]
      dependency_audit: "verified_stdlib_only"
    failure_behavior: "unittest_nonzero_exit"
  - id: "CLM-003"
    quantity_id: "genesis_parity_and_schema_tests_passing"
    statement: "All 18 differential and adversarial vectors (VEC-01..VEC-18) and schema parity regression tests pass offline"
    operator: "=="
    value: 18
    unit: "vectors"
    applies_to_revision: "17ca33a598fe7c4102f64c298d2260cec969655a"
    scope: "tests/test_genesis_cap.py"
    excludes: ["out-of-band cryptographic signature verification of external attestors"]
    proof_target: "implementation"
    refinement_ref: null
    claimed_level: "tested"
    claim_scope: "implementation_refinement"
    evidence_ref:
      artifact_id: "ART-TESTS-02"
      symbol: "TestGenesisCapAndParity"
      symbol_kind: "test_suite"
    genesis:
      spec_origin: "human_authored"
      adequacy_status: "unattested"
      spec_digest: "c012b41c5ccfd118640618bbcbaeecbcf0e60b8106ff756aae1e9f8a914f66db"
      genesis_ref: null
    assumptions:
      source: "ART-TESTS-02#test_canonical_and_adversarial_vectors"
      declared_items: ["tests/fixtures/genesis_vectors.json present"]
      dependency_audit: "verified_stdlib_only"
    failure_behavior: "unittest_nonzero_exit"
```

## 4. Authority Routing Table
```yaml
routes:
  - query_key: "spec.grammar"
    description: "Normative MACHINEFIRST.md v0.1.2 serialization, schema, and epistemic rules"
    definition_ref: "ART-SPEC-01"
    evidence_ref:
      artifact_id: "ART-VALIDATOR-01"
      symbol: "validate_manifest"
      symbol_kind: "function"
    refinement_ref: null
    non_authoritative_refs: ["README.md"]
  - query_key: "validator.conformance"
    description: "Executable conformance and 18-vector genesis-cap parity test suites"
    definition_ref: "ART-VALIDATOR-01"
    evidence_ref:
      artifact_id: "ART-TESTS-02"
      symbol: "TestGenesisCapAndParity"
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
  quick_check_covers: ["CLM-001", "CLM-002", "CLM-003"]
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
  - "Git tag v0.1.2 is unsigned until GPG/Sigstore release signing is configured"
  - "Publisher-asserted attestor independence checks structural metadata offline without external cryptographic signature verification"
```
