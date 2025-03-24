# Automation Scripts

A collection of automation scripts for various tasks that streamline repetitive processes and improve efficiency. The scripts in this repository can be easily customized and executed for different use cases.

## Scripts

# Automation Scripts

A collection of Python and batch automation scripts for various tasks that streamline repetitive processes and improve efficiency.

## Scripts

### 1. **Rename Folders (Python)**
   - **Description**: Renames folders by replacing substrings.
   - **How to Use**:
     - Clone the repository or download the script.
     - Run the script using the following command:
       ```bash
       python rename.py <directory> <old_str1> <new_str1> <old_str2> <new_str2> ...
       ```
     - Example:
       ```bash
       python rename.py ./Test/ "OldName" "NewName" "RemoveThis" ""
       ```
#### Requirements
- Python 3.x
- argparse module (usually included in Python standard library)

### 2. **System Health Check and Update Reset (Batch)**
   - **Description**: This batch script performs a system file check, restores system health, resets Windows Update components, and runs a quick scan with Windows Defender.
   - **How to Use**:
     - Right-click on the batch file (`system_health_check.bat`) and select "Run as Administrator".
     - The script will run system checks and optimizations:
       - **SFC** and **DISM** commands to restore system health.
       - Stops and restarts Windows Update services.
       - Cleans up the SoftwareDistribution folder.
       - Runs a quick scan with Windows Defender.
       - Optimizes the disk by detecting if it's an SSD or HDD and runs the appropriate optimization.

## How to Contribute

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make changes and commit them.
4. Push to your fork and create a pull request.
