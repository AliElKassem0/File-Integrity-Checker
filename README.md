# File Integrity Checker

A small command-line tool in Python that detects when files in a folder are **modified, added or deleted**. It works like a minimal version of tools such as Tripwire: take a snapshot of a folder once, then compare against it later.

## How it works

1. `init` walks through the folder (including subfolders), computes a **SHA-256 hash** of every file and saves them as a baseline in `hashes.json`.
2. `check` hashes every file again and compares with the baseline. Any change to a file's content, even a single byte, gives a different hash.

## Requirements

- Python 3.8 or newer
- [colorama](https://pypi.org/project/colorama/) for the coloured output

```bash
pip3 install colorama
```

## Usage

Create the baseline:

```bash
python3 main.py init ~/Documents/important
```

```
[✓] Baseline created for 3 files.
```

Later, check the folder against it:

```bash
python3 main.py check ~/Documents/important
```

```
[OK] /Users/you/Documents/important/notes.txt unchanged
[MODIFIED] /Users/you/Documents/important/config.ini
[NEW] /Users/you/Documents/important/unknown.sh
[DELETED] /Users/you/Documents/important/backup.zip
```

In the terminal, each status has its own colour: blue for OK, red for modified, green for new and yellow for deleted.

## Good to know

- `hashes.json` is created in the folder you run the command from. Run `init` and `check` from the same place.
- Use the same folder path for `init` and `check` (both absolute or both relative), because files are matched by their path.
- macOS `.DS_Store` files are ignored.
- The baseline itself isn't protected. Someone who can change your files could also update `hashes.json`. Real integrity tools store the baseline somewhere safe or sign it.

## License

[MIT](LICENSE)
