import numpy as np
import pandas as pd
import os
from tqdm import tqdm
import argparse
import pathlib

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--train_dir', type=pathlib.Path, required=True)
    parser.add_argument('--output_dir', type=pathlib.Path, required=True)

    args = parser.parse_args()
    train_path = args.train_dir
    out_path = args.output_dir

    train_files = os.listdir(train_path)

    points = []
    for npy_file in tqdm(train_files):
        fpath = os.path.join(train_path, npy_file)
        sig = np.load(fpath)
        points.extend(list(sig))
    p_array = np.array(points)
    a = np.mean(p_array)
    b = np.std(p_array)

    norm_npy = np.array([a,b])
    savepath = os.path.join(out_path, 'norm.npy')
    np.save(savepath, norm_npy)
