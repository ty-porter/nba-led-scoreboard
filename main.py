from datetime import datetime, timedelta
from data.scoreboard_config import ScoreboardConfig
from renderer.main import MainRenderer
from RGBMatrixDriver import RGBMatrix, RGBMatrixOptions, prefilled_matrix_options
from utils import args
from data.data import Data
import debug

SCRIPT_NAME = "NBA Scoreboard"
SCRIPT_VERSION = "1.0.0"

# Check for led configuration arguments
command_line_args = args()

# Initialize the matrix
matrix = RGBMatrix(options=prefilled_matrix_options(command_line_args))

# Print some basic info on startup
debug.info("{} - v{} ({}x{})".format(SCRIPT_NAME, SCRIPT_VERSION, matrix.width, matrix.height))

# Read scoreboard options from config.json if it exists
config = ScoreboardConfig("config", args)
debug.set_debug_status(config)

data = Data(config)

MainRenderer(matrix, data).render()