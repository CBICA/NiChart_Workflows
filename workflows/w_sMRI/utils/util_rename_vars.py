import pandas as pd
import argparse
import json
import sys

def select_sample(in_csv, rename_vars, out_csv):
    """
    Filters data based on json data
    """
    
    # Read input files
    df = pd.read_csv(in_csv)

    # Select fields
    df_out = df.copy()
    df_out.columns = rename_vars
    
    # Write out file
    df_out.to_csv(out_csv, index=False)

if __name__ == "__main__":
    # Access arguments from command line using sys.argv
    if len(sys.argv) != 4:
        print("Error: Please provide all required arguments")
        print("Usage: python select_sample.py in_csv.csv in_filter.json out_csv.csv")
        sys.exit(1)

    in_csv = sys.argv[1]
    rename_vars = sys.argv[2]
    out_csv = sys.argv[3]

    list_rename_vars = rename_vars.split(',')

    # Call the function
    select_sample(in_csv, list_rename_vars, out_csv)

    print("Variable selection complete! Output file:", out_csv)

