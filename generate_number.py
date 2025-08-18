import random
import subprocess
from datetime import datetime
import logging

repo_dir = "/home/ashu/Project/main_acc/random_password_generator"

# Configure logging
log_file = f"{repo_dir}/script.log"
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Log the last run date
logging.info("Script executed.")

# Generate random number between 32-bit and 64-bit range
number = random.randint(2**31, 2**63 - 1)
logging.info(f"Generated number: {number}")

# Current timestamp in ISO format
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
logging.info(f"Current timestamp: {timestamp}")

# Append to file
with open(f"{repo_dir}/numbers.txt", "a") as f:
    f.write(f"by pc {timestamp} - {number}\n")

# Git commands

subprocess.run(["git", "-C", repo_dir, "add", "-A"])
subprocess.run(["git", "-C", repo_dir, "commit", "-m", f"Add number {number} at {timestamp}"])
subprocess.run(["git", "-C", repo_dir, "push"])
