"""Hook automatically executed after creating the project."""
import os
import shutil


def remove_folder_or_file(path: str) -> None:
    """Remove a file or folder, based on its path."""
    if os.path.isfile(path):
        os.unlink(path)
    elif os.path.isdir(path):
        shutil.rmtree(path)


def remove_garbage_files() -> None:
    """Remove all files and folders present in .gitignore."""
    with open(".gitignore") as ignored_assets:
        content = ignored_assets.readlines()

        for asset in content:
            if asset.startswith("/"):
                asset_name = asset[1:].strip()
                remove_folder_or_file(asset_name)


def main() -> None:
    """Run the functions of interest."""
    remove_garbage_files()


main()
