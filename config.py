# Configuration utilities by Andrew6870
import json

def load_config(config_file):
    """Load configuration from JSON file"""
    try:
        with open(config_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"default": "settings"}

def save_config(config, config_file):
    """Save configuration to JSON file"""
    with open(config_file, 'w') as f:
        json.dump(config, f, indent=2)
