import csv
import pandas as pd
from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.charfilter import *
from nega_posi import get_posnega_df

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

if __name__ == '__main__':
    df = get_score_df()
    print(df)