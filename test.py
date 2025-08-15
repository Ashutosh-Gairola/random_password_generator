import random
from datetime import datetime

number = random.randint(2**31, 2**63 - 1)
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("numbers.txt", "a") as f:
    f.write(f"{timestamp} - {number}\n")
