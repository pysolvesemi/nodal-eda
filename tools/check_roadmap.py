#!/usr/bin/env python3
"""Validate the authoritative Markdown task graph, without inventing status.

Evidence validation checks local links/anchors, not the truth of test results.
Remote qualification and review remain explicit increment-closure obligations.
"""

from __future__ import annotations

import argparse
from collections import Counter, deque
from dataclasses import dataclass, field
from pathlib import Path
import re
import sys

ID = r"[A-Z]+-\d+(?:\.\d+)*"
TASK = re.compile(rf"^( *)- \[([ xX])\] \*\*({ID})(?=\*\*| —)(.*)$")
TASK_START = re.compile(r"^\s*[-*+] \[[^\]]*\]")
DEPENDENCY = re.compile(r"^  - \*\*Depends on:\*\* (.+)$")
EVIDENCE = re.compile(r"Evidence:\s*\[[^\]]+\]\(([^\s)]+)\)")


@dataclass
class Task:
    id: str
    checked: bool
    depth: int
    path: Path
    line: int
    evidence: str | None
    children: list[str] = field(default_factory=list)
    dependencies: set[str] = field(default_factory=set)

    def location(self) -> str:
        return f"{self.path}:{self.line}: {self.id}"


def unfenced(text: str):
    """Yield source-numbered prose; recognize matching backtick/tilde fences."""
    fence: tuple[str, int] | None = None
    for number, line in enumerate(text.splitlines(), 1):
        marker = re.match(r"^\s*(`{3,}|~{3,})(.*)$", line)
        if marker:
            token, suffix = marker.groups()
            if fence is None:
                fence = token[0], len(token)
            elif token[0] == fence[0] and len(token) >= fence[1] and not suffix.strip():
                fence = None
            continue
        if fence is None:
            yield number, line
    if fence is not None:
        raise ValueError("unclosed fenced code block")


def heading_anchors(text: str) -> set[str]:
    counts: Counter[str] = Counter()
    anchors = set()
    for _, line in unfenced(text):
        match = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
        if match:
            slug = re.sub(r"[^\w -]", "", match[1].lower()).replace(" ", "-")
            count = counts[slug]
            counts[slug] += 1
            anchors.add(slug + (f"-{count}" if count else ""))
    return anchors


def evidence_error(root: Path, task: Task) -> str | None:
    if not task.evidence:
        return "checked task has no local Evidence link"
    target, _, anchor = task.evidence.partition("#")
    if re.match(r"\w+:", target) or target.startswith("/"):
        return "evidence must reference a repository-local record"
    path = (task.path.parent / target).resolve() if target else task.path.resolve()
    if not path.is_relative_to(root) or not path.is_file():
        return "evidence file is missing or outside the repository"
    try:
        text = path.read_text(encoding="utf-8")
        if not text.strip():
            return "evidence record is empty"
        if anchor and anchor not in heading_anchors(text):
            return "evidence anchor is missing"
    except (OSError, UnicodeError, ValueError) as error:
        return f"unreadable evidence: {error}"
    return None


def check(root: Path, files: list[Path] | None = None) -> tuple[dict[str, Task], list[str]]:
    root = root.resolve()
    paths = files if files is not None else sorted((root / "docs/roadmap/tracks").glob("*.md"))
    tasks: dict[str, Task] = {}
    errors: list[str] = []
    declarations: dict[str, str] = {}
    if not paths:
        return {}, ["no roadmap track files found"]
    for path in paths:
        path = path.resolve()
        if not path.is_relative_to(root):
            errors.append(f"{path}: track is outside the repository")
            continue
        stack: list[Task] = []
        parent: Task | None = None
        file_tasks = 0
        try:
            for number, line in unfenced(path.read_text(encoding="utf-8")):
                match = TASK.match(line)
                if match:
                    file_tasks += 1
                    depth = len(match[1])
                    task_id = match[3]
                    evidence = EVIDENCE.search(line)
                    task = Task(task_id, match[2].lower() == "x", depth, path, number,
                                evidence[1] if evidence else None)
                    if task_id in tasks:
                        errors.append(f"{task.location()}: duplicate task ID")
                        continue
                    tasks[task_id] = task
                    while stack and stack[-1].depth >= depth:
                        stack.pop()
                    if depth != 2 * task_id.count("."):
                        errors.append(f"{task.location()}: ID and indentation disagree")
                    if depth:
                        if not stack or stack[-1].depth != depth - 2:
                            errors.append(f"{task.location()}: missing immediate parent")
                        elif task_id.rsplit(".", 1)[0] != stack[-1].id:
                            errors.append(f"{task.location()}: ID does not belong to its parent")
                        else:
                            stack[-1].children.append(task_id)
                    else:
                        parent = task
                    stack.append(task)
                elif TASK_START.match(line):
                    errors.append(f"{path}:{number}: malformed task or indentation")
                elif "**Depends on:**" in line:
                    dependency = DEPENDENCY.match(line)
                    if not dependency or parent is None:
                        errors.append(f"{path}:{number}: malformed dependency declaration")
                    elif parent.id in declarations:
                        errors.append(f"{path}:{number}: duplicate dependency declaration")
                    else:
                        declarations[parent.id] = dependency[1]
        except (OSError, UnicodeError, ValueError) as error:
            errors.append(f"{path}: {error}")
        if not file_tasks:
            errors.append(f"{path}: track contains no tasks")
    for task in tasks.values():
        if task.depth == 0:
            declaration = declarations.get(task.id)
            if declaration is None:
                errors.append(f"{task.location()}: missing dependency declaration")
            else:
                task.dependencies.update(re.findall(rf"\b{ID}\b", declaration))
                earlier = re.search(r"all earlier ([A-Z]+) increments", declaration)
                if earlier:
                    prefix = earlier[1]
                    if not task.id.startswith(prefix + "-"):
                        errors.append(f"{task.location()}: invalid earlier-increment scope")
                    else:
                        ordinal = int(task.id.split("-")[1].split(".")[0])
                        task.dependencies.update(
                            other.id for other in tasks.values()
                            if other.depth == 0 and "." not in other.id and other.id.startswith(prefix + "-")
                            and int(other.id.split("-")[1]) < ordinal
                        )
                residual = re.sub(rf"\b{ID}\b", "", declaration)
                residual = re.sub(r"all earlier [A-Z]+ increments", "", residual)
                residual = re.sub(r"\b(?:none|and)\b|[,.\s]", "", residual)
                if residual:
                    errors.append(f"{task.location()}: unrecognized dependency syntax")
            if not task.id.startswith("FND-"):
                task.dependencies.add("FND-10")
        for dependency in task.dependencies:
            if dependency not in tasks:
                errors.append(f"{task.location()}: unknown dependency {dependency}")
            elif tasks[dependency].depth != 0:
                errors.append(f"{task.location()}: dependency must name an increment")
            elif task.checked and not tasks[dependency].checked:
                errors.append(f"{task.location()}: checked task has open dependency {dependency}")
        if task.checked:
            if any(not tasks[child].checked for child in task.children):
                errors.append(f"{task.location()}: checked ancestor has an open descendant")
            reason = evidence_error(root, task)
            if reason:
                errors.append(f"{task.location()}: {reason}")
    # Kahn's algorithm keeps long valid roadmaps independent of Python recursion limits.
    indegree = {task.id: len(task.dependencies & tasks.keys()) for task in tasks.values()}
    dependents: dict[str, list[str]] = {task_id: [] for task_id in tasks}
    for task in tasks.values():
        for dependency in task.dependencies & tasks.keys():
            dependents[dependency].append(task.id)
    ready = deque(sorted(key for key, count in indegree.items() if count == 0))
    visited = 0
    while ready:
        current = ready.popleft()
        visited += 1
        for dependent in dependents[current]:
            indegree[dependent] -= 1
            if indegree[dependent] == 0:
                ready.append(dependent)
    if visited != len(tasks):
        errors.append("dependency cycle: " + ", ".join(sorted(k for k, v in indegree.items() if v)))
    return tasks, sorted(errors)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    tasks, errors = check(args.root)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    leaves = sum(not task.children for task in tasks.values())
    completed = sum(task.checked and not task.children for task in tasks.values())
    print(f"Roadmap valid: {len(tasks)} tasks; {completed}/{leaves} required leaves complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
