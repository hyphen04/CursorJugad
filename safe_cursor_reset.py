#!/usr/bin/env python3
"""
Safe Cursor Config Reset Tool

This script reads the Cursor configuration file (storage.json),
backs it up, and updates specific telemetry fields with new random UUIDs.

DISCLAIMER:
Modifying software configurations may violate terms of service.
This code is for educational purposes only. Use responsibly and at your own risk.
"""

import os
import sys
import json
import uuid
import shutil
from datetime import datetime

# List of telemetry keys to refresh.
TELEMETRY_KEYS = [
    "telemetry.machineId",
    "telemetry.macMachineId",
    "telemetry.devDeviceId",
    "telemetry.sqmId"
]

def generate_new_ids():
    """Generate new UUIDs for telemetry fields."""
    return {key: str(uuid.uuid4()) for key in TELEMETRY_KEYS}

def backup_file(file_path):
    """Create a backup of the configuration file."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = f"{file_path}.backup_{timestamp}"
    try:
        shutil.copy2(file_path, backup_path)
        print(f"[INFO] Backup created at: {backup_path}")
    except Exception as e:
        print(f"[ERROR] Could not backup file: {e}")
        sys.exit(1)

def update_config_file(config_path):
    """Load the configuration file, update telemetry fields, and save it."""
    # Read the current configuration
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            config_data = json.load(f)
    except Exception as e:
        print(f"[ERROR] Reading config file failed: {e}")
        sys.exit(1)

    new_ids = generate_new_ids()
    # Update or add the telemetry fields
    for key, new_id in new_ids.items():
        config_data[key] = new_id
        print(f"[INFO] Set {key} to {new_id}")

    # Write the updated configuration back to the file
    try:
        with open(config_path, "w", encoding="utf-8") as f:
            json.dump(config_data, f, indent=4)
        print("[INFO] Configuration file updated successfully.")
    except Exception as e:
        print(f"[ERROR] Writing config file failed: {e}")
        sys.exit(1)

def get_config_path():
    """Determine the configuration file path based on the operating system."""
    if sys.platform.startswith('win'):
        return os.path.join(os.getenv('APPDATA'), 'Cursor', 'User', 'globalStorage', 'storage.json')
    elif sys.platform == 'darwin':
        return os.path.expanduser('~/Library/Application Support/Cursor/User/globalStorage/storage.json')
    elif sys.platform.startswith('linux'):
        return os.path.expanduser('~/.config/Cursor/User/globalStorage/storage.json')
    else:
        print(f"[ERROR] Unsupported operating system: {sys.platform}")
        sys.exit(1)

def main():
    config_path = get_config_path()
    if not os.path.isfile(config_path):
        print(f"[ERROR] Configuration file not found at: {config_path}")
        sys.exit(1)

    print(f"[INFO] Processing configuration file: {config_path}")
    backup_file(config_path)
    update_config_file(config_path)

if __name__ == "__main__":
    main()
