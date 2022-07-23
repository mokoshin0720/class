from pydoc import TextRepr
from tracemalloc import stop
from turtle import pos
from matplotlib import pyplot as plt
from wordcloud import WordCloud
from wordcloud import STOPWORDS
import MeCab
from prepare_data import get_score_df, get_word_merged_df

def wakati_text(tagger, select_conditions, text):
    node = tagger.parseToNode(text)
    terms = []

    while node:
        term = node.surface
        pos = node.feature.split(',')[0]

        if pos in select_conditions:
            terms.append(term)

        node = node.next

    text_result = ' '.join(terms)
    return text_result

def divide_words(df):
    pos_sentence = ""
    neg_sentence = ""
    for _, row in df.iterrows():
        if row['標準化スコア'] >= 0:
            pos_sentence += row['テキスト']
        else:
            neg_sentence += row['テキスト']

    tagger = MeCab.Tagger("")
    tagger.parse('')

    select_conditions = ['名詞', '形容詞']
    pos_words = wakati_text(
        tagger=tagger,
        select_conditions=select_conditions,
        text=pos_sentence
    )
    neg_words = wakati_text(
        tagger=tagger,
        select_conditions=select_conditions,
        text=neg_sentence
    )

    return pos_words, neg_words

data = get_score_df()

pos_words, neg_words = divide_words(data)

fpath = "./ipaexg.ttf"

stop_words = [
    '国葬',
    '安倍',
    'の',
    'ん',
    'これ',
    'こと',
]

for word in stop_words:
    STOPWORDS.add(word)

wordc = WordCloud(background_color='white', 
                    width=800, 
                    height=600, 
                    font_path=fpath,
                    ).generate(pos_words)
wordc.to_file('pos.png')

wordc = WordCloud(background_color='white', 
                    width=800, 
                    height=600, 
                    font_path=fpath,
                    ).generate(neg_words)
wordc.to_file('neg.png')