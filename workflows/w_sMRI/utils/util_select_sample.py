import pandas as pd
import argparse
import json
import sys

def select_sample(in_csv, in_sample, in_rois, in_vars, out_csv):

    """
    Select data based on list of samples and variables
    """
    
    # Read input files
    df = pd.read_csv(in_csv)
    if in_sample != 'None':
        dfs = pd.read_csv(in_sample)
    if in_rois != 'None':
        dfr = pd.read_csv(in_rois)
    
    # Make a list of selected variables
    sel_vars = in_vars.split(',')
    sel_vars_renamed = in_vars.split(',')
    if in_rois != 'None':
        sel_vars = sel_vars + dfr.Index.astype(str).tolist()
        sel_vars_renamed = sel_vars_renamed + dfr.Name.tolist()
    in_key = sel_vars[0]
    
    # Select variables and rename them (ROI index renamed with ROI name)
    df_out = df[sel_vars]
    df_out.columns = sel_vars_renamed

    # Select sample
    if in_sample != 'None':
        df_out = dfs.merge(df_out, on = in_key)
    
    # Write out file
    df_out.to_csv(out_csv, index=False)

if __name__ == "__main__":
    # Access arguments from command line using sys.argv
    if len(sys.argv) != 6:
        print("Error: Please provide all required arguments")
        print("Usage: python select_sample.py in_csv.csv in_sample.csv in_rois.csv in_vars out_csv.csv")
        sys.exit(1)

    in_csv = sys.argv[1]
    in_sample = sys.argv[2]
    in_rois = sys.argv[3]
    in_vars = sys.argv[4]
    out_csv = sys.argv[5]

    # Call the function
    select_sample(in_csv, in_sample, in_rois, in_vars, out_csv)

    print("Sample selection complete! Output file:", out_csv)

