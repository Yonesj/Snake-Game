# This script loads configuration data from a JSON file and assigns the values to variables.
# The variables represent various constants used in the program.
import json

# Load configuration data from JSON file
with open(r"..\config.json") as config_file:
    data = json.loads(config_file.read())

# Assign configuration data to variables
back_color:  tuple = data['back_color']
fruit_color: tuple = data['fruit_color']
block_color: tuple = data['block_color']
cell_size:   int   = data['cell_size']
block_cells: list  = data['block_cells']
table_size:  int   = data['table_size']
height:      int   = data['height']
width:       int   = data['width']
snakes:      list  = data['snakes']
sx:          int   = data['sx']
sy:          int   = data['sy']
id:          int   = data['id']
