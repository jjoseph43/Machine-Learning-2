# Example Python code to read CSV file format

# The attached example Python code can be used to load the CSV files
# into a Pandas DataFrame object for processing in popular machine
# learning frameworks like Tensorflow or PyTorch.

import pandas as pd
import numpy as np

col_names = [
    "hwid",
    "idx",
    "x",
    "y",
    "z",
    "r",
    "eta",
    "phi",
    "raw",
    "pid",
    "n",
    "truth_eta",
    "truth_phi",
    "truth_pt",
    "trk_good",
    "trk_barcode",
    "trk_pt",
]

col_dtype = {
    "hwid": np.int64,
    "idx": np.int32,
    "x": np.float32,
    "y": np.float32,
    "z": np.float32,
    "r": np.float32,
    "eta": np.float32,
    "phi": np.float32,
    "raw": np.float32,
    "pid": np.int32,
    "n": np.int32,
    "truth_eta": np.float32,
    "truth_phi": np.float32,
    "truth_pt": np.float32,
    "trk_good": np.float32,
    "trk_barcode": np.float32,
    "trk_pt": np.float32,
}

filename = "zej/4e1c143b-728f-44fd-b553-f1000c23bebb_nevts1_evtid00000005_graphcnn_1l_0j.csv"
data = pd.read_csv(filename, header=None, names=col_names, dtype=col_dtype, sep="\t")
