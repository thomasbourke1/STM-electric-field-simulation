#import modules

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import re
from scipy.ndimage import gaussian_filter

# Specify the directory

def generate_file_lists(directory):
    """Generate lists of files in a directory with E_x and E_z

    Args:
        directory (str): file directory, eg. 'COMSOL_data/feedback_off/'
    Returns:
        x_files, z_files (array): Array of file names
    """

    # directory = 'COMSOL_data'
    # current = 400 # current set point for this dataset -> may change

    z_files = []
    x_files = []

    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        # Check if it's a file (not a subdirectory)
        if os.path.isfile(file_path):
            if 'pulse_x.txt' in file_path:
                x_files.append(file_path)
            if 'pulse_z.txt' in file_path:
                z_files.append(file_path)
    
    # sort arrays in ascending voltage
    x_files = sorted(x_files, key=lambda x: int(re.search(r'(\d+)V', x).group(1)))
    z_files = sorted(z_files, key=lambda x: int(re.search(r'(\d+)V', x).group(1)))
    
    return x_files, z_files


#Plot E_z data

def plot_Ez(z_files, feedback, free_param):
    """Plot Ez as a function of distance across the sample

    Args:
        z_files (array): list of files to read over
        feedback (_type_): _description_
        free_param (_type_): _description_
    """

    
    if feedback == 'on':
        current = free_param # current in pA
    if feedback == 'off':
        height = free_param # height in angstrom
    
        
    plt.figure(figsize=(6, 5))
    plt.rcParams.update({
        'axes.labelsize': 14,    # Axis labels font size
        'xtick.labelsize': 12,   # X-tick labels font size
        'ytick.labelsize': 12,   # Y-tick labels font size
        'axes.titlesize': 16     # Title font size
    })

    for file in z_files:
        df = pd.read_csv(file, delimiter='\t')
        # voltage = file.split('/')[1].split('V')[0]
        voltage = re.search(r'(\d+)V', file).group(1)

        df[['Distance', 'E_field']] = df['% Model:              STM_tip.mph'].str.split(' ', 1, expand=True)
        df = df[7:]

        df['Distance'] = pd.to_numeric(df['Distance'])
        df['E_field'] = pd.to_numeric(df['E_field'])

        # Create the plot
        plt.plot(df['Distance'], abs(df['E_field']), marker='', linestyle='-', label=f'{voltage}V')
        
        # Add titles and labels
        if feedback == 'on':
            plt.title(f'Electric field E$_z$, I$_s$ = {current}pA, feedback {feedback}')
        if feedback == 'off':
            plt.title(f'Electric field E$_z$, $z$ = {height}$\AA$, feedback {feedback}')
            
        #scale limitations
        plt.ylim(0,6) 
        # plt.xlim()
        
        
        plt.xlabel('Distance nm') # axis labels
        plt.ylabel('$E_z$ V/nm')
        # plt.xlim(20, 30)
        plt.legend(fontsize=14)
        plt.grid(True)
