import random
import subprocess
import os
import shutil
from datetime import datetime
import logging
import time
from pytz import timezone

repo_dir = "/home/ashu/Project/main_acc/random_password_generator"

# Configure logging
log_file = f"{repo_dir}/cron.log"
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Marker file to track state
marker_file = os.path.join(repo_dir, ".toggle_state")

# Decide action
if not os.path.exists(marker_file):
    action = "create"
    last_count = 0
else:
    with open(marker_file, "r") as f:
        content = f.read().strip().split(",")
    last_action = content[0]
    last_count = int(content[1]) if len(content) > 1 else 0
    action = "delete" if last_action == "create" else "create"


if action == "create":
    # Pick random number of folders between 1 and 10,000
    folder_count = random.randint(1, 10)
    # logging.info(f"Creating {folder_count} folders")

    for i in range(1, folder_count + 1):
        folder = os.path.join(repo_dir, f"folder_{i}")
        os.makedirs(folder, exist_ok=True)
        file_path = os.path.join(folder, "text-1")

        # Generate random 32–64 bit number
        number = random.randint(2**31, 2**63 - 1)
        with open(file_path, "w") as f:
            f.write(f"{number}\n")

        # if i <= 5 or i == folder_count:  # log only first 5 and last
            # logging.info(f"Created {file_path} with number {number}")

    # Save state with count
    with open(marker_file, "w") as f:
        f.write(f"create,{folder_count}")

elif action == "delete":
    # logging.info(f"Deleting {last_count} folders")
    for i in range(1, last_count + 1):
        folder = os.path.join(repo_dir, f"folder_{i}")
        if os.path.exists(folder):
            shutil.rmtree(folder)
            # if i <= 5 or i == last_count:
            #     logging.info(f"Deleted {folder}")

    # Save state with count=0
    with open(marker_file, "w") as f:
        f.write("delete,0")

# Git commit/push
subprocess.run(["git", "-C", repo_dir, "add", "-A"])
time.sleep(5)  # Ensure timestamp is different
ist = timezone('Asia/Kolkata')
commit_msg = f"{action.capitalize()} folders at {datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')}"
time.sleep(6)  # Ensure timestamp is different
subprocess.run(["git", "-C", repo_dir, "commit", "-m", commit_msg])
time.sleep(7)  # Ensure timestamp is different
subprocess.run(["git", "-C", repo_dir, "push"])
logging.info(f"{commit_msg}")
print("done")