import csv as csv
import nibabel as nib
import numpy as np
import pandas as pd

def combine_rois(in_csv, dict_csv, key_var = 'MRID', roi_prefix = 'MUSE_',  out_csv):
    '''
    Calculates a dataframe with the volumes of derived rois.
    '''

    # Read input files
    df_in = pd.read_csv(in_csv, dtype = {'MRID':str})
    
    ## Read derived roi map file to a dictionary
    dict_roi = {}
    with open(dict_csv) as roi_map:
        reader = csv.reader(roi_map, delimiter=',')
        for row in reader:
            key = roi_prefix + str(row[0])
            val = [roi_prefix + str(x) for x in row[2:]]
            dict_roi[key] = val

    ## Create derived roi df
    label_names = list(dict_roi.keys())
    df_out = df_in[[key_var]].copy()
    df_out = df_out.reindex(columns = [key_var] + label_names)

    # Calculate volumes for derived rois
    for i, key in enumerate(dict_roi):
        key_vals = dict_roi[key]
        try:
            df_out[key] = df_in[key_vals].sum(axis=1)
        except:
            df_out = df_out.drop(columns = key)
        
    ## Save df_out
    df_out.to_csv(out_csv, index = False)


if __name__ == "__main__":
    # Access arguments from command line using sys.argv
    if len(sys.argv) != 6:
        print("Error: Please provide all required arguments")
        print("Usage: python combine_rois.py in_csv.csv dict_csv.csv key_var roi_prefix out_csv.csv")
        sys.exit(1)

    in_csv = sys.argv[1]
    var_name = sys.argv[2]
    min_val = int(sys.argv[3])
    max_val = int(sys.argv[4])
    out_csv = sys.argv[5]

    # Call the function
    combine_rois(in_csv, dict_csv, key_var, roi_prefix, out_csv)

    print("Derived roi calculation complete! Output file:", out_csv)
