import pandas as pd
import argparse
import json
import sys

def select_vars_by_suffix(in_csv, key_var, suffix, out_csv):

    """
    Select variables from data file based on suffix
    """
    
    # Read input files
    df = pd.read_csv(in_csv, dtype = {'MRID':str})

    # Convert columns of dataframe to str (to handle numeric ROI indices)
    df.columns = df.columns.astype(str)

    # Get variables (input var list + rois)
    sel_vars = [key_var] + df.columns[df.columns.str.contains(suffix)].tolist()
    
    # Select variables
    df_out = df[sel_vars]

    # Write out file
    df_out.to_csv(out_csv, index=False)

if __name__ == "__main__":
    # Access arguments from command line using sys.argv
    if len(sys.argv) != 5:
        print("Error: Please provide all required arguments")
        print("Usage: python select_vars_by_suffix.py in_csv key_var suffix out_csv")
        sys.exit(1)

    in_csv = sys.argv[1]
    key_var = sys.argv[2]
    suffix = sys.argv[3]
    out_csv = sys.argv[4]

    # Print run command
    print('About to run: ' + ' '.join(sys.argv))

    # Call the function
    select_vars_by_suffix(in_csv, key_var, suffix, out_csv)

    print("Selection of variables complete! Output file:", out_csv)

