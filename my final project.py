import sys
import os


def initialize_workspace():
    """Ensures the directory structure is ready for personal work."""
    personal_dir = "personal"
    if not os.path.exists(personal_dir):
        os.makedirs(personal_dir)
        print(f"[+] Created personal directory: ./{personal_dir}")
    else:
        print(f"[*] Workspace Ready: ./{personal_dir} found.")


def check_environment():
    """Validates the Python version and venv status."""
    v = sys.version_info
    print(f"[*] System: Python {v.major}.{v.minor}.{v.micro}")

    # Identify if running in a virtual environment
    is_venv = sys.base_prefix != sys.prefix or hasattr(sys, 'real_prefix')

    if is_venv:
        print("[+] Environment: Virtual Environment Active.")
    else:
        print("[!] Warning: Running in global scope. Activate 'venv' for safety.")


def run_logic():
    """Placeholder for the main execution logic."""
    print("[*] Initializing core tasks...")

    # This represents your project successfully finishing its tasks
    print("[+] Task successfully executed. success script")


if __name__ == "__main__":
    try:
        initialize_workspace()
        check_environment()
        run_logic()
    except Exception as e:
        print(f"[X] Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n[X] Critical Error: {e}")
        sys.exit(1)