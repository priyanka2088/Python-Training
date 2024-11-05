import pandas as pd
seriesa=pd.Series([11,12,13,14,15,23])
print(seriesa.head())
print(seriesa.tail(2))
seriesb=pd.Series([11,21,31,41,51,61],index=list('abcdef'))
print(seriesb)
print(seriesb.loc['c'])
print(seriesb.iloc[2])
print(seriesb.loc[:'e'])
print(seriesb.loc['a':'d'])

