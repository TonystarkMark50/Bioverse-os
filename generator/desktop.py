from pathlib import Path

def create_desktop():
    shell_dir = Path("src") / "shell"
    shell_dir.mkdir(parents=True, exist_ok=True)

    main_file = shell_dir / "main.py"

    code = """print("Welcome to BioVerse OS Desktop v0.1")"""

    main_file.write_text(code, encoding="utf-8")

    print("[OK] Desktop generated successfully!")
    print(f"[OK] Created: {main_file}")