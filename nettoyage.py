import pandas as pd
data=pd.read_excel("datacv.xlsx")
data['projets']=data['projets'].fillna('NOT_FOUND')
data.to_excel('datacvnettoyé.xlsx', index=False)
print('done')