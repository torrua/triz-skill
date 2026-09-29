# Security Policy & Agent Threat Model

## Supported Versions

| Version | Supported |
|---|---|
| `3.0.x` | ✅ Yes |
| `< 3.0.0` | ❌ No (upgrade to `v3.0.0+`) |

## Threat Model for AI Agent Skills

`triz-universal` is a prompt-and-reference skill package loaded into AI coding and reasoning agents (such as Google Antigravity, Claude Code, Cursor, and Codex CLI) that may have access to filesystem, shell execution, or external MCP tools.

### 1. Indirect Prompt Injection via Reference Files
- **Risk:** If an attacker modifies files inside `triz-universal/references/` or supplies an untrusted third-party reference module, hidden instructions could attempt to hijack the agent's tool execution.
- **Mitigation:**
  - `triz-universal` contains **only static Markdown documentation** in `triz-universal/`. It never instructs the agent to execute shell commands, fetch remote URLs, or exfiltrate environment variables during problem solving.
  - Use `python scripts/sync_deployment.py --mode check --destination <installed-path>` to verify SHA-256 byte-for-byte parity between the audited repository source and your installed skill directory.

### 2. Over-Privileged or Unlawful Resource Mobilization (VPR)
- **Risk:** In classical TRIZ, "use existing free resources" could be misinterpreted by an autonomous agent as permission to scrape private user telemetry, bypass authentication, or call paid external APIs without authorization.
- **Mitigation:**
  - Step 1 and Step 3 of `SKILL.md` enforce a strict **VPR Qualification Gate**: a resource qualifies only when it is available within the authorized system boundary, legally usable (GDPR/KYC/privacy compliant), and has a known incremental cost.
  - Regulated domains (`C-KYC-01` in `references/CLAIMS.md`) require an explicit legal/jurisdiction gate before implementation.

### 3. Hallucinated Safety or Compliance Guarantees
- **Risk:** An LLM might claim a proposed architecture is "verified" or "100% compliant".
- **Mitigation:**
  - Layer 2 outputs enforce mandatory `Evidence & Confidence` (`Established`, `Pattern`, `Hypothesis`), `Residual Risks`, and default `Status: UNVERIFIED` outcome labels unless empirical benchmark data was supplied by the user.

## Reporting a Vulnerability

If you discover a prompt-injection vector, unsafe instruction pattern, or script vulnerability in this repository:
1. Open a security advisory on GitHub (`Security` -> `Report a vulnerability`) or open an issue labeled `security` if non-exploitable.
2. Include the affected file, reproduction prompt, and observed agent behavior.
