from pathlib import Path
import logging
import shutil


FILE_CATEGORIES = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",

    ".pdf": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",

    ".csv": "Spreadsheets",
    ".xlsx": "Spreadsheets",

    ".mp3": "Audio",
    ".wav": "Audio",

    ".mp4": "Videos",
    ".mkv": "Videos",

    ".py": "Code",
    ".java": "Code",
    ".js": "Code"
}


logging.basicConfig(
    filename="organizer.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def get_category(extension):
    """Return the category for a file extension."""

    return FILE_CATEGORIES.get(extension, "Others")


def get_unique_filename(destination, filename):
    """Return a unique destination path for a file."""

    file_path = destination / filename

    if not file_path.exists():
        return file_path

    counter = 1

    while True:
        new_name = (
            f"{file_path.stem}_{counter}"
            f"{file_path.suffix}"
        )

        new_path = destination / new_name

        if not new_path.exists():
            return new_path

        counter += 1


def organize_files(folder, dry_run=False):
    """Organize files inside the given folder."""

    summary = {}

    for item in folder.iterdir():

        if not item.is_file():
            continue

        extension = item.suffix.lower()
        category = get_category(extension)

        destination = folder / category
        destination.mkdir(exist_ok=True)

        try:
            destination_file = get_unique_filename(
                destination,
                item.name
            )

            if dry_run:

                print(
                    f"[DRY RUN] {item.name} "
                    f"→ {destination_file}"
                )

                continue

            shutil.move(
                item,
                destination_file
            )

            summary[category] = (
                summary.get(category, 0) + 1
            )

            print(
                f"{item.name} → "
                f"{destination_file.name}"
            )

            logging.info(
                f"MOVED: {item.name} → "
                f"{destination_file}"
            )

        except Exception as error:

            print(
                f"Could not move {item.name}: "
                f"{error}"
            )

            logging.error(
                f"Could not move {item.name}: "
                f"{error}"
            )

    return summary


def main():

    folder_path = input(
        "Enter the folder path: "
    ).strip()

    folder = Path(folder_path)

    if not folder.exists():

        print("Folder does not exist.")

        logging.error(
            f"Folder does not exist: {folder}"
        )

        return

    if not folder.is_dir():

        print("The path is not a folder.")

        logging.error(
            f"Path is not a folder: {folder}"
        )

        return

    choice = input(
        "Run in dry-run mode? (y/n): "
    ).strip().lower()

    dry_run = choice == "y"

    if dry_run:
        print("\nDRY RUN - No files will be moved.\n")
    else:
        print("\nOrganizing files...\n")

    summary = organize_files(
        folder,
        dry_run
    )

    if dry_run:
        print("\nDry run complete.")
        return

    print("\n" + "=" * 35)
    print("ORGANIZATION COMPLETE")
    print("=" * 35)

    total_files = sum(summary.values())

    print(f"Total files organized: {total_files}\n")

    for category, count in summary.items():
        print(f"{category}: {count}")


if __name__ == "__main__":
    main()