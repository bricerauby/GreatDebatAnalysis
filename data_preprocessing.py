import argparse
import numpy as np 

import pandas as pd 

parser = argparse.ArgumentParser()    
parser.add_argument('--raw_data_path', required=True, 
                    type=str,help = 'path to the raw data')
parser.add_argument('--output_path', required=True, 
                    type=str, help = 'path to the output file')
args = parser.parse_args()

raw_data = pd.read_csv(args.raw_data_path)

# We select only the question we are interested in 
data = raw_data[['authorZipCode',"QUXVlc3Rpb246MTYw - Quel est aujourd'hui pour vous le problème concret le plus important dans le domaine de l'environnement ?","QUXVlc3Rpb246MTYx - Que faudrait-il faire selon vous pour apporter des réponses à ce problème ?"]]

no_na = data.dropna()
no_na[no_na.columns[2]] = no_na[no_na.columns[2]].apply(lambda x : x if len(x) > 200 else np.nan )
col_names = {
    no_na.columns[0]: 'zip_code',
     no_na.columns[1]: 'problem',
     no_na.columns[2]: 'solution'
}
clean_data = no_na.dropna()
clean_data = clean_data.rename(columns=col_names)
clean_data.to_csv(args.output_path)