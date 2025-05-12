from dotenv import load_dotenv
import os

load_dotenv()

# Define the root path of the project dynamically
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

region = os.getenv("local_path")

