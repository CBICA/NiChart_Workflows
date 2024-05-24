import pandas as pd
import sys
import os

def combine_data(out_csv, list_in_csv):
    """
    Combines multiple input data files
    """
    
    key_var = 'MRID'
    
    in_csv = list_in_csv[0]
    df_out = pd.read_csv(in_csv)

    ## Rename spare score
    s1 = os.path.basename(in_csv).split('.')[0]
    sname = 'SPARE_' + s1.split('_')[3] + '_' + s1.split('_')[1]
    
    df_out = df_out[['MRID', 'SPARE_score']]
    df_out.columns = ['MRID', sname]
    
    for i, in_csv in enumerate(list_in_csv[1:]):
        # Read csv files
        df_tmp = pd.read_csv(in_csv)
        df_tmp = df_tmp[df_tmp[key_var].isna()==False]
        
        ## Rename spare score
        s1 = os.path.basename(in_csv).split('.')[0]
        sname = 'SPARE_' + s1.split('_')[3] + '_' + s1.split('_')[1]

        df_tmp = df_tmp[['MRID', 'SPARE_score']]
        df_tmp.columns = ['MRID', sname]

        # Merge DataFrames
        df_out = df_out.merge(df_tmp, on = key_var)

    # Write out file
    df_out.to_csv(out_csv, index=False)
        
if __name__ == "__main__":
  # Access arguments from command line using sys.argv
  if len(sys.argv) < 3:
      print("Error: Please provide all required arguments")
      print("Usage: python combine_data.py out_csv.csv in_csv1.csv,in_csv2.csv,...")
      sys.exit(1)

  out_csv = sys.argv[1]
  list_in_csv = sys.argv[3:]
  
  # Call the function
  combine_data(out_csv, list_in_csv)

  print("Merge complete! Output file:", out_csv)
