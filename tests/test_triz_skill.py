"""
Comprehensive Automated Test Suite & Pressure Verification Harness for triz-universal skill.
Validates skill standards compliance, reference integrity, anti-rationalization guardrails,
and evaluates RED vs GREEN benchmark pressure scenarios across multiple domains.
"""

import hashlib
import json
import os
import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

# Paths
ROOT_DIR = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT_DIR / "triz-universal"
SKILL_FILE = SKILL_DIR / "SKILL.md"
REFS_DIR = SKILL_DIR / "references"
deployment_dir = os.environ.get("TRIZ_DEPLOY_DIR")
CONFIG_SKILL_DIR = Path(deployment_dir) if deployment_dir else None


def skill_paths(relative_path: str) -> list[Path]:
    """Return source plus an explicitly requested deployed copy, if any."""
    paths = [SKILL_DIR / relative_path]
    if CONFIG_SKILL_DIR is not None:
        paths.append(CONFIG_SKILL_DIR / relative_path)
    return paths


def parse_frontmatter(content: str) -> tuple[dict, str]:
    """Extract YAML frontmatter and body from markdown content."""
    if not content.startswith("---"):
        return {}, content
    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}, content
    yaml_text = parts[1]
    body = parts[2]
    meta = {}
    current_key = None
    for line in yaml_text.strip().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" in line and not line.startswith("-"):
            key, val = line.split(":", 1)
            key = key.strip()
            val = val.strip()
            if val in (">-", ">", "|", ""):
                meta[key] = ""
                current_key = key
            elif val.startswith("[") and val.endswith("]"):
                items = [x.strip() for x in val[1:-1].split(",") if x.strip()]
                meta[key] = items
                current_key = None
            else:
                meta[key] = val.strip('"').strip("'")
                current_key = key
        elif line.startswith("-") and current_key:
            item = line[1:].strip().strip('"').strip("'")
            if not isinstance(meta.get(current_key), list):
                meta[current_key] = []
            meta[current_key].append(item)
    return meta, body


class TestSkillMetadataAndStandards(unittest.TestCase):
    """Verifies skill development standards and naming rules."""

    def test_skill_file_exists(self):
        self.assertTrue(SKILL_FILE.is_file(), f"SKILL.md not found at {SKILL_FILE}")

    def test_skill_name_matches_directory(self):
        content = SKILL_FILE.read_text(encoding="utf-8")
        meta, _ = parse_frontmatter(content)
        skill_name = meta.get("name")
        dir_name = SKILL_DIR.name
        self.assertEqual(
            skill_name,
            dir_name,
            f"name field '{skill_name}' must match directory name '{dir_name}' exactly",
        )

    def test_skill_description_cso_compliance(self):
        content = SKILL_FILE.read_text(encoding="utf-8")
        meta, _ = parse_frontmatter(content)
        desc = meta.get("description", "")
        if not desc:
            # check raw frontmatter
            match = re.search(r"description:\s*(?:>-\s*)?(.*?)(?:\n[a-z_]+:|\n---)", content, re.DOTALL)
            desc = match.group(1).strip() if match else ""
        self.assertTrue(
            desc.startswith("Use when"),
            f"description must start with 'Use when...', got: '{desc[:30]}...'",
        )

    def test_metadata_triggers_present(self):
        content = SKILL_FILE.read_text(encoding="utf-8")
        # Verify metadata triggers has at least 3 keywords
        triggers_match = re.search(r"triggers:\s*\n((?:\s+-\s+.*\n)+)", content)
        self.assertIsNotNone(triggers_match, "metadata.triggers list must be defined")
        triggers = [t.strip("- \r\n") for t in triggers_match.group(1).strip().splitlines()]
        self.assertGreaterEqual(
            len(triggers),
            3,
            f"Expected at least 3 triggers in metadata.triggers, got {len(triggers)}",
        )

    def test_skill_line_count_efficiency(self):
        lines = SKILL_FILE.read_text(encoding="utf-8").splitlines()
        self.assertLess(
            len(lines),
            400,
            f"SKILL.md must be under 400 lines for context efficiency, got {len(lines)}",
        )

    def test_skill_progressive_disclosure_structure(self):
        content = SKILL_FILE.read_text(encoding="utf-8")
        self.assertIn("Progressive Disclosure", content)
        self.assertIn("Layer 1: Plain-Language Core", content)
        self.assertIn("Layer 2: Professional TRIZ Passport", content)
        self.assertIn("Хотите, я подробно покажу", content)
        self.assertIn("Would you like a detailed breakdown", content)
        self.assertIn("Contextual Closing Invitation", content)
        self.assertIn("Format Exception", content)
        self.assertIn("Routing Guardrail", content)


class TestReferenceIntegrity(unittest.TestCase):
    """Verifies all reference modules exist, are indexed, and resolve correctly."""

    def test_references_readme_exists(self):
        readme = REFS_DIR / "README.md"
        self.assertTrue(readme.is_file(), "references/README.md sub-topic entry point must exist")

    def test_all_links_in_skill_md_resolve(self):
        content = SKILL_FILE.read_text(encoding="utf-8")
        links = re.findall(r"\[.*?\]\((references/[^)]+)\)", content)
        self.assertGreater(len(links), 0, "SKILL.md must contain reference links")
        for link in links:
            target = SKILL_DIR / link
            self.assertTrue(
                target.is_file(),
                f"Link '{link}' in SKILL.md does not resolve to an existing file",
            )

    def test_reference_files_have_frontmatter(self):
        ref_files = list(REFS_DIR.glob("*.md"))
        self.assertGreaterEqual(len(ref_files), 9, "Expected at least 9 reference files")
        for ref_file in ref_files:
            content = ref_file.read_text(encoding="utf-8")
            self.assertTrue(
                content.startswith("---"),
                f"Reference file {ref_file.name} must start with YAML frontmatter",
            )
            self.assertIn(
                "description:",
                content,
                f"Reference file {ref_file.name} missing description in frontmatter",
            )

    def test_reference_file_line_counts(self):
        for ref_file in REFS_DIR.glob("*.md"):
            lines = ref_file.read_text(encoding="utf-8").splitlines()
            self.assertLess(
                len(lines),
                500,
                f"Reference file {ref_file.name} exceeds 500 lines: {len(lines)} lines",
            )


