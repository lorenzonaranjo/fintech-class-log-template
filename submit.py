"""Make the file you hand in on Canvas: your whole class log, with its history.

Run it from your class log folder at the end of each class, after committing:

    python submit.py

It writes a .bundle file in the folder above this one (your course folder).
"""

import subprocess
import sys
from datetime import datetime
from pathlib import Path


def git(*args):
    return subprocess.run(["git", *args], capture_output=True, text=True)


repo = Path(__file__).resolve().parent
if git("-C", str(repo), "rev-parse", "--is-inside-work-tree").returncode != 0:
    sys.exit("This folder is not a git repository. Run submit.py from your class log folder.")

status = git("-C", str(repo), "status", "--porcelain").stdout.strip()
if status:
    sys.exit("These files have changes that are not committed:\n" + status
             + "\n\nCommit them, then run submit.py again.")

out = repo.parent / f"class-log-{datetime.now():%Y-%m-%d-%H%M}.bundle"
made = git("-C", str(repo), "bundle", "create", str(out), "--all")
if made.returncode != 0 or git("-C", str(repo), "bundle", "verify", str(out)).returncode != 0:
    sys.exit("Could not create the bundle:\n" + made.stderr)

commits = git("-C", str(repo), "rev-list", "--count", "HEAD").stdout.strip()
print(f"\nCreated {out}")
print(f"It contains {commits} commits. Upload this file to the session's Canvas assignment.")

unpushed = git("-C", str(repo), "log", "--oneline", "@{u}..HEAD")
if unpushed.returncode == 0 and unpushed.stdout.strip():
    print("Remember to push as well (git push), so that GitHub keeps a copy.")
