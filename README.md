# File Integrity Checker

A simple **Python file integrity checker** that monitors changes, additions, and deletions in a folder.  
Inspired by professional tools like Tripwire, it’s useful for system security and folder monitoring.

---

## Features

- Scan a folder and create a **baseline snapshot** of all files  
- Detect **modified**, **new**, and **deleted files**  
- Ignore system files like `.DS_Store` automatically  
- Color-coded output for easy reading in Terminal  
- Works on macOS, Linux, and Windows  

---
Usage
  1. Initialize baseline (first snapshot)
  python3 main.py init /path/to/your/folder
  Scans all files in the folder and saves their hashes in hashes.json
  Example:
  python3 main.py init ~/Desktop/testfolder

  2. Check for changes
  python3 main.py check /path/to/your/folder
  Compares current files to the baseline
  Prints the status:
  [MODIFIED] file1.txt
  [NEW] file2.txt
  [DELETED] file3.txt
  [OK] file4.txt unchanged

---

## Requirements

- Python 3.8 or higher  
- [colorama](https://pypi.org/project/colorama/) (optional, for colored output)

Install colorama:

```bash
pip3 install colorama