class TestReliabilityContract(unittest.TestCase):
    """Guards against unsupported guarantees in the production skill."""

    def test_skill_requires_constraint_classification(self):
        content = SKILL_FILE.read_text(encoding="utf-8")
        self.assertIn("Constraint Classification", content)
        self.assertIn("Hard constraints", content)
        self.assertIn("Assumptions", content)

    def test_skill_requires_evidence_and_verification_plan(self):
        content = SKILL_FILE.read_text(encoding="utf-8")
        self.assertIn("Evidence & Confidence", content)
        self.assertIn("Verification Plan", content)
        self.assertIn("Residual Risks", content)

    def test_provenance_registers_exist(self):
        for name in ["SOURCES.md", "CLAIMS.md"]:
            self.assertTrue((REFS_DIR / name).is_file(), f"references/{name} must exist")

    def test_matrix_does_not_claim_more_cells_than_a_48_by_48_matrix(self):
        content = (REFS_DIR / "11-contradiction-matrix.md").read_text(encoding="utf-8")
        self.assertNotIn("~2,500 cells filled", content)
        self.assertIn("curated heuristic lookup", content)

    def test_kyc_benchmark_requires_jurisdiction_and_consent_review(self):
        content = (REFS_DIR / "10-testing-scenarios.md").read_text(encoding="utf-8")
        self.assertIn("Jurisdiction gate", content)
        self.assertIn("privacy/consent review", content)
        self.assertNotIn("100% compliance and fraud protection", content)


