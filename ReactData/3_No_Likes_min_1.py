import pandas as pd
import os
import numpy as np


cols = ['name', 'love_count', 'wow_count',
        'haha_count', 'sad_count', 'angry_count']

df = pd.read_csv(r"C:\Users\jorda\Desktop\FB-Data\name_msg_desc_links_like_reacts\name_msg_desc_links_like_reacts.csv",
                 usecols=cols, encoding='utf16')

df['react_sum'] = df['love_count'] + df['wow_count'] + \
    df['haha_count'] + df['sad_count'] + df['angry_count']

df = df[df['react_sum'] > 1]

df = df.drop('react_sum', axis=1)

df = df[df['name'].apply(lambda x: isinstance(x, str))]

df_reacts = df.select_dtypes(include=[np.number])

df_reacts = df_reacts.div(df_reacts.sum(axis=1), axis=0)
df[df_reacts.columns] = df_reacts

shuffled_df = df.sample(frac=1).reset_index(drop=True)

shuffled_df.to_csv('3_No_Likes_min_1.csv', encoding='utf16', index=False)
