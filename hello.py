from datetime import datetime
import sys

if len(sys.argv) < 2:
    print("Usage: python3 hello.py <name>")
    sys.exit(1)

name = sys.argv[1]
current_time = datetime.now().astimezone()

print(f"Hello {name}, right now the time is {current_time}")