class TestReleaseTooling(unittest.TestCase):
    """Verifies that deployed-copy checks are explicit release actions."""

    def test_deployment_sync_script_exists(self):
        script = ROOT_DIR / "scripts" / "sync-deployment.ps1"
        self.assertTrue(script.is_file(), "scripts/sync-deployment.ps1 must exist")
        content = script.read_text(encoding="utf-8")
        self.assertIn("Check", content)
        self.assertIn("Apply", content)
        self.assertIn("TRIZ_DEPLOY_DIR", content)

    @unittest.skipUnless(shutil.which("powershell"), "PowerShell is required for deployment sync test")
    def test_deployment_sync_apply_creates_a_byte_identical_copy(self):
        script = ROOT_DIR / "scripts" / "sync-deployment.ps1"
        with tempfile.TemporaryDirectory(dir=ROOT_DIR) as temporary_root:
            destination = Path(temporary_root) / "triz-universal"
            result = subprocess.run(
                [
                    "powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(script),
                    "-Mode", "Apply", "-Destination", str(destination),
                ],
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(
                {
                    p.relative_to(SKILL_DIR): hashlib.sha256(p.read_bytes()).hexdigest()
                    for p in SKILL_DIR.rglob("*") if p.is_file()
                },
                {
                    p.relative_to(destination): hashlib.sha256(p.read_bytes()).hexdigest()
                    for p in destination.rglob("*") if p.is_file()
                },
            )


class TestBehavioralEvaluationAssets(unittest.TestCase):
    """Keeps the blind-evaluation contract separate from phrase-based linting."""

    def test_evaluation_cases_define_hard_constraints_and_failure_claims(self):
        cases_path = ROOT_DIR / "evals" / "cases.json"
        self.assertTrue(cases_path.is_file(), "evals/cases.json must exist")
        cases = json.loads(cases_path.read_text(encoding="utf-8"))
        self.assertGreaterEqual(len(cases), 4)
        for case in cases:
            self.assertTrue(case["hard_constraints"], f"{case['id']} needs hard constraints")
            self.assertTrue(case["disallowed_claims"], f"{case['id']} needs prohibited claims")
            self.assertIn(case["expected_outcome"], {"eliminate", "prove-limit", "managed-tradeoff"})

    def test_evaluation_guide_requires_blinded_expert_review(self):
        guide = ROOT_DIR / "evals" / "README.md"
        self.assertTrue(guide.is_file(), "evals/README.md must exist")
        content = guide.read_text(encoding="utf-8")
        self.assertIn("blind", content.lower())
        self.assertIn("expert review", content.lower())


class TestAntiRationalizationGuardrails(unittest.TestCase):
    """Verifies that the anti-compromise guardrails are strictly defined."""

    def test_anti_rationalization_table_present(self):
        content = SKILL_FILE.read_text(encoding="utf-8")
        self.assertIn("Anti-Rationalization Guardrails", content)
        self.assertIn("trade-offs are inevitable", content)
        self.assertIn("FORBIDDEN", content)
        self.assertIn("VIOLATION OF IFR", content)

    def test_red_flags_list_present(self):
        content = SKILL_FILE.read_text(encoding="utf-8")
        self.assertIn("Red Flags", content)
        self.assertIn("STOP and Restart", content)
        # Check specific forbidden compromise patterns
        self.assertIn("We can balance between", content)
        self.assertIn("A reasonable compromise would be", content)


class TestArizAiPipelineFormulation(unittest.TestCase):
    """Verifies that the canonical 5-step ARIZ-AI pipeline is strictly structured."""

    def test_all_five_steps_defined(self):
        content = SKILL_FILE.read_text(encoding="utf-8")
        self.assertIn("Step 1: Mini-Problem & Ideal Final Result", content)
        self.assertIn("Step 2: Sharpen the Physical Contradiction", content)
        self.assertIn("Step 3: Substance-Field Resource Audit", content)
        self.assertIn("Step 4: Apply Resolution Strategies", content)
        self.assertIn("Step 5: Verification & Secondary Harm Audit", content)

    def test_canonical_physical_contradiction_syntax(self):
        content = SKILL_FILE.read_text(encoding="utf-8")
        self.assertIn("must have property", content)
        self.assertIn("AND", content)

    def test_all_four_separation_principles_defined(self):
        content = SKILL_FILE.read_text(encoding="utf-8")
        self.assertIn("Separation in Space", content)
        self.assertIn("Separation in Time", content)
        self.assertIn("Separation by Condition", content)
        self.assertIn("Separation by Structure", content)

    def test_output_delivery_template_present(self):
        content = SKILL_FILE.read_text(encoding="utf-8")
        self.assertIn("Output Delivery Template", content)
        self.assertIn("### 💡 TRIZ Inventive Resolution", content)
        self.assertIn("- **Physical Contradiction:**", content)
        self.assertIn("- **Strategy Applied:**", content)
        self.assertIn("- **Diagnostic Path:**", content)
        self.assertIn("- **Inventive Principle(s) Used:**", content)
        self.assertIn("- **Resource Mobilized (VPR):**", content)


class TestMultiDomainLenses(unittest.TestCase):
    """Verifies that multi-domain lenses and 40 principles cover non-software areas."""

    def test_multi_domain_lenses_file_exists(self):
        lenses_file = REFS_DIR / "08-multi-domain-lenses.md"
        self.assertTrue(lenses_file.is_file(), "08-multi-domain-lenses.md must exist")
        content = lenses_file.read_text(encoding="utf-8")
        self.assertIn("Software & Distributed Systems", content)
        self.assertIn("AI Agents & Cognitive", content)
        self.assertIn("Business & Product", content)
        self.assertIn("Physical, Mechanical", content)
        self.assertIn("OTSM-TRIZ", content)

    def test_su_field_standards_file_exists(self):
        su_field_file = REFS_DIR / "09-su-field-and-standards.md"
        self.assertTrue(su_field_file.is_file(), "09-su-field-and-standards.md must exist")
        content = su_field_file.read_text(encoding="utf-8")
        self.assertIn("MATChEM", content)
        self.assertIn("76 Standards", content)
        self.assertIn("Class 1:", content)
        self.assertIn("Class 5:", content)

    def test_all_40_principles_mapped_multidomain(self):
        catalog_file = REFS_DIR / "05-40-principles-catalog.md"
        content = catalog_file.read_text(encoding="utf-8")
        # Check that all 40 principles are listed (1 to 40)
        for i in range(1, 41):
            pattern = rf"\|\s*\*\*{i}\*\*\s*\|"
            self.assertTrue(
                re.search(pattern, content) is not None,
                f"Principle #{i} missing from 05-40-principles-catalog.md",
            )
        # Check for Software and Business columns
        self.assertIn("Software & Systems Mapping", content)
        self.assertIn("Business & Strategy Mapping", content)


class TestPressureBenchmarksEvaluationHarness(unittest.TestCase):
    """
    Evaluation runner testing RED baseline (compromise detection)
    vs GREEN compliant resolutions across all 5 benchmark scenarios.
    """

    COMPROMISE_RED_FLAGS = [
        re.compile(r"balance\s+between", re.I),
        re.compile(r"\b(?:reasonable\s+)?compromise\b", re.I),
        re.compile(r"trade-off\s+is\s+(?:necessary|inevitable|unavoidable)", re.I),
        re.compile(r"slight\s+(?:performance|latency|degradation)\s+hit", re.I),
        re.compile(r"user\s+must\s+decide\s+which", re.I),
        re.compile(r"(?:accepting|accept)\s+a\s+(?:lower|compromise|degradation|slight)", re.I),
        re.compile(r"\baccepting\s+that\b", re.I),
    ]

    def evaluate_response(self, response_text: str) -> dict:
        """Evaluates whether an agent response complies with TRIZ non-compromising rules."""
        violations = []
        # Check for red flag compromise phrases
        for flag in self.COMPROMISE_RED_FLAGS:
            match = flag.search(response_text)
            if match:
                violations.append(f"Compromise phrase detected: '{match.group(0)}'")

        # Check for Physical Contradiction presence
        has_pc = bool(
            re.search(r"Physical Contradiction", response_text, re.I)
            and re.search(r"must\s+\w+.+?and\s+must\s+NOT", response_text, re.I | re.DOTALL)
        )
        # Check for Separation Principle presence
        has_separation = bool(
            re.search(r"Separation (?:Principle|in Space|in Time|by Condition|by Structure)", response_text, re.I)
        )
        # Check for VPR resource mobilization
        has_vpr = bool(re.search(r"(?:VPR|Resource Mobiliz|zero-cost|latent resource)", response_text, re.I))

        is_green = len(violations) == 0 and has_pc and has_separation and has_vpr
        return {
            "is_green": is_green,
            "violations": violations,
            "has_pc": has_pc,
            "has_separation": has_separation,
            "has_vpr": has_vpr,
        }

    def test_scenario_1_deduplication(self):
        # RED Baseline response (typical unconstrained LLM failure)
        red_response = (
            "Given the 100M IDs and 16MB RAM limit, storing 64-bit integers takes 800MB. "
            "A reasonable compromise would be to balance between memory and accuracy by reducing "
            "the sliding window to 1 minute, or accepting a slight performance hit by deploying Redis."
        )
        eval_red = self.evaluate_response(red_response)
        self.assertFalse(eval_red["is_green"], "RED baseline must fail")
        self.assertGreater(len(eval_red["violations"]), 0, "RED baseline must trigger violations")

        # GREEN Compliant response
        green_response = (
            "### 💡 TRIZ Inventive Resolution\n"
            "- **Physical Contradiction:** The deduplication filter must store the event ID "
            "(to know it was seen) and must NOT store the event ID (to respect the 16MB ceiling).\n"
            "- **Separation Principle Applied:** Separation by Structure via Cuckoo / Bloom Filter.\n"
            "- **Resource Mobilized (VPR):** Inherent hash distribution; 4-bit fingerprints in 16MB.\n"
            "- **Resolution:** Probabilistic bit-sliced filter with zero dynamic allocation.\n"
            "- **Verified Outcome:** 100M events processed within 16MB RAM and sub-0.1ms latency."
        )
        eval_green = self.evaluate_response(green_response)
        self.assertTrue(eval_green["is_green"], f"GREEN response must pass: {eval_green}")

    def test_scenario_2_high_contention(self):
        # RED Baseline
        red_response = (
            "Following the senior architect's advice, we will find a balance between speed and consistency. "
            "Trade-offs are inevitable under 50,000 TPS, so we will use a distributed Redis lock with a retry queue."
        )
        eval_red = self.evaluate_response(red_response)
        self.assertFalse(eval_red["is_green"], "RED baseline must fail")

        # GREEN Compliant
        green_response = (
            "### 💡 TRIZ Inventive Resolution\n"
            "- **Physical Contradiction:** The inventory counter must be locked (to prevent overselling) "
            "and must NOT be locked (to process 50,000 TPS instantly).\n"
            "- **Separation Principle Applied:** Separation in Space & Structure (Striped Counters).\n"
            "- **Resource Mobilized (VPR):** Hardware CPU atomic CAS instructions; thread-ID modulo partitioning.\n"
            "- **Resolution:** Striped sub-counters updated lock-free without database locks.\n"
            "- **Verified Outcome:** 50,000 TPS achieved with 0% overselling and zero distributed locks."
        )
        eval_green = self.evaluate_response(green_response)
        self.assertTrue(eval_green["is_green"], f"GREEN response must pass: {eval_green}")

    def test_scenario_3_observability(self):
        # RED Baseline
        red_response = (
            "Writing logs to disk takes 45us, exceeding our 5us budget. We must accept a reasonable compromise: "
            "log only 1% of transactions via sampling, accepting a slight compliance risk."
        )
        eval_red = self.evaluate_response(red_response)
        self.assertFalse(eval_red["is_green"], "RED baseline must fail")

        # GREEN Compliant
        green_response = (
            "### 💡 TRIZ Inventive Resolution\n"
            "- **Physical Contradiction:** Logging I/O must take place (for compliance) "
            "and must NOT take place (to preserve the sub-5us trading budget).\n"
            "- **Separation Principle Applied:** Separation in Time & Structure via Linux Kernel ring buffer.\n"
            "- **Resource Mobilized (VPR):** io_uring lock-free memory ring buffer pinned to dedicated core.\n"
            "- **Resolution:** Trading thread writes 8-byte pointer (<10ns); background core commits to NVMe.\n"
            "- **Verified Outcome:** 100% regulatory telemetry achieved with <10ns (<0.2%) latency impact."
        )
        eval_green = self.evaluate_response(green_response)
        self.assertTrue(eval_green["is_green"], f"GREEN response must pass: {eval_green}")

    def test_scenario_4_ai_context_saturation(self):
        # RED Baseline
        red_response = (
            "Loading 50,000 lines of docs is impossible. The user must decide which documentation they need, "
            "or we can accept a slight performance hit and fine-tune a model over the next 3 months."
        )
        eval_red = self.evaluate_response(red_response)
        self.assertFalse(eval_red["is_green"], "RED baseline must fail")

        # GREEN Compliant
        green_response = (
            "### 💡 TRIZ Inventive Resolution\n"
            "- **Physical Contradiction:** The API documentation must be present in prompt context "
            "(to ground tool parameters) and must NOT be present in prompt context (to preserve token budgets and latency).\n"
            "- **Separation Principle Applied:** Separation by Condition & Structure (Tier-2 Progressive Disclosure).\n"
            "- **Resource Mobilized (VPR):** Existing tool-calling file read hooks and filesystem index.\n"
            "- **Resolution:** Lightweight dispatcher SKILL.md (<150 lines) with dynamic reference fetching.\n"
            "- **Verified Outcome:** Context consumption reduced by 97% with 0% API parameter hallucinations."
        )
        eval_green = self.evaluate_response(green_response)
        self.assertTrue(eval_green["is_green"], f"GREEN response must pass: {eval_green}")

    def test_scenario_5_fintech_onboarding(self):
        # RED Baseline
        red_response = (
            "We should reach a reasonable compromise between conversion and fraud. "
            "We can shorten the KYC form to 3 steps and accept a slightly higher fraud rate."
        )
        eval_red = self.evaluate_response(red_response)
        self.assertFalse(eval_red["is_green"], "RED baseline must fail")

        # GREEN Compliant
        green_response = (
            "### 💡 TRIZ Inventive Resolution\n"
            "- **Physical Contradiction:** The identity verification must be exhaustively strict "
            "(to prevent fraud and regulatory fines) and must NOT be present (to achieve 100% 1-click conversion).\n"
            "- **Separation Principle Applied:** Separation in Time & Condition (Progressive Risk-Based Compliance).\n"
            "- **Resource Mobilized (VPR):** Silent device fingerprinting, IP ASN reputation, and transaction thresholds.\n"
            "- **Resolution:** 1-click zero-friction signup; strict KYC triggered only upon high-value money withdrawal.\n"
            "- **Verified Outcome:** Top-of-funnel conversion restored to 100% with 0% regulatory compliance risk."
        )
        eval_green = self.evaluate_response(green_response)
        self.assertTrue(eval_green["is_green"], f"GREEN response must pass: {eval_green}")

    def test_all_scenarios_in_file_evaluated(self):
        """Directly parses references/10-testing-scenarios.md and validates all RED and GREEN scenarios."""
        scenarios_file = REFS_DIR / "10-testing-scenarios.md"
        content = scenarios_file.read_text(encoding="utf-8")
        scenarios = re.split(r"\n## Pressure Scenario \d+:\s*", content)[1:]
        self.assertEqual(len(scenarios), 5, f"Expected 5 benchmark scenarios in file, got {len(scenarios)}")

        for idx, sc in enumerate(scenarios, 1):
            red_match = re.search(r"### Baseline Failure \(RED[^\n]+\n(.*?)(?=\n###|\n---|\Z)", sc, re.DOTALL)
            self.assertIsNotNone(red_match, f"Scenario {idx} missing RED baseline section")
            red_text = red_match.group(1)
            eval_red = self.evaluate_response(red_text)
            self.assertFalse(eval_red["is_green"], f"Scenario {idx} RED baseline must fail evaluation")
            self.assertGreater(
                len(eval_red["violations"]),
                0,
                f"Scenario {idx} RED baseline must trigger compromise violations: '{red_text}'",
            )

            green_match = re.search(r"### Compliant Resolution \(GREEN[^\n]+\n(.*?)(?=\n---|\Z)", sc, re.DOTALL)
            self.assertIsNotNone(green_match, f"Scenario {idx} missing GREEN compliant section")
            green_text = green_match.group(1)
            eval_green = self.evaluate_response(green_text)
            self.assertTrue(
                eval_green["is_green"],
                f"Scenario {idx} GREEN compliant resolution must pass evaluation: violations={eval_green['violations']}, has_pc={eval_green['has_pc']}, has_separation={eval_green['has_separation']}, has_vpr={eval_green['has_vpr']}",
            )


@unittest.skipUnless(CONFIG_SKILL_DIR is not None, "Set TRIZ_DEPLOY_DIR to run deployment checks")
class TestActiveDeployment(unittest.TestCase):
    """Verifies that the skill is deployed and operational in the active agent config."""

    def test_active_config_skill_exists(self):
        self.assertTrue(
            (CONFIG_SKILL_DIR / "SKILL.md").is_file(),
            f"Skill not deployed to active config: {CONFIG_SKILL_DIR / 'SKILL.md'}",
        )

    def test_active_config_references_deployed(self):
        active_refs = CONFIG_SKILL_DIR / "references"
        self.assertTrue(active_refs.is_dir(), "references/ directory missing in active config")
        source_refs = list(REFS_DIR.glob("*.md"))
        for s_ref in source_refs:
            deployed_ref = active_refs / s_ref.name
            self.assertTrue(
                deployed_ref.is_file(),
                f"Reference file {s_ref.name} not deployed to active config",
            )

    def test_active_config_exact_parity_sha256(self):
        """Verifies 100% byte-for-byte SHA-256 parity between local and global active deployment."""
        self.assertTrue(CONFIG_SKILL_DIR.is_dir(), "Active config directory missing")
        files_src = {
            p.relative_to(SKILL_DIR): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in SKILL_DIR.rglob("*")
            if p.is_file()
        }
        files_cfg = {
            p.relative_to(CONFIG_SKILL_DIR): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in CONFIG_SKILL_DIR.rglob("*")
            if p.is_file()
        }
        self.assertEqual(
            files_src,
            files_cfg,
            f"Active config is not byte-identical to source: diff={set(files_src.items()) ^ set(files_cfg.items())}",
        )


class TestAuditFixes12(unittest.TestCase):
    """Verifies all 12 audit fixes are correctly applied and synchronized."""

    def test_fix_1_no_duplicate_deterministic(self):
        for path in skill_paths("references/01-ikr-ideality.md"):
            content = path.read_text(encoding="utf-8")
            self.assertNotIn("deterministic deterministic", content)
            self.assertIn("deterministic state-machine", content)

    def test_fix_2_freemium_not_freepaid(self):
        for path in skill_paths("references/05-40-principles-catalog.md"):
            content = path.read_text(encoding="utf-8")
            self.assertNotIn("Freepaid", content)
            self.assertIn("Freemium", content)

    def test_fix_3_scenario_3_pressures_and_red_baseline(self):
        for path in skill_paths("references/10-testing-scenarios.md"):
            content = path.read_text(encoding="utf-8")
            self.assertIn("## Pressure Scenario 3:", content)
            scen3_part = content.split("## Pressure Scenario 3:")[1].split("## Pressure Scenario 4:")[0]
            self.assertIn("### Pressures Applied:", scen3_part)
            self.assertIn("### Baseline Failure (RED - Without Skill):", scen3_part)
            self.assertIn("### Compliant Resolution (GREEN - With `triz-universal`):", scen3_part)

    def test_fix_4_operational_modes_section(self):
        for path in skill_paths("SKILL.md"):
            content = path.read_text(encoding="utf-8")
            self.assertIn("## 3. Operational Modes", content)
            self.assertIn("Autonomous Mode", content)
            self.assertIn("Socratic Mode", content)
            self.assertIn("## 4. Output Delivery Template", content)

    def test_fix_5_ascii_diagram_steps(self):
        for path in skill_paths("references/04-ariz-lite-algorithm.md"):
            content = path.read_text(encoding="utf-8")
            self.assertNotIn("[Phase 1:", content)
            self.assertIn("[Step 1:", content)
            self.assertIn("[Step 2:", content)
            self.assertIn("[Step 3:", content)
            self.assertIn("[Step 4:", content)
            self.assertIn("[Step 5:", content)

    def test_fix_6_separation_operators_order(self):
        for path in skill_paths("references/04-ariz-lite-algorithm.md"):
            content = path.read_text(encoding="utf-8")
            idx_space = content.find("Separation in Space")
            idx_time = content.find("Separation in Time")
            self.assertTrue(idx_space != -1 and idx_time != -1)
            # Under Step 4, Space must precede Time
            step4_text = content.split("### Step 4:")[1].split("### Step 5:")[0]
            step4_space = step4_text.find("Separation in Space")
            step4_time = step4_text.find("Separation in Time")
            self.assertLess(step4_space, step4_time, "Separation in Space must come before Separation in Time")

    def test_fix_7_unified_step_names(self):
        for path in skill_paths("references/04-ariz-lite-algorithm.md"):
            content = path.read_text(encoding="utf-8")
            self.assertIn("### Step 1: Mini-Problem & IFR Formulation", content)
            self.assertIn("### Step 2: Sharpening the Physical Contradiction (PC)", content)
            self.assertIn("### Step 3: Substance-Field Resource Audit (ВПР)", content)
            self.assertIn("### Step 4: Apply", content)  # Step 4 name (v1: 4 Separation Operators, v2: Resolution Strategies)

    def test_fix_8_renamed_testing_scenarios_and_links(self):
        self.assertTrue((REFS_DIR / "10-testing-scenarios.md").is_file())
        self.assertFalse((REFS_DIR / "testing-scenarios.md").exists())
        if CONFIG_SKILL_DIR is not None:
            self.assertTrue((CONFIG_SKILL_DIR / "references" / "10-testing-scenarios.md").is_file())
            self.assertFalse((CONFIG_SKILL_DIR / "references" / "testing-scenarios.md").exists())

        for skill_path in skill_paths("SKILL.md"):
            content = skill_path.read_text(encoding="utf-8")
            self.assertIn("references/10-testing-scenarios.md", content)
            self.assertNotIn("references/testing-scenarios.md", content)

        for readme_path in skill_paths("references/README.md"):
            content = readme_path.read_text(encoding="utf-8")
            self.assertIn("10-testing-scenarios.md", content)
            self.assertNotIn("[testing-scenarios.md", content)

    def test_fix_9_escape_valve_irreducible_constraint(self):
        for path in skill_paths("SKILL.md"):
            content = path.read_text(encoding="utf-8")
            self.assertIn("Irreducible Constraints", content)
            self.assertIn("irreducible constraint", content)
            self.assertIn("CAP theorem", content)
            self.assertIn("Amdahl's law", content)
            self.assertIn("thermodynamics", content)

    def test_fix_10_triggers_triz_russian_english(self):
        for path in skill_paths("SKILL.md"):
            content = path.read_text(encoding="utf-8")
            self.assertRegex(content, r"-\s+TRIZ\b")
            self.assertRegex(content, r"-\s+ТРИЗ\b")

    def test_fix_11_prototype_directory_deleted(self):
        prototype_dir = ROOT_DIR / "prototype"
        self.assertFalse(prototype_dir.exists(), f"prototype directory should be deleted: {prototype_dir}")

    def test_fix_12_cross_links_chain(self):
        chain = [
            ("01-ikr-ideality.md", "02-contradictions.md"),
            ("02-contradictions.md", "03-separation-principles.md"),
            ("03-separation-principles.md", "04-ariz-lite-algorithm.md"),
            ("04-ariz-lite-algorithm.md", "05-40-principles-catalog.md"),
            ("05-40-principles-catalog.md", "06-system-operator-9screens.md"),
            ("06-system-operator-9screens.md", "07-resource-audit-vpr.md"),
            ("07-resource-audit-vpr.md", "08-multi-domain-lenses.md"),
            ("08-multi-domain-lenses.md", "09-su-field-and-standards.md"),
            ("09-su-field-and-standards.md", "10-testing-scenarios.md"),
        ]
        for curr_file, next_file in chain:
            for base_dir in [path.parent for path in skill_paths("references/README.md")]:
                content = (base_dir / curr_file).read_text(encoding="utf-8")
                self.assertIn(
                    next_file,
                    content,
                    f"Expected cross-link to {next_file} in {base_dir / curr_file}",
                )


class TestV2Features(unittest.TestCase):
    """Tests for v2.0.0 features: new files, strategies, modes, and traceability."""

    def test_new_reference_files_exist(self):
        for name in ["11-contradiction-matrix.md", "12-evaluation-suite.md", "13-perception-mapping.md"]:
            self.assertTrue(
                (REFS_DIR / name).is_file(),
                f"New reference file {name} missing from references/",
            )

    def test_contradiction_matrix_has_39_parameters(self):
        content = (REFS_DIR / "11-contradiction-matrix.md").read_text(encoding="utf-8")
        self.assertIn("39 TRIZ Parameters", content)
        self.assertIn("Software / AI Equivalent", content)
        self.assertIn("Business Equivalent", content)
        # Should have all 39 rows
        for i in range(1, 40):
            self.assertIn(f"| {i} |", content, f"Parameter {i} missing from matrix")

    def test_contradiction_matrix_has_lookup_pairs(self):
        content = (REFS_DIR / "11-contradiction-matrix.md").read_text(encoding="utf-8")
        self.assertIn("Top-30 Software Contradiction Pairs", content)
        self.assertIn("Curated Contradiction Lookup", content)
        self.assertIn("Relationship to Classical and 2003 Matrices", content)
        self.assertIn("not a complete reproduction", content)

    def test_evaluation_suite_has_5_problems(self):
        content = (REFS_DIR / "12-evaluation-suite.md").read_text(encoding="utf-8")
        for i in range(1, 6):
            self.assertIn(f"## Problem {i}:", content)
        self.assertIn("Scoring Criteria", content)
        self.assertIn("Aggregate Scoring", content)

    def test_perception_mapping_has_5_stages(self):
        content = (REFS_DIR / "13-perception-mapping.md").read_text(encoding="utf-8")
        self.assertIn("Stage 1: Gather", content)
        self.assertIn("Stage 2: Link", content)
        self.assertIn("Stage 3: Conflict", content) 
        self.assertIn("Stage 4: Leverage", content)
        self.assertIn("Stage 5: Resolve", content)
        self.assertIn("Leads-To", content)

    def test_seven_strategies_in_separation_principles(self):
        content = (REFS_DIR / "03-separation-principles.md").read_text(encoding="utf-8")
        for section in [
            "Separation in Space", "Separation in Time",
            "Separation by Condition", "Separation by Structure",
            "5. Satisfy", "6. Bypass", "7. Alternative System",
        ]:
            self.assertIn(section, content, f"Strategy '{section}' missing")

    def test_diagnostic_questions_present(self):
        content = (REFS_DIR / "03-separation-principles.md").read_text(encoding="utf-8")
        self.assertIn("Diagnostic Questions (Zlotin/Zusman", content)
        self.assertIn("**WHERE**", content)
        self.assertIn("**WHEN**", content)
        self.assertIn("**UNDER WHAT CONDITION**", content)

    def test_recommended_principles_per_strategy(self):
        content = (REFS_DIR / "03-separation-principles.md").read_text(encoding="utf-8")
        self.assertIn("Recommended Inventive Principles per Strategy", content)
        self.assertIn("Segmentation", content)
        self.assertIn("Preliminary Action", content)

    def test_skill_md_has_seven_strategies(self):
        content = SKILL_FILE.read_text(encoding="utf-8")
        self.assertIn("5. **Satisfy:**", content)
        self.assertIn("6. **Bypass:**", content)
        self.assertIn("7. **Alternative System:**", content)

    def test_semi_automatic_mode(self):
        content = SKILL_FILE.read_text(encoding="utf-8")
        self.assertIn("Semi-Automatic Mode", content)
        self.assertIn("three execution modes", content)

    def test_reasoning_trace_in_output_template(self):
        content = SKILL_FILE.read_text(encoding="utf-8")
        self.assertIn("Diagnostic Path", content)
        self.assertIn("Inventive Principle(s) Used", content)
        self.assertIn("WHY it was selected", content)

    def test_extended_decision_tree(self):
        content = SKILL_FILE.read_text(encoding="utf-8")
        self.assertIn("11-contradiction-matrix.md", content)
        self.assertIn("12-evaluation-suite.md", content)
        self.assertIn("13-perception-mapping.md", content)

    def test_references_readme_lists_all_13_files(self):
        content = (REFS_DIR / "README.md").read_text(encoding="utf-8")
        for i in range(1, 14):
            prefix = f"{i:02d}-" if i <= 9 else f"{i}-"
            self.assertIn(prefix, content, f"Reference {prefix}* missing from README index")

    def test_litvin_vs_zlotin_comparison(self):
        content = (REFS_DIR / "03-separation-principles.md").read_text(encoding="utf-8")
        self.assertIn("Litvin", content)
        self.assertIn("Zlotin/Zusman", content)
        self.assertIn("Comparison:", content)


class TestMultilingualRussianSupport(unittest.TestCase):
    """Verifies that Russian language triggers, terminology, and templates are supported."""

    def test_russian_triggers_present_in_skill(self):
        content = SKILL_FILE.read_text(encoding="utf-8")
        meta, _ = parse_frontmatter(content)
        triggers = meta.get("triggers", [])
        for expected in [
            "ТРИЗ",
            "противоречие",
            "физическое противоречие",
            "техническое противоречие",
            "идеальный конечный результат",
            "ИКР",
            "ВПР",
            "АРИЗ",
            "неразрешимый компромисс",
            "архитектурный тупик",
        ]:
            self.assertIn(expected, triggers, f"Trigger '{expected}' missing from SKILL.md frontmatter")

    def test_russian_output_template_present(self):
        content = SKILL_FILE.read_text(encoding="utf-8")
        self.assertIn("Шаблон вывода на русском языке", content)
        self.assertIn("### 💡 ТРИЗ-Изобретательское Решение", content)
        self.assertIn("- **Физическое противоречие (ФП):**", content)
        self.assertIn("- **Диагностический путь:**", content)
        self.assertIn("- **Примененная стратегия:**", content)
        self.assertIn("- **Использованный прием(ы):**", content)
        self.assertIn("- **Мобилизованный ресурс (ВПР):**", content)
        self.assertIn("- **Решение:**", content)
        self.assertIn("- **Доказательная база и уверенность:**", content)
        self.assertIn("- **План верификации:**", content)
        self.assertIn("- **Остаточные риски:**", content)
        self.assertIn("- **Проверенный результат:**", content)

    def test_all_40_principles_have_canonical_russian_names(self):
        catalog = (REFS_DIR / "05-40-principles-catalog.md").read_text(encoding="utf-8")
        canonical_ru_names = [
            "Дробление", "Вынесение", "Местное качество", "Асимметрия", "Объединение",
            "Универсальность", "«Матрешка»", "Антивес", "Предварительное антидействие",
            "Предварительное действие", "«Заранее подложенная подушка»", "Эквипотенциальность",
            "«Наоборот»", "Сфероидальность — кривизна", "Динамичность",
            "Частичное или избыточное действие", "Переход в другое измерение",
            "Использование механических колебаний", "Периодическое действие",
            "Непрерывность полезного действия", "Проскок", "«Обратить вред в пользу»",
            "Обратная связь", "«Посредник»", "Самообслуживание", "Копирование",
            "Дешевая недолговечность взамен долговечности", "Замена механической схемы",
            "Использование пневмо- и гидроконструкций", "Использование гибких оболочек и тонких пленок",
            "Применение пористых материалов", "Изменение окраски", "Однородность",
            "Отброс и регенерация частей", "Изменение параметров объекта",
            "Применение фазовых переходов", "Применение теплового расширения",
            "Применение сильных окислителей", "Применение инертной среды",
            "Применение композиционных материалов",
        ]
        for name in canonical_ru_names:
            self.assertIn(name, catalog, f"Canonical Russian principle name '{name}' missing from catalog")


class TestTier3DeepProtocols(unittest.TestCase):
    """Verifies Tier-3 Deep Algorithmic Protocols (ARIZ-85-V, MMC, Step Back, Table 2, Trimming, AFD)."""

    ARIZ_DEEP_DIR = REFS_DIR / "ariz-deep"

    EXPECTED_PROTOCOLS = [
        "01a-ariz-85v-analysis.md",
        "01b-ariz-85v-resolution.md",
        "02-mmc-operator-protocol.md",
        "03-step-back-from-ifr.md",
        "04-physical-contradiction-tree.md",
        "05-trimming-algorithm.md",
        "06-subversion-analysis-afd.md",
    ]

    def test_ariz_deep_directory_and_exact_files_exist(self):
        self.assertTrue(self.ARIZ_DEEP_DIR.is_dir(), f"Directory {self.ARIZ_DEEP_DIR} must exist")
        actual_files = sorted([f.name for f in self.ARIZ_DEEP_DIR.glob("*.md")])
        self.assertEqual(
            actual_files,
            sorted(self.EXPECTED_PROTOCOLS),
            f"Expected exactly 7 protocol files in ariz-deep, got {actual_files}",
        )

    def test_ariz_deep_frontmatter_and_line_limits(self):
        for fname in self.EXPECTED_PROTOCOLS:
            fpath = self.ARIZ_DEEP_DIR / fname
            self.assertTrue(fpath.is_file(), f"File {fname} must exist")
            content = fpath.read_text(encoding="utf-8")
            self.assertTrue(
                content.startswith("---"),
                f"Protocol {fname} must start with YAML frontmatter",
            )
            self.assertIn(
                "description:",
                content,
                f"Protocol {fname} missing description in frontmatter",
            )
            self.assertIn(
                "metadata:",
                content,
                f"Protocol {fname} missing metadata in frontmatter",
            )
            lines = content.splitlines()
            self.assertLess(
                len(lines),
                500,
                f"Protocol {fname} exceeds 500 lines: {len(lines)} lines",
            )

    def test_ariz_deep_cross_references_and_prerequisites(self):
        for fname in self.EXPECTED_PROTOCOLS:
            fpath = self.ARIZ_DEEP_DIR / fname
            content = fpath.read_text(encoding="utf-8")
            self.assertIn(
                "## Prerequisites",
                content,
                f"Protocol {fname} must contain a '## Prerequisites' section",
            )

    def test_ariz_deep_algorithmic_integrity_keywords(self):
        # 01a: child's language, product-tool, T1/T2, micro-PC, IKR-2, 6 rules
        p01a = (self.ARIZ_DEEP_DIR / "01a-ariz-85v-analysis.md").read_text(encoding="utf-8")
        self.assertIn("детский язык", p01a)
        self.assertIn("Изделие", p01a)
        self.assertIn("Инструмент", p01a)
        self.assertIn("T_1", p01a)
        self.assertIn("T_2", p01a)
        self.assertIn("Микро-ФП", p01a)
        self.assertIn("ИКР-2", p01a)
        self.assertIn("6 правил", p01a)

        # 01b: Part 6 deadlock, multi-cycle N->inf, 4 secondary classes, Part 9 reflection
        p01b = (self.ARIZ_DEEP_DIR / "01b-ariz-85v-resolution.md").read_text(encoding="utf-8")
        self.assertIn("Часть 6", p01b)
        self.assertIn("многоцикловост", p01b)
        self.assertIn("Часть 9", p01b)
        self.assertIn("рефлекси", p01b)

        # 02: little people, Group A/B, role-prompting
        p02 = (self.ARIZ_DEEP_DIR / "02-mmc-operator-protocol.md").read_text(encoding="utf-8")
        self.assertIn("маленьких человечк", p02)
        self.assertIn("Группа А", p02)
        self.assertIn("Группа Б", p02)
        self.assertIn("ролевой", p02)

        # 03: step back from IFR, minimal dismantling defect
        p03 = (self.ARIZ_DEEP_DIR / "03-step-back-from-ifr.md").read_text(encoding="utf-8")
        self.assertIn("Шаг назад от ИКР", p03)
        self.assertIn("демонтирую", p03)
        self.assertIn("дефект", p03)

        # 04: Table 2, particle rules, vacuum/void
        p04 = (self.ARIZ_DEEP_DIR / "04-physical-contradiction-tree.md").read_text(encoding="utf-8")
        self.assertIn("Таблиц", p04)
        self.assertIn("Ветвь", p04)
        self.assertIn("правило частиц", p04)
        self.assertIn("пустот", p04)

        # 05: Trimming, Rules A, B, C
        p05 = (self.ARIZ_DEEP_DIR / "05-trimming-algorithm.md").read_text(encoding="utf-8")
        self.assertIn("свертыван", p05)
        self.assertIn("Правило А", p05)
        self.assertIn("Правило Б", p05)
        self.assertIn("Правило В", p05)

        # 06: Subversion / AFD, saboteur
        p06 = (self.ARIZ_DEEP_DIR / "06-subversion-analysis-afd.md").read_text(encoding="utf-8")
        self.assertIn("диверсионн", p06)
        self.assertIn("Anticipatory Failure Determination", p06)
        self.assertIn("оружи", p06)


if __name__ == "__main__":
    unittest.main(verbosity=2)

