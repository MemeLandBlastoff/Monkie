
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

print(os.getenv("DISCORD_TOKEN"))
print(os.getenv("COMBINED"))