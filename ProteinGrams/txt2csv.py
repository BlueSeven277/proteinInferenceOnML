import numpy as np
import pandas as pd

txt = np.loadtxt('ret_sigma_list.txt')
txtDF = pd.DataFrame(txt)
txtDF.to_csv('sigma_features.csv', index=False)