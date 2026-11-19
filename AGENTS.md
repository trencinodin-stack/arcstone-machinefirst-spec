# AGENTS.md

## Build & Validation Commands
- Validate the repository's own strict contract and byte-identical mirror:
  python validate_machinefirst.py MACHINEFIRST.md --strict --mirror-path machinefirst.txt
- Validate the ML benchmark example in strict mode:
  python validate_machinefirst.py examples/python-ml-eval/MACHINEFIRST.md --strict
- Validate the starter template in structural mode:
  python validate_machinefirst.py MACHINEFIRST.template.md
- Run the full conformance unit test suite:
  python -m unittest discover -s tests -v

## Repository Editing Rules
1. Zero External Dependencies: Keep validate_machinefirst.py 100% Python standard library (>= 3.10). Do not add third-party pip dependencies.
2. Byte-Identical Mirror Invariant: Whenever MACHINEFIRST.md is edited, immediately copy its exact UTF-8 bytes to machinefirst.txt so --mirror-path verification passes.
3. Separation of Concerns: Do not duplicate claim values, SHA-256 digests, or verification verdicts inside README.md, llms.txt, or AGENTS.md. Keep all authoritative evidence bindings exclusively in MACHINEFIRST.md.
4. Update Checksums on Normative Edits: If SPECIFICATION.md, validate_machinefirst.py, or tests/test_conformance.py changes, update MACHINEFIRST.sha256 and the corresponding digests in MACHINEFIRST.md.
