@echo off
:: Windows System Health Check and Windows Update Reset Script
:: Author: Amir Hossein Mobayen
:: Description: This script performs a system file check, restores system health, and resets Windows Update components.

:: Check for Administrator privileges
NET SESSION >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Please run this script as Administrator.
    pause
    exit /b
)

echo Running System File Checker (SFC)...
sfc /scannow

echo Running Deployment Image Servicing and Management (DISM) tool...
dism /online /cleanup-image /restorehealth

echo Stopping Windows Update and Background Intelligent Transfer Service...
net stop wuauserv
net stop bits

echo Cleaning SoftwareDistribution folder...
cd %windir%\SoftwareDistribution
del /f /s /q *.*

echo Restarting Windows Update and Background Intelligent Transfer Service...
net start wuauserv
net start bits

echo Running Windows Defender Quick Scan...
"%ProgramFiles%\Windows Defender\MpCmdRun.exe" -Scan -ScanType 1

:: Detect disk type and perform optimization
echo Detecting disk type for optimization...
wmic diskdrive get model, mediatype | find "SSD" > nul
IF %ERRORLEVEL% EQU 0 (
    echo Running TRIM on SSD...
    defrag C: /L
) ELSE (
    echo Running Disk Defragmentation on HDD...
    defrag C: /O
)


echo Process completed successfully!
pause