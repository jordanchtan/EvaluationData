import pandas as pd
import numpy as np

path = r'C:\Users\jorda\Desktop\FB-Data\name_msg_desc_links_like_reacts'
cols = ['name']

df = pd.read_csv(path + r"\name_msg_desc_links_like_reacts.csv",
                 usecols=cols, encoding='utf16')


np.savetxt('fb_corpus.txt', df, fmt='%s', encoding='utf16')
