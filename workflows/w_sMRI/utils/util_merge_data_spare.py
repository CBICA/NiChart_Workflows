import pandas as pd
import sys

def merge_data(out_csv, key_var, list_in_csv):
    """
    Merge multiple input data files
    Output data includes an inner merge
    """
    
    df_out = pd.read_csv(list_in_csv[0])
    for i, in_csv in enumerate(list_in_csv[1:-1]):
        # Read csv files
        df_tmp = pd.read_csv(in_csv)
        df_tmp = df_tmp[df_tmp[key_var].isna()==False]

        # Merge DataFrames
        df_out = df_out.merge(df_tmp, on = key_var)

    ## FIXME
    ## Update columns
    vlist = ['CorpusCallosum', 'Frontal_WM_L', 'Frontal_WM_R', 'Occipital_WM_L', 'Occipital_WM_R', 'Parietal_WM_L', 'Parietal_WM_R', 'Temporal_WM_L', 'Temporal_WM_R']
    
    for tvar in vlist:
        if tvar in df_out:
            df_out[tvar + '.1'] = df_out[tvar]

    ## FIXME
    ## Add ICV
    dftmp = pd.read_csv(list_in_csv[2])
    dftmp = dftmp[['MRID','ICV']]
    if 'ICV' not in df_out.columns:
        df_out = df_out.merge(dftmp, on='MRID')

    ## FIXME
    ## Drop study
    df_out = df_out.drop(columns='Study')
    
    # Write out file
    df_out.to_csv(out_csv, index=False)
        
if __name__ == "__main__":
  # Access arguments from command line using sys.argv
  if len(sys.argv) < 4:
      print("Error: Please provide all required arguments")
      print("Usage: python merge_data.py out_csv.csv key_var in_csv1.csv,in_csv2.csv,...")
      sys.exit(1)

  out_csv = sys.argv[1]
  key_var = sys.argv[2]
  list_in_csv = sys.argv[3:]
  
  # Call the function
  merge_data(out_csv, key_var, list_in_csv)

  print("Merge complete! Output file:", out_csv)
