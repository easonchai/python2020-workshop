# MAIN FILE
# This is what we are going to interact with! You can think of this file as the conductor in an orchestra
# It imports all the other files and plays them only when needed

import setup, encryption, scraper
from os import path # This is important to read the config.ini
import json 

