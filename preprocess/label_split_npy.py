import os
import numpy as np
from tqdm import tqdm
import argparse
import pathlib
import pandas as pd

if __name__== "__main__":
    # Arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--tsv_dir', type=pathlib.Path, required=True, help='Path to directory containing tsv files')
    parser.add_argument('--npy_dir', type=pathlib.Path, required=True, help='Path to directory containing npy files')
    parser.add_argument('--output_dir', type=pathlib.Path, required=True, help='Path to input directory')    
    parser.add_argument('--num_window', type=int, choices=[1,3], required=True, help='Number of windows to use')

    # Read arguments
    args = parser.parse_args()
    tsv_dir = args.tsv_dir
    npy_dir = args.npy_dir
    output_dir = args.output_dir
    num_window = args.num_window

    # Make directories for output
    os.makedirs(output_dir, exist_ok=True)

    # List input files
    raw_files = os.listdir(tsv_dir)
    tsv_files = [x for x in raw_files if '.tsv' in x]
    npy_files = os.listdir(npy_dir)

    # Loop through tsv files, extract labels, and split npy files
    for tfile in tqdm(tsv_files):
        # load data
        recid = tfile.split('.')[0]
        tdata = pd.read_csv(os.path.join(tsv_dir, tfile), delimiter='\t')
        eeg_array = np.load(os.path.join(npy_dir, recid+'.npy'))
        # process dataframe
        subdf = tdata[tdata['description'].str.contains('stage')].reset_index(drop=True)
        stages = list(subdf['description'])
        stages = [x[-1] for x in stages]
        onsets = list(subdf['onset'])
        durations = list(subdf['duration'])
        # Process array and save
        wcnt = 0
        rcnt = 0
        n1cnt = 0
        n2cnt = 0
        n3cnt = 0
        for idx, stg in enumerate(stages):
            dur = durations[idx]
            onset = onsets[idx]
            if (stg in ['W','1','2','3','R'])&(dur==30):
                if num_window==3:
                    startind = int((onset-30)*256)
                    endind = startind + 90*256
                else:
                    startind = onset*256
                    endind = onset+30*256
                subarray = eeg_array[startind:endind]
                if stg == 'W':
                    savename = recid + '_W_' + str(wcnt)
                    wcnt+=1
                elif stg == '1':
                    savename = recid + '_N1_' + str(n1cnt)
                    n1cnt+=1
                elif stg == '2':
                    savename = recid + '_N2_' + str(n2cnt)
                    n2cnt+=1
                elif stg == '3':
                    savename = recid + '_N3_' + str(n3cnt)
                    n3cnt+=1
                elif stg == 'R':
                    savename = recid + '_R_' + str(rcnt)
                    rcnt+=1
                savepath = os.path.join(output_dir, savename+'.npy')
                np.save(savepath, subarray)
