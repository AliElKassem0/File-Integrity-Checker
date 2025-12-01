import os
import hashlib
import json
import sys

HASH_FILE = "hashes.json"

IGNORE = {".DS_Store"}

from colorama import init, Fore, Style
init(autoreset=True)


def hash_file(path):
    sha = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(4096):
            sha.update(chunk)
    return sha.hexdigest()

def get_all_files(folder_path):
    files = []
    for root, dirs, file_names in os.walk(folder_path):
        for name in file_names:
            if name in IGNORE:
                continue
            full_path = os.path.join(root, name)
            files.append(full_path)
    return files


def save_hashes(hashes):
    with open(HASH_FILE, "w") as f:
        json.dump(hashes, f, indent=4)

def load_hashes():
    if not os.path.exists(HASH_FILE):
        return {}
    with open(HASH_FILE, "r") as f:
        return json.load(f)

def init_hashes(folder_path):
    files = get_all_files(folder_path)
    hashes = {}
    for file in files:
        hashes[file] = hash_file(file)
    save_hashes(hashes)
    print(f"[✓] Baseline created for {len(files)} files.")

def check_hashes(folder_path):
    old_hashes = load_hashes()
    current_files = get_all_files(folder_path)

    for file in current_files:
        if file not in old_hashes:
            print(Fore.GREEN + f"[NEW] {file}")
        else:
            current_hash = hash_file(file)
            if current_hash != old_hashes[file]:
                print(Fore.RED + f"[MODIFIED] {file}")
            else:
                print(Fore.BLUE + f"[OK] {file} unchanged")

    for file in old_hashes:
        if file not in current_files:
            print(Fore.YELLOW + f"[DELETED] {file}")

def main():
    if len(sys.argv) < 3:
        print("Usage:")
        print("  python3 main.py init <folder_path>")
        print("  python3 main.py check <folder_path>")
        return

    command = sys.argv[1]
    folder = sys.argv[2]

    if command == "init":
        init_hashes(folder)
    elif command == "check":
        check_hashes(folder)
    else:
        print("Unknown command.")

if __name__ == "__main__":
    main()
