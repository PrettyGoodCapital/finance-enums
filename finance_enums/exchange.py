'''https://www.iso20022.org/sites/default/files/ISO10383_MIC/ISO10383_MIC.csv'''
import pandas as pd
import os
import os.path

_DF = pd.read_csv(os.path.join(__file__, 'data', 'mics.csv'))

MICS = set(_DF[''].values.tolist())
MICS_MAP = list(_DF[['MIC', 'NAME-INSTITUTION DESCRIPTION']].set_index('MIC').to_dict().values())[0]
