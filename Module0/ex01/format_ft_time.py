import time
from datetime import datetime

timestamp = time.time()
now = datetime.now()


regular_format = f"{timestamp:,.4f}"
scientific_format = f"{timestamp:.2e}"

print(f"Seconds since January 1, 1970: {regular_format} or {scientific_format} in scientific notation")
now = datetime.fromtimestamp(timestamp)
print(now.strftime("%b %-d %Y"))