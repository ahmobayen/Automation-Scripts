import os
import argparse


def rename_folders(directory: str, replacements: dict):
    """
    Renames folders within a specified directory by replacing specified substrings.

    Parameters:
    directory (str): Path to the directory containing folders to rename.
    replacements (dict): A dictionary where keys are substrings to be replaced
                         and values are their replacements. An empty string as a value removes the key substring.
    """
    for folder_name in os.listdir(directory):
        folder_path = os.path.join(directory, folder_name)

        # Ensure it's a directory before processing
        if os.path.isdir(folder_path):
            new_folder_name = folder_name

            # Replace occurrences of old substrings with new substrings
            for old_str, new_str in replacements.items():
                if new_str:
                    new_folder_name = new_folder_name.replace(old_str, new_str).replace(old_str.capitalize(), new_str)
                else:
                    new_folder_name = new_folder_name.replace(old_str, "").replace(old_str.capitalize(), "")

            # Rename the folder if changes were made
            if new_folder_name != folder_name:
                new_folder_path = os.path.join(directory, new_folder_name)
                os.rename(folder_path, new_folder_path)
                print(f'Renamed "{folder_name}" to "{new_folder_name}"')


if __name__ == "__main__":
    # Argument parser setup
    parser = argparse.ArgumentParser(description="Rename folders by replacing substrings.")
    parser.add_argument("directory", type=str, help="Path to the directory containing folders to rename.")
    parser.add_argument("replacements", type=str, nargs='+',
                        help="Pairs of old and new substrings (e.g., 'old1 new1 old2 new2'). "
                             "Use 'old1 ""' to remove 'old1' from folder names.")
    args = parser.parse_args()

    # Ensure replacements are provided in pairs
    if len(args.replacements) % 2 != 0:
        print("Error: Replacements must be provided in pairs (old1 new1 old2 new2 ...)")
        exit(1)

    # Convert replacement arguments into a dictionary
    replacements = {args.replacements[i]: args.replacements[i + 1] for i in range(0, len(args.replacements), 2)}

    # Execute folder renaming
    rename_folders(args.directory, replacements)
