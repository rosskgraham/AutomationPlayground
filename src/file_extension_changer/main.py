"""
Script to add extension suffixes to files
    Files have no file type extensions
    Extensions are listed in a separate metadata file, files/meta.csv
"""

from pathlib import Path
import polars as pl
from collections import defaultdict
from alive_progress import alive_it

from shared_utils import list_files


files_path = Path(__file__).parent / "test_data" / "files"
meta_path = Path(__file__).parent / "test_data" / "meta.csv"

# Make a dict to lookup file types for renaming
# eg. {"folder1":{"file1":"txt","file2":"jpg"}}
mapping = defaultdict(dict)
for folder, file_path, type in [
    d.values() for d in pl.read_csv(meta_path, infer_schema=False).to_dicts()
]:
    mapping[folder].update({file_path: type})

# Rename the files
for file_path in alive_it(list_files(files_path)):
    folder, file = file_path.parent.stem ,file_path.stem
    ext = mapping.get(folder, {}).get(file, "unmapped")
    file_path.rename(file_path.with_suffix(f".{ext}"))
