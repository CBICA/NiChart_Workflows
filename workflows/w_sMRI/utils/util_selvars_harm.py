import pandas as pd
import argparse
import json
import sys

def selvars_harm(in_csv, in_rois, out_csv):
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
    
    # Make a list of selected variables
    sel_vars = ['MRID'] + roi_vars

    # Select fields
    df_out = df[sel_vars]
    
    # Write out file
    df_out.to_csv(out_csv, index=False)

if __name__ == "__main__":
    # Access arguments from command line using sys.argv
    if len(sys.argv) != 4:
        print("Error: Please provide all required arguments")
        print("Usage: python selvars_harm.py in_csv.csv in_rois.csv out_csv.csv")
        sys.exit(1)

    in_csv = sys.argv[1]
    in_rois = sys.argv[2]    
    out_csv = sys.argv[3]

    # Call the function
    selvars_harm(in_csv, in_rois, out_csv)

    print("Variable selection complete! Output file:", out_csv)

