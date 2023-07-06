import os
import json
import zipfile


# Get the directory path of the current script file
script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(script_dir)

mods_unpacked_path = os.path.join(script_dir, "root\\mods-unpacked")
# Get a list of all the items in the directory
items = os.listdir(mods_unpacked_path)
# Loop over the items and find the first folder
for item in items:
    item_path = os.path.join(mods_unpacked_path, item)
    if os.path.isdir(item_path):
        # Found the first folder, so return its name
        first_folder_name = item
        break

# Open the manifest.json file and load its contents as a dictionary
manifest_path = os.path.join(os.path.join(mods_unpacked_path, first_folder_name), "manifest.json")
with open(manifest_path, "r") as manifest_file:
    manifest_data = json.load(manifest_file)
    namespace = manifest_data["namespace"]
    name = manifest_data["name"]
    version = manifest_data["version_number"]

zip_name = f"{namespace}-{name}-{version}.zip"

# Create a new zip file
zip_file = zipfile.ZipFile(zip_name, "w")

# Add mod icon
zip_file.write(os.path.join(script_dir, ".publish\\icon.png"), "icon.png")
# Add mod manifest
zip_file.write(manifest_path, "manifest.json")

# Add mod files

root_dir = os.path.join(script_dir, "root")
for root, dirs, files in os.walk(root_dir):
    for file in files:
        file_path = os.path.join(root, file)
        relative_path = os.path.relpath(file_path, root_dir)
        zip_file.write(file_path, relative_path)

mod_name = os.path.basename(script_dir).lower().replace("otdan-", "", 1)
# Add import files
for root, dirs, files in os.walk("E:\\Projects\\Godot\\Modding\\brotato\\BrotatoModding\\.import"):
    for file in files:
        if file.startswith(mod_name):
            zip_file.write(os.path.join(root, file), os.path.join(".import", os.path.basename(file)))


