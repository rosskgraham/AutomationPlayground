from pathlib import Path


def list_files(path: Path, recurse: bool = True) -> list[Path]:
    """List files in a directory and subdirectories."""
    paths: list[Path] = []
    for p in path.iterdir():
        if p.is_dir():
            paths.extend(list_files(p))
        else:
            paths.append(p)
    return paths
