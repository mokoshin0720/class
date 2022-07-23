from matplotlib import pyplot as plt
from wordcloud import WordCloud
from prepare_data import get_score_df, get_word_merged_df
import MeCab

data = get_score_df()

text = ""
for index, row in data.iterrows():
    print('----------------------')
    print(row["テキスト"])
    text += row["テキスト"]

print(text)

m = MeCab.Tagger("-Owakati")
parsed = m.parse(text)
splitted = ' '.join([x.split('\t')[0] for x in parsed.splitlines()[:-1]])

print(splitted)
print(text)

fpath = "./ipaexg.ttf"
wordc = WordCloud(background_color='white', 
                    width=800, 
                    height=600, 
                    font_path=fpath,
                    ).generate(text)
wordc.to_file('wordcloud.png')