import os
import subprocess
import shutil

# file paths
system_file = "/private/var/db/os_eligibility/eligibility.plist"
replacement_file = "/Users/YOUR_USERNAME/Downloads/hazemirror/eligibility.plist"  # change "YOUR_USERNAME" to your user,if u don't know your user type whoami command and take the user from there


# file change function
def replace_files():
    try:
        # backup create 
        backup_file = f"{system_file}.backup"
        if not os.path.exists(backup_file):
            shutil.copy(system_file, backup_file)

        
        print("Root permisson required")
        subprocess.run(['sudo', 'cp', replacement_file, system_file], check=True)
        print("File changed successfully.")

    except Exception as e:
        print(f"Error: {e}")


# App start
def launch_mirroring_app():
    try:
        # Run with sudo
        print("Application starting iPhone Mirroring...")
        subprocess.run(['open', '/System/Applications/iPhone Mirroring.app'], check=True)
        print("Access granted.")
	
    except Exception as e:
        print(f"Update os to macos sequoia,the error: {e}")


if __name__ == "__main__":
    # file change
    replace_files()

    # app run
    launch_mirroring_app()
