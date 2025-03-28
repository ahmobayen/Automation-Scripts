import os
import re
import sys


def get_files(directory):
    """
    Scans the given directory and extracts numerical file names.

    Args:
        directory (str): The path to the directory to scan.

    Returns:
        tuple: A set of extracted numerical file names and a list of all file names in the directory.
    """
    files = os.listdir(directory)
    numbers = {int(re.search(r"(\d+)", f).group(1)) for f in files if re.search(r"(\d+)", f)}
    return numbers, files


def find_missing_files(directory):
    """
    Identifies missing files in a numerical sequence based on existing files in the directory.

    Args:
        directory (str): The path to the directory to scan.

    Returns:
        list: A list of missing file names reconstructed from the detected pattern.
    """
    existing_numbers, files = get_files(directory)
    if not existing_numbers:
        return []

    expected_numbers = set(range(min(existing_numbers), max(existing_numbers) + 1))
    missing_numbers = expected_numbers - existing_numbers

    # Attempt to determine file naming pattern (prefix and extension)
    sample_file = next((f for f in files if re.search(r"(\d+)", f)), "")
    match = re.match(r"(\D*)(\d+)(\..+)", sample_file)
    prefix, ext = match.group(1, 3) if match else ("", "")

    return [f"{prefix}{num}{ext}" for num in sorted(missing_numbers)]


if __name__ == "__main__":
    """
    Main execution point for the script. 
    Accepts a directory path as a command-line argument, scans for missing files, and prints the results.
    """
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory>")
        sys.exit(1)

    directory_to_scan = sys.argv[1]
    missing_files = find_missing_files(directory_to_scan)

    if missing_files:
        print("Missing files:", missing_files)
    else:
        print("No files missing.")
