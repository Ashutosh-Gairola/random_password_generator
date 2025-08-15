import random
import subprocess
from datetime import datetime

# repo_dir = "/home/ashu/Project/main_acc/random_password_generator"

# Generate random number between 32-bit and 64-bit range
number = random.randint(2**31, 2**63 - 1)

# Current timestamp in ISO format
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Append to file
with open(f"numbers.txt", "a") as f:
    f.write(f"1.-->{timestamp} - {number}\n")

# Git commands
# subprocess.run(["git", "-C", repo_dir, "add", "numbers.txt"])
# subprocess.run(["git", "-C", repo_dir, "commit", "-m", f"Add number {number} at {timestamp}"])
# subprocess.run(["git", "-C", repo_dir, "push"])
