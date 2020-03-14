# GreatDebatAnalysis
GreatDebatAnalysis

This repository contains the code necessary to replicate the results exposed in the report (available on demand).

The original data used from the GDN are available [here](http://opendata.auth-6f31f706db6f4a24b55f42a6a79c5086.storage.sbg.cloud.ovh.net/2019-03-21/LA_TRANSITION_ECOLOGIQUE.csv). 

this can be preprocess with the data_preporcessing.py file ```python data_processing.py --raw_data_path=<path_to_LA_TRANSITION_ECOLOGIQUE.csv>  --output_path=<dataset_1.csv>  ``` 

In the notebook the preprocessed dataset is called "dataset_1.csv"

The annotated dataset is available [here](https://drive.google.com/open?id=1K1-lzE6vvhc6UZR_5y2O1oZ0RUuDjqbC) under the filename "annotated_data.csv" (some other files are also available on this drive, useful to replicate the map, or the study with Insee value)
