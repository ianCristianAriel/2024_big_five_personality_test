# BSD 2-Clause License
# Copyright (c) 2024, Ian Cristian Ariel, Yané
# All rights reserved.
#
# This file is part of a project licensed under the BSD 2-Clause License.
# See the LICENSE file for more information.

# <------------------------------------------------------------------------------------------------------------------------------->

# <-- import libraries -->
# System libraries 
import os

# Data viz libraries
from matplotlib import pyplot as plt
import seaborn as sns
    

# <-- Definition common constants -->
RANDOM_STATE = 27
NUMBER_SAMPLES = 9

# dotenv file path
ENV_FILE_PATH = "/Users/cristianariel/Desktop/Progreso/Codigo/Permanentes/cinco_grandes_rasgos_personalidad/.env"

# Set path to data folder
BASE_PATH = "/Users/cristianariel/Desktop/Progreso/Codigo/Permanentes/cinco_grandes_rasgos_personalidad"
DATA_PATH = os.path.join(BASE_PATH, 'data')
RAW_DATASETS = os.path.join(DATA_PATH, 'raw')
PROCESSED_DATASETS = os.path.join(DATA_PATH, 'processed')

# kaggle repository dataset URL
KAGGLE_DATASET_URL = "tunguz/big-five-personality-test"

# Set path to models folder
MODELS_PATH = os.path.join(BASE_PATH, 'models')

# <-- Configure initial parameters of matplotlib to standardize the plots -->
# Apply the configuration
"""Configure matplotlib with predefined parameters."""
plt.style.use('tableau-colorblind10')
params = {
        'figure.figsize': (16, 10),  # Set the size of each plot
        'figure.dpi': 80,  # Set the resolution per inch
        'figure.facecolor': 'white',  # Define the background color
        'figure.edgecolor': 'white',  # Define the edge color
        'figure.frameon': True,  # Keep the plot frame enabled
        'figure.constrained_layout.use': False,  # Disable constrained layout for figures
        'figure.constrained_layout.h_pad': 0.04167,  # Horizontal padding in constrained layout
        'figure.constrained_layout.w_pad': 0.04167,  # Vertical padding in constrained layout
        'axes.labelsize': 12,  # Set the size of axis labels
        'axes.titlesize': 14,  # Set the size of the title
        'axes.labelweight': 'normal',  # Set the font weight of axis labels
        'xtick.labelsize': 10,  # Define the size of x-axis labels
        'ytick.labelsize': 10,  # Define the size of y-axis labels
        'xtick.color': 'black',  # Set the color of x-axis labels
        'ytick.color': 'black',  # Set the color of y-axis labels
        'axes.spines.top': True,  # Keep the top spine of the plot visible
        'axes.spines.right': True,  # Keep the right spine of the plot visible
        'legend.frameon': True,  # Keep the legend frame visible
        'grid.linestyle': '-',  # Define the style of grid lines
        'grid.linewidth': 0.8,  # Set the width of grid lines
        'grid.color': 'gray',  # Set the color of grid lines
        'legend.fontsize': 10,  # Set the font size of the legend
        'axes.titleweight': 'normal',  # Set the font weight of the title
        'axes.titlecolor': 'black',  # Set the color of the title
        'axes.titlelocation': 'center',  # Place the title in the center of the plot
    }
plt.rcParams.update(params)