from pathlib import Path

folders = [
    "src/core",
    "src/kernel",
    "src/desktop",
    "src/apps",
    "src/services",
    "src/system",
    "src/ui",
    "src/assets",
    "src/themes",
    "build",
    "iso",
    "docs",
    "scripts",
    "tests"
]

files = [
    "README.md",
    "requirements.txt",
    "pyproject.toml",
    "src/desktop/main.py"
]


def create_project():

    print("\nCreating BioVerse OS Project...\n")

    for folder in folders:
        Path(folder).mkdir(parents=True, exist_ok=True)

    for file in files:
        p = Path(file)

        if not p.exists():
            p.touch()

    print("Project Created Successfully!")

    print("\nFolders Created")

    for f in folders:
        print("✓", f)

    print("\nFiles Created")

    for f in files:
        print("✓", f)