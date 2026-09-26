"""Independent miniature roadmaps with hand-specified acceptance outcomes."""

from pathlib import Path
import tempfile
import unittest

from tools.check_roadmap import check


PARTIAL = """- [ ] **FND-01 — Bootstrap**
  - **Depends on:** none.
  - [x] **FND-01.1** CLI. Evidence: [run](evidence.md#result)
  - [ ] **FND-01.2** Integration.
"""
CLOSED = """- [x] **FND-01 — Bootstrap** Evidence: [run](evidence.md#result)
  - **Depends on:** none.
  - [x] **FND-01.1** CLI. Evidence: [run](evidence.md#result)
"""


class RoadmapTests(unittest.TestCase):
    def run_case(self, source):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            track = root / "track.md"
            track.write_text(source, encoding="utf-8")
            (root / "evidence.md").write_text("# Evidence\n\n## Result\n\nIndependent fixture result.\n")
            return check(root, [track])

    def rejects(self, source, expected):
        _, errors = self.run_case(source)
        self.assertTrue(any(expected in error for error in errors), errors)

    def test_partial_progress_keeps_parent_open(self):
        tasks, errors = self.run_case(PARTIAL)
        self.assertEqual(errors, [])
        self.assertFalse(tasks["FND-01"].checked)
        self.assertTrue(tasks["FND-01.1"].checked)

    def test_closed_tree_with_evidence(self):
        _, errors = self.run_case(CLOSED)
        self.assertEqual(errors, [])

    def test_premature_parent_closure(self):
        self.rejects(PARTIAL.replace("- [ ] **FND-01 — Bootstrap**", "- [x] **FND-01 — Bootstrap** Evidence: [run](evidence.md#result)"), "open descendant")

    def test_closed_child_with_open_grandchild(self):
        self.rejects(CLOSED + "    - [ ] **FND-01.1.1** Still open.\n", "open descendant")

    def test_duplicate_id(self):
        self.rejects(PARTIAL + "  - [ ] **FND-01.2** Duplicate.\n", "duplicate task ID")

    def test_missing_parent(self):
        self.rejects("    - [ ] **FND-01.1.1** Orphan.\n", "missing immediate parent")

    def test_wrong_id_parent(self):
        self.rejects(PARTIAL.replace("FND-01.2", "FND-02.2"), "does not belong")

    def test_tabs_and_odd_indentation(self):
        for indent in ("\t", " ", "   "):
            with self.subTest(indent=repr(indent)):
                _, errors = self.run_case(PARTIAL.replace("  - [ ]", indent + "- [ ]"))
                self.assertTrue(errors)

    def test_malformed_task(self):
        self.rejects(PARTIAL + "  - [yes] **FND-01.3** Invalid state.\n", "malformed task")

    def test_required_evidence_is_not_optional(self):
        self.rejects(CLOSED.replace(" Evidence: [run](evidence.md#result)", ""), "no local Evidence link")

    def test_missing_file_anchor_and_external_evidence(self):
        for target, expected in [("missing.md", "missing or outside"), ("evidence.md#absent", "anchor is missing"), ("https://example.org/pass", "repository-local")]:
            with self.subTest(target=target):
                self.rejects(CLOSED.replace("evidence.md#result", target), expected)

    def test_evidence_cannot_escape_repository(self):
        self.rejects(CLOSED.replace("evidence.md#result", "../evidence.md"), "missing or outside")

    def test_unknown_dependency(self):
        self.rejects(PARTIAL.replace("none.", "FND-99."), "unknown dependency FND-99")

    def test_cycle(self):
        self.rejects("- [ ] **FND-01 — A**\n  - **Depends on:** FND-02.\n- [ ] **FND-02 — B**\n  - **Depends on:** FND-01.\n", "dependency cycle")

    def test_open_dependency_prevents_closed_parent(self):
        source = CLOSED.replace("none.", "FND-02.") + "- [ ] **FND-02 — Prerequisite**\n  - **Depends on:** none.\n"
        self.rejects(source, "open dependency FND-02")

    def test_implicit_foundation_gate(self):
        self.rejects("- [ ] **TOOL-01 — Integration**\n  - **Depends on:** none.\n", "unknown dependency FND-10")

    def test_all_earlier_foundation_dependency_and_no_false_consumer_edge(self):
        source = PARTIAL + "- [ ] **FND-10 — Acceptance**\n  - **Depends on:** FND-01 and all earlier FND increments.\n  - Later consumer TOOL-99 is not a dependency.\n"
        tasks, errors = self.run_case(source)
        self.assertEqual(errors, [])
        self.assertEqual(tasks["FND-10"].dependencies, {"FND-01"})

    def test_missing_duplicate_and_invalid_dependency_declarations(self):
        for source, expected in [
            (PARTIAL.replace("  - **Depends on:** none.\n", ""), "missing dependency declaration"),
            (PARTIAL + "  - **Depends on:** none.\n", "duplicate dependency declaration"),
            (PARTIAL.replace("none.", "whenever available."), "unrecognized dependency syntax"),
        ]:
            with self.subTest(expected=expected):
                self.rejects(source, expected)

    def test_fenced_examples_are_ignored(self):
        example = "- [x] **FND-99 — Invalid example**\n"
        for opening, closing in [("```markdown", "```"), ("~~~~markdown", "~~~~"), ("````markdown", "````")]:
            with self.subTest(opening=opening):
                tasks, errors = self.run_case(PARTIAL + opening + "\n" + example + "```\n" + closing + "\n" if len(closing) > 3 else PARTIAL + opening + "\n" + example + closing + "\n")
                self.assertEqual(errors, [])
                self.assertNotIn("FND-99", tasks)

    def test_unclosed_fence_is_not_silent(self):
        self.rejects(PARTIAL + "```markdown\n", "unclosed fenced")

    def test_empty_track_directory_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            _, errors = check(Path(directory))
            self.assertEqual(errors, ["no roadmap track files found"])

    def test_empty_track_and_malformed_root_do_not_pass_or_crash(self):
        self.rejects("# Empty track\n", "track contains no tasks")
        self.rejects("- [ ] **FND-01.1** Bad root.\n  - **Depends on:** none.\n- [ ] **FND-10 — End**\n  - **Depends on:** all earlier FND increments.\n", "ID and indentation disagree")


if __name__ == "__main__":
    unittest.main()
