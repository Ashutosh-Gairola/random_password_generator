import random
import subprocess
import os
import shutil
from datetime import datetime
import logging

repo_dir = "/home/ashu/Project/main_acc/random_password_generator"

# Configure logging
log_file = f"{repo_dir}/script.log"
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Marker file to track whether to create or delete
marker_file = os.path.join(repo_dir, ".toggle_state")

# Determine action
if not os.path.exists(marker_file):
    action = "create"
else:
    with open(marker_file, "r") as f:
        last_action = f.read().strip()
    action = "delete" if last_action == "create" else "create"

logging.info(f"Script executed. Action: {action}")

# Perform action
if action == "create":
    for i in range(1, 25):  # 1 to 24
        folder = os.path.join(repo_dir, f"folder_{i}")
        os.makedirs(folder, exist_ok=True)
        file_path = os.path.join(folder, "text-1")

        number = random.randint(2**31, 2**63 - 1)
        with open(file_path, "w") as f:
            f.write(f"{number}\n")

        logging.info(f"Created {file_path} with number {number}")

elif action == "delete":
    for i in range(1, 25):
        folder = os.path.join(repo_dir, f"folder_{i}")
        if os.path.exists(folder):
            shutil.rmtree(folder)
            logging.info(f"Deleted {folder}")

# Save new state
with open(marker_file, "w") as f:
    f.write(action)

# Git commands
subprocess.run(["git", "-C", repo_dir, "add", "-A"])
commit_msg = f"{action.capitalize()} folders at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
subprocess.run(["git", "-C", repo_dir, "commit", "-m", commit_msg])
subprocess.run(["git", "-C", repo_dir, "push"])
