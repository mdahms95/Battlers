import json
from pathlib import Path
import zipfile

root = Path(__file__).parent
input_path = root / "Battlers.json"
database_path = root / "packs" / "Battlers.db"
output_zip = zipfile.ZipFile(root / "Battlers.zip", "w")

# Loads the json data
with input_path.open(encoding='utf-8') as fp:
    data = json.load(fp)

# Coverts the .json to the expected .db
with database_path.with_suffix(".db").open("w", encoding='utf-8') as fp:
    for entry in data["RollTable"]:
        fp.write(json.dumps(entry))
        fp.write("\n")

# This will zip the files
output_zip.write(database_path, "packs/Battlers.db")
output_zip.write(Path(r"module.json"), "module.json")
output_zip.close()
