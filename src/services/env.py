from pathlib import Path
import sys

def setup_project():
    """
    Adds the project 'src/' folder to sys.path so modules like 'services.config' can be imported.
    Call this at the top of any notebook.
    """
    current = Path.cwd()
    while not (current / "src").exists():
        if current == current.parent:
            raise RuntimeError("Could not find project root containing 'src/' directory.")
        current = current.parent

    src_path = current / "src"
    if str(src_path) not in sys.path:
        sys.path.insert(0, str(src_path))
    
    print(f"✅ Project path added to sys.path: {src_path}")
