import sys
from pathlib import Path

# Ensure project root is on sys.path before tests/ so imports like 'truco.*' resolve to the package
PROJECT_ROOT = Path(__file__).resolve().parent.parent
PROJECT_ROOT_STR = str(PROJECT_ROOT)
if PROJECT_ROOT_STR not in sys.path:
    sys.path.insert(0, PROJECT_ROOT_STR)
