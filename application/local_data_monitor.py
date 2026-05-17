import os
import json
import hashlib

STATE_FILE = "file_state.json"
ROOT_DIR = "./repo"


def file_hash(path):
    h = hashlib.sha256()

    with open(path, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)

    return h.hexdigest()


def load_state():
    if not os.path.exists(STATE_FILE):
        return {}

    with open(STATE_FILE, "r") as f:
        return json.load(f)


def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


def scan_files():
    current = {}

    for root, _, files in os.walk(ROOT_DIR):
        for file in files:
            path = os.path.join(root, file)

            current[path] = {
                "hash": file_hash(path)
            }

    return current


old_state = load_state()
new_state = scan_files()

new_files = []
changed_files = []
deleted_files = []

for path, meta in new_state.items():

    if path not in old_state:
        new_files.append(path)

    elif meta["hash"] != old_state[path]["hash"]:
        changed_files.append(path)

for path in old_state:
    if path not in new_state:
        deleted_files.append(path)

print("NEW:", new_files)
print("CHANGED:", changed_files)
print("DELETED:", deleted_files)

save_state(new_state)
    

