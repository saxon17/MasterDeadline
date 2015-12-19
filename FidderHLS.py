import zipfile
import pandas as pd
zf = zipfile.ZipFile('test.zip', 'r')

html = zf.read("_index.htm")
df = pd.read_html(html)[0]
df2 = df.loc[:,['Body','URL','Content-Type']]
df2 = df2[df2['Content-Type'] == 'application/octet-stream']
df2['Dur'] = df2['URL'].apply(getDur)
df2['Itag'] = df2['URL'].apply(getItag)
df2['Rate'] = df2.Body*8/df2.Dur
df2