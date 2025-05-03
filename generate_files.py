from pathlib import Path
from random import randint, choices, choice
import shutil

files_path = Path("C:/git/FileExtensionChanger/files")
meta_path = Path(files_path / "meta.csv")
types = ["txt","ini","dat","bat"]

def generate_files(folders: int = 100, min_files: int = 1, max_files: int = 100) -> int:
    meta_path.unlink(missing_ok=True)
    if (files_path / "files").exists():
        shutil.rmtree(files_path / "files")
    file_count = 0
    with open(meta_path, "w") as csv:
        csv.write("folder,file,type\n")
        for folder in choices(range(100000, 999999), k=folders):
            for file in choices(range(100000, 999999), k=randint(min_files, max_files)):
                file_path = files_path / "files" / str(folder) / str(file)
                file_path.parent.mkdir(parents=True, exist_ok=True)
                file_type = choice(types)
                with open(file_path, "w") as f:
                    f.write(f"Hello World\n{file}.{file_type}")
                    file_count += 1
                csv.write(f"{folder},{file},{file_type}\n")
    return file_count

print(generate_files(100, 50, 100))
