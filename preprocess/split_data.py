import os
import shutil
import random
import string
import argparse
from tqdm import tqdm
import pathlib
import pandas as pd

if __name__== "__main__":
    # Arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_dir', type=pathlib.Path, required=True, help='Path to input directory')
    parser.add_argument('--output_dir', type=pathlib.Path, required=True, help='Path to output directory')

    # Read arguments
    args = parser.parse_args()
    input_dir = args.input_dir
    output_dir = args.output_dir

    # Make directories for train and test dataset
    train_dir = os.path.join(output_dir, 'train')
    test_dir = os.path.join(output_dir, 'test')
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)

    # List npy files
    npyfiles = os.listdir(input_dir)
    
    # Rename files and split train/test
    original_fname = []
    encoded_fname = []
    isTrain = []

    characters = string.ascii_letters + string.digits
    random.seed(2022)

    for npyfile in tqdm(npyfiles):
        # Make random name
        newid = ''.join(random.choice(characters) for i in range(10))
        while newid+'.npy' in encoded_fname:
            newid = ''.join(random.choice(characters) for i in range(10))
        newid = newid+'.npy'
        # Randomly select train or test
        random_number = random.uniform(0,1)
        if random_number < 0.2: #test
            filedst = os.path.join(test_dir, newid)
            split=False
        else: #train
            filedst = os.path.join(train_dir, newid)
            split=True
        # Move files
        filesrc = os.path.join(input_dir, npyfile)
        shutil.copy(filesrc, filedst)
        # Store info
        original_fname.append(npyfile)
        encoded_fname.append(newid)
        isTrain.append(split)

    # compile info as dataframe
    keydf = pd.DataFrame({'file_id':original_fname, 'encoded_id':encoded_fname, 'train':isTrain})
    keydf.to_csv(os.path.join(output_dir, 'keydf.csv'), index=False)

    # Save train labels
    traindf = keydf[keydf.train==True].reset_index(drop=True)
    fnames = list(traindf['file_id'])
    fstages = [x.split('_')[2] for x in fnames]
    traindf = traindf.drop(columns=['file_id','train'])
    traindf['stage'] = fstages
    traindf = traindf.rename(columns={'encoded_id':'rec_id'})
    traindf.to_csv(os.path.join(output_dir, 'train_labels.csv'), index=False)
