from dotenv import load_dotenv
import os

load_dotenv()

# Define the root path of the project dynamically
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

# Define paths for input and output directories relative to the root path
INPUT_DIR = os.path.join(ROOT_PATH, "data/input")
OUTPUT_DIR = os.path.join(ROOT_PATH, "data/output")

region = os.getenv("local_path")

