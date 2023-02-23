import os
import numpy as np
import mne
from tqdm import tqdm
import argparse
import pathlib

if __name__== "__main__":
    # Arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_dir', type=pathlib.Path, required=True, help='Path to input directory')
    parser.add_argument('--output_dir', type=pathlib.Path, required=True, help='Path to input directory')
    parser.add_argument('--channel', type=str, default='EEG F3-M2')

    # Read arguments
    args = parser.parse_args()
    input_dir = args.input_dir
    output_dir = args.output_dir
    channel = args.channel

    # Make directories for output
    outpath = os.path.join(output_dir, channel)
    os.makedirs(outpath, exist_ok=True)

    # List EDF files
    raw_files = os.listdir(input_dir)
    edf_files = [x for x in raw_files if '.edf' in x]

    # Loop through edf files and extract given channel
    for rec in tqdm(edf_files):
        # Load edf
        edfpath = os.path.join(input_dir, rec)
        rawedf = mne.io.read_raw_edf(edfpath, verbose=False)
        # Check if channel is in edf file
        edf_channels = rawedf.ch_names
        if channel in edf_channels:
            raw_eeg = rawedf[channel][0][0]
            savename = rec.split('.')[0]
            savepath = os.path.join(outpath, savename)
            np.save(savepath, raw_eeg)