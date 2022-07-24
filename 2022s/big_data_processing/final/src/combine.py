import csv
import pathlib
import jaconv
import pandas as pd
from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.charfilter import *
from wordcloud import WordCloud
from wordcloud import STOPWORDS
import MeCab
from prepare_data import get_score_df


def get_word_merged_df():
    with open('out.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    t = Tokenizer()
    char_filters = [UnicodeNormalizeCharFilter()]
    analyzer = Analyzer(char_filters=char_filters, tokenizer=t)

    word_lists = []

    for i, row in enumerate(data):
        try:
            for t in analyzer.analyze(row[0]):
                surf = t.surface
                base = t.base_form
                pos = t.part_of_speech
                reading = t.reading

                word_lists.append([i, surf, base, pos, reading])
        except:
            continue

    word_df = pd.DataFrame(word_lists, columns=['No', '単語', '基本形', '品詞', '読み'])
    word_df['品詞'] = word_df['品詞'].apply(lambda x : x.split(',')[0])
    nega_pos_df = get_posnega_df()


    score_result = pd.merge(word_df, nega_pos_df, on = ['基本形', '品詞', '読み'], how = 'left')

    return score_result

def get_posnega_df():
    p_dic = pathlib.Path('dic')

    for i in p_dic.glob("*.txt"):
        with open(i, 'r', encoding='cp932') as f:
            x = [ii.replace('\n', '').split(':') for ii in f.readlines()]

    posi_nega_df = pd.DataFrame(x, columns=['基本形', '読み', '品詞', 'スコア'])
    posi_nega_df['読み'] = posi_nega_df['読み'].apply(lambda x : jaconv.hira2kata(x))
    posi_nega_df = posi_nega_df[~posi_nega_df[['基本形', '読み', '品詞']].duplicated()]

    return posi_nega_df

def get_score_df():
    pd.set_option('display.max_rows', None)
    df = get_word_merged_df()
    result = []
    for i in range(len(df['No'].unique())):
        tmp_df = df[df['No'] == i]
        text = ''.join(list(tmp_df['単語']))
        score = tmp_df['スコア'].astype(float).sum()
        score_r = score / tmp_df['スコア'].astype(float).count()
        result.append([i, text, score, score_r])

    score_df = pd.DataFrame(result, columns=['No.', 'テキスト', '累計スコア', '標準化スコア']).sort_values(by='標準化スコア').reset_index(drop=True)

    return score_df

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
    tagger = MeCab.Tagger("")
    tagger.parse('')
    select_conditions = ['名詞', '形容詞']

    pos_words = ""
    neg_words = ""

    for _, row in df.iterrows():
        if row['標準化スコア'] >= 0:
            text = wakati_text(tagger, select_conditions, row['テキスト'])
            pos_sentence = pos_sentence + ' ' + text
            pass
        else:
            text = wakati_text(tagger, select_conditions, row['テキスト'])
            neg_words = neg_words + ' ' + text

    return pos_words, neg_words

def out_wordcloud():
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
    
if __name__ == '__main__':
    out_wordcloud()