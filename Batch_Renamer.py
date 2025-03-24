import os
import argparse

def rename_folders(directory: str, replacements: dict):
    for folder_name in os.listdir(directory):
        folder_path = os.path.join(directory, folder_name)
        if os.path.isdir(folder_path):
            new_folder_name = folder_name
            for old_str, new_str in replacements.items():
                new_folder_name = new_folder_name.replace(old_str, new_str).replace(old_str.capitalize(), new_str) if new_str else new_folder_name.replace(old_str, "").replace(old_str.capitalize(), "")
            
            if new_folder_name != folder_name:
                new_folder_path = os.path.join(directory, new_folder_name)
                os.rename(folder_path, new_folder_path)
                print(f'Renamed "{folder_name}" to "{new_folder_name}"')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rename folders by replacing substrings.")
    parser.add_argument("directory", type=str, help="Path to the directory.")
    parser.add_argument("replacements", type=str, nargs='+', help="Pairs of old and new substrings (e.g., 'old1 new1 old2 new2', use 'old1 '""' to remove old1).")
    args = parser.parse_args()
    
    if len(args.replacements) % 2 != 0:
        print("Error: Replacements must be provided in pairs (old1 new1 old2 new2 ...)")
        exit(1)
    
    replacements = {args.replacements[i]: args.replacements[i+1] for i in range(0, len(args.replacements), 2)}
    rename_folders(args.directory, replacements)
