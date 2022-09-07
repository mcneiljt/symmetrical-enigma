import pandas as pd
import os
import pyarrow.orc

df = pd.read_orc('./pretend.orc')
result = df[df[COL].str.contains('|'.join(FILTER))]
result.to_orc('.pretend_result.orc')
