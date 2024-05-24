import pandas as pd
import argparse
import json
import sys

def select_vars_harmonize(in_csv, in_rois, sel_vars, out_csv):
    """
    Filters data based on json data
    """
    
    # Read input files
    df = pd.read_csv(in_csv)
    dfr = pd.read_csv(in_rois)

    # Remove suffix from harmonized vars
    df.columns = df.columns.str.replace('_HARM', '')

    # Convert columns of dataframe to str (to handle numeric ROI indices)
    df.columns = df.columns.astype(str)

    # Get variable lists (input var list + rois)
    roi_vars = dfr.Name.astype(str).tolist()

    # Remove roi vars not in dataframe
    df_vars = df.columns.tolist()    
    roi_vars = [x for x in roi_vars if x in df_vars]
    

    # Remove duplicate vars (in case a variable is both in roi list and input var list)
    sel_vars = [x for x in sel_vars if x not in roi_vars]
    
    # Make a list of selected variables
    sel_vars = sel_vars + roi_vars 


    # Select fields
    df_out = df[sel_vars]
    
    # Write out file
    df_out.to_csv(out_csv, index=False)

if __name__ == "__main__":
    # Access arguments from command line using sys.argv
    if len(sys.argv) != 5:
        print("Error: Please provide all required arguments")
        print("Usage: python select_vars_harmonize.py in_csv.csv in_rois.csv sel_vars out_csv.csv")
        sys.exit(1)

    in_csv = sys.argv[1]
    in_rois = sys.argv[2]    
    sel_vars = sys.argv[3]
    out_csv = sys.argv[4]

    sel_vars = sel_vars.split(',')

    # Call the function
    select_vars_harmonize(in_csv, in_rois, sel_vars, out_csv)

    print("Variable selection complete! Output file:", out_csv)

