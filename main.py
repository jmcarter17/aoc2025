import importlib.util
import re
from pathlib import Path

base_path = Path(".")


def extract_day_number(folder_name):
    match = re.match(r"day(\d+)", folder_name)
    return int(match.group(1)) if match else float("inf")


def main():
    folders = [
        f for f in base_path.iterdir() if f.is_dir() and re.match(r"day\d+", f.name)
    ]
    folders.sort(key=lambda f: extract_day_number(f.name))

    for folder in folders:
        if folder.is_dir():
            solution_path = folder / "solution.py"
            if solution_path.exists():
                spec = importlib.util.spec_from_file_location("solution", solution_path)
                solution = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(solution)
                if hasattr(solution, "main"):
                    print("Solution for", folder)
                    solution.main()
                    print("================")


if __name__ == "__main__":
    main()
