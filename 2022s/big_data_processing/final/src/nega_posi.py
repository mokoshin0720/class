import pandas as pd
import pathlib
import jaconv

def get_posnega_df():
    p_dic = pathlib.Path('dic')

    for i in p_dic.glob("*.txt"):
        with open(i, 'r', encoding='cp932') as f:
            x = [ii.replace('\n', '').split(':') for ii in f.readlines()]

    posi_nega_df = pd.DataFrame(x, columns=['基本形', '読み', '品詞', 'スコア'])
    posi_nega_df['読み'] = posi_nega_df['読み'].apply(lambda x : jaconv.hira2kata(x))
    posi_nega_df = posi_nega_df[~posi_nega_df[['基本形', '読み', '品詞']].duplicated()]

    return posi_nega_df

df = get_posnega_df
print(df)