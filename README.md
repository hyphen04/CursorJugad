# Safe Cursor Config Reset Tool

A Python utility that safely resets Cursor IDE's telemetry configuration by generating new UUIDs while preserving other settings.

## Prerequisites

- Python 3.6 or higher
- Operating System: Windows, macOS, or Linux
- Cursor IDE installed on your system

## Installation

1. Clone this repository or download the script:
```bash
git clone https://github.com/hyphen04/CursorJugad.git
# or download safe_cursor_reset.py directly
```

2. Ensure Python is installed on your system:
```bash
python --version  # Should show Python 3.6 or higher
```

## Usage

1. Make sure Cursor IDE is not running before using this tool.

2. Run the script:
```bash
python safe_cursor_reset.py
```

The script will:
- Automatically detect your operating system and locate the Cursor configuration file
- Create a backup of your current configuration
- Generate new UUIDs for telemetry fields
- Update the configuration file with new values

## What it Does

The tool updates the following telemetry fields with new random UUIDs:
- telemetry.machineId
- telemetry.macMachineId
- telemetry.devDeviceId
- telemetry.sqmId

## File Locations

The configuration file (`storage.json`) is located at:
- Windows: `%APPDATA%\Cursor\User\globalStorage\storage.json`
- macOS: `~/Library/Application Support/Cursor/User/globalStorage/storage.json`
- Linux: `~/.config/Cursor/User/globalStorage/storage.json`

## Backup

Before making any changes, the script automatically creates a backup of your configuration file with a timestamp:
```
storage.json.backup_YYYYMMDD_HHMMSS
```

## Disclaimer

This tool is for educational purposes only. Modifying software configurations may violate terms of service. Use responsibly and at your own risk.

## License

[Your chosen license]

## Contributing

Feel free to submit issues and enhancement requests! 