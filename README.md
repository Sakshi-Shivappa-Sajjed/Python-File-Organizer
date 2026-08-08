# Python File Organizer

A Python automation tool that scans a directory, classifies files by type, and organizes them into structured folders — with duplicate-safe handling, a dry-run preview mode, and activity logging.

## Why I Built This

Manually sorting downloads, documents, and media files is repetitive and error-prone. This project automates that process end-to-end, while giving me a hands-on way to practice core Python skills: file-system operations, error handling, logging, and writing clean, modular code.

## What It Does

- **Scans a folder** and classifies each file by extension (Images, Documents, Spreadsheets, Audio, Video, Code, Others)
- **Creates category folders automatically** and moves matching files into them
- **Detects duplicate filenames** and renames new files instead of overwriting existing ones
- **Offers a dry-run mode** so users can preview exactly what would move before any files are touched
- **Validates input paths** before running, to avoid errors on invalid or missing directories
- **Logs every action** (successful moves, errors, skipped files) for troubleshooting and audit purposes
- **Prints a summary report** showing totals per category once organizing is complete

## Why It's Useful

- Saves time on a task almost everyone deals with — a messy Downloads folder, a cluttered project directory, or a pile of unsorted exports
- The dry-run mode adds a safety net, so nothing is moved or lost unintentionally
- The same extension-based classification logic scales to broader use cases: log management, report processing, data ingestion pipelines, and digital asset organization
- Demonstrates practical, production-adjacent thinking (validation, logging, graceful error recovery) rather than just a script that works once

## Skills Demonstrated

- **Python fundamentals:** functions, conditionals, loops, dictionaries, f-strings, default arguments
- **File-system programming:** `pathlib` for path handling and directory traversal, `shutil` for file operations
- **Error handling:** `try`/`except` blocks so a single failed file doesn't crash the whole run
- **Logging:** structured activity logs using Python's `logging` module
- **Code organization:** modular, docstring-documented functions with a clean `if __name__ == "__main__"` entry point

No third-party dependencies — built entirely with the Python standard library.

## How to Run

```bash
git clone YOUR_REPOSITORY_URL
cd python-file-organizer
python organizer.py
```

You'll be prompted for a folder path and whether to run in dry-run mode. Dry-run shows what *would* happen; running normally performs the actual organization and prints a completion summary.

## Possible Next Steps

- Command-line interface via `argparse`
- Recursive directory scanning
- User-configurable category rules
- Undo/rollback functionality
- Unit test coverage

## Author

**Sakshi Shivappa Sajjed**