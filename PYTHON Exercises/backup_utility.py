import shutil
import os

def backup_files(src, dest):
    try:
        # Create backup folder if it does not exist
        os.makedirs(dest, exist_ok=True)

        # Store existing backup files in a set
        existing_files = set(os.listdir(dest))

        # Open log file
        with open("backup.log", "a") as log_file:

            # Check files in source folder
            for file in os.listdir(src):

                source_path = os.path.join(src, file)
                dest_path = os.path.join(dest, file)

                # Copy only if file is not already present
                if file not in existing_files:

                    # Copy file
                    shutil.copy(source_path, dest_path)

                    # Log copied file
                    log_file.write(f"Copied: {file}\n")

                else:
                    # Log skipped duplicate
                    log_file.write(f"Skipped duplicate: {file}\n")

        print("Backup completed successfully")

    except FileNotFoundError:
        print("Error: Folder not found")

    except PermissionError:
        print("Error: Permission denied")


# Function call
backup_files("source", "backup")