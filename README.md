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

## Requirements

- Python 3.8 or higher  
- [colorama](https://pypi.org/project/colorama/) (optional, for colored output)

Install colorama:

```bash
pip3 install colorama
