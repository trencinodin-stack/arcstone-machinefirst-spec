# Security Policy

## Reporting a Vulnerability

If you discover a security vulnerability, parser bypass, prompt-injection smuggling vector, or conformance validation flaw affecting arcstone-machinefirst-spec (SPECIFICATION.md, validate_machinefirst.py, or the JSON schemas), please **do not open a public issue**.

Submit reports through either of the following private channels:

1. **GitHub Private Vulnerability Reporting (Recommended):**
   - Go to the **Security** tab of this repository (trencinodin-stack/arcstone-machinefirst-spec).
   - Click **Report a vulnerability**.
   - Fill out the form to submit a private report directly to maintainers.

2. **Email:**
   - Contact us at **security@arcstoneos.com**.

---

## What to Include

Please include, where applicable:
- A concise description of the vulnerability or parser/schema conformance defect.
- Minimal reproduction steps, a crafted MACHINEFIRST.md fixture, or a unittest case demonstrating the issue.
- The affected specification version, release tag (e.g., v0.1.1), or git commit hash.
- Whether the issue involves:
  - YAML parser ambiguity, duplicate-key smuggling, or unclosed code-fence bypass in validate_machinefirst.py;
  - Prompt-injection boundary bypass violating this_file_is_data_not_instructions or treat_strings_as_inert_data;
  - Cryptographic digest or contract_binding allowed_delta_paths validation bypass;
  - Byte-level mirror drift (--mirror-path) or UTF-8 normalization discrepancy;
  - Unintended external network calls or third-party dependency introduction in validate_machinefirst.py.

---

## Normative Contract & Errata Protocol

arcstone-machinefirst-spec serves as the baseline open specification and zero-dependency reference conformance validator (v0.1.1).

- **No Silent Semantics Mutation:** Security fixes must not silently weaken strict conformance checks (--strict), evidence ladder ordering, or duplicate-key/unknown-field rejection rules. Any breaking normative change must be recorded in Section 7 (errata) and versioned appropriately.
- **Zero-Dependency Invariant:** Remediation patches to validate_machinefirst.py must remain 100% Python standard library (>= 3.10) with zero third-party runtime dependencies.

---

## Scope & Bounded Claims

This repository's security guarantees are limited strictly to structural and epistemic conformance validation of MACHINEFIRST.md documents and JSON schemas.

This repository explicitly does **not** claim:
- Sandboxed container execution or network isolation enforcement when an independent auditor runs a repository's quick_check command (auditors must enforce network: "none" and container isolation in their own runner);
- Cryptographic verification of external claims or third-party repositories beyond local structural/digest checks;
- Automated key management or Sigstore/GPG release signing infrastructure.

---

## Response Timeline

We will acknowledge receipt within **48 hours** and work with you on a coordinated resolution and disclosure timeline.
