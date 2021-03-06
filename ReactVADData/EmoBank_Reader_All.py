import pandas as pd

path = r'C:\Users\jorda\Desktop\evaluations\EmoBank-master\EmoBank-master\corpus'
df_reader = pd.read_csv(path + r"\reader.csv", encoding='utf8')
df_raw = pd.read_csv(path + r"\raw.csv", encoding='utf8')
meta = pd.read_csv(path + r'\meta.tsv', sep='\t', index_col=0)

df = pd.merge(df_reader, df_raw, on='id',  how='left')
df = pd.merge(df, meta, on='id',  how='left')

df = df[df['text'].apply(lambda x: isinstance(x, str))]
df = df.sample(frac=1).reset_index(drop=True)

df.to_csv(r'.\ReactVADData\EmoBank_Reader_All.csv', index=False)
