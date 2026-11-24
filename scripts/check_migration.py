"""Verify protected source files against the authorized pinned working-tree snapshot."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = json.loads((ROOT / "docs/SOURCE_SNAPSHOT.json").read_text())
# These imported files intentionally change for product text, setup, or documentation only.
ALLOWED_CHANGES = {
    ".env.example", ".gitignore", "README.md", "BUILD_PROMPT.md", "SKILL.md",
    "apps/web/app/layout.tsx", "apps/web/components/shell.tsx", "apps/web/package.json",
    "apps/web/package-lock.json", "services/api/app/main.py", "docs/ARCHITECTURE.md",
}
failures = []
checked = 0
for entry in MANIFEST["files"]:
    relative = entry["path"]
    if relative in ALLOWED_CHANGES:
        continue
    path = ROOT / relative
    if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != entry["sha256"]:
        failures.append(relative)
    checked += 1
if failures:
    raise SystemExit("Unexpected source changes: " + ", ".join(failures))
print(f"Preserved {checked} protected source files byte-for-byte, including models, migrations, routes and tests.")
