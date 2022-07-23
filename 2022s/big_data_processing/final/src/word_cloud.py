from matplotlib import pyplot as plt
from wordcloud import WordCloud
from prepare_data import get_word_merged_df
import Mecab

data = get_word_merged_df()

print(data)

m = Mecab.Tagger('')
parsed = m.parse(data)