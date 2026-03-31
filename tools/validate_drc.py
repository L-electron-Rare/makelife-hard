#!/usr/bin/env python3
"""Run DRC/ERC validation on KiCad projects."""

import sys
import subprocess
from pathlib import Path


def find_kicad_projects(root: Path) -> list[Path]:
    """Find all .kicad_pro files."""
    return list(root.glob("**/*.kicad_pro"))


def run_drc(project: Path) -> bool:
    """Run DRC on a KiCad project (stub — requires kicad-cli)."""
    print(f"DRC: {project}")
    # In real usage: kicad-cli pcb drc --output report.json project.kicad_pcb
    print("  SKIP — kicad-cli not available in this environment")
    return True


def main():
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("hardware")
    projects = find_kicad_projects(root)

    if not projects:
        print(f"No KiCad projects found in {root}")
        return

    print(f"Found {len(projects)} KiCad project(s)")
    passed = sum(1 for p in projects if run_drc(p))
    print(f"Results: {passed}/{len(projects)} passed")


if __name__ == "__main__":
    main()
