from wordcloud import WordCloud
from wordcloud import STOPWORDS
import MeCab
from prepare_data import get_score_df

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
            pos_words = pos_words + ' ' + text
            pass
        else:
            text = wakati_text(tagger, select_conditions, row['テキスト'])
            neg_words = neg_words + ' ' + text

    print(neg_words)

    return pos_words, neg_words

def out_wordcloud():
    data = get_score_df()

    pos_words, neg_words = divide_words(data)

    fpath = "./ipaexg.ttf"

    stop_words = [
        '国葬',
        '安倍',
        '晋三',
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