import sys
import jieba
import codecs
import pandas
import numpy as np
import matplotlib.pyplot as plt
from imageio import imread
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator

def preprocess(input_filename):
    try:
        fin = open(input_filename, "r", encoding = 'utf-8')
    except Exception as e:
        print('Error:',e)
        sys.exit()
    
    fout = open("__" + input_filename, "w", encoding = 'utf-8')

    for line in fin.readlines():
        if len(line) > 0:
            if line[0] == '2' and line[1] == '0' or (line[:4] == "http"):
                pass
            else:
                fout.write(line)

def main(txt,maskimg = 'love.png',font = 'KaiTi_GB2312.ttf'):
    try:
        text = open('__'+txt,'r',encoding = 'utf-8').read()
    except Exception as e:
        print('Error:',e)
        sys.exit()
    segs = jieba.cut(text)
    # word_split = " ".join(segs)

    stopwords = set([line.strip() for line in codecs.open('stopwords.txt', 'r', 'utf-8')])
    words = []
    for seg in segs:
        word = seg.strip().lower()
        if len(word) > 1 and word not in stopwords:
            words.append(word)

    words_df = pandas.DataFrame({'word': words})
    words_data = words_df.groupby(by = ['word'])['word'].agg(np.size) # colum word, row size
    words_data = words_data.to_frame()
    words_data.columns = ['number']
    words_data = words_data.reset_index().sort_values(by = "number", ascending = False)

    print('# of different words =', len(words_data))
    # print(type(words_data))  # <class 'pandas.core.frame.DataFrame'>
    print('TOP5: \n', words_data.iloc[:5, :])


    mask = imread(maskimg) 
    # my_wordclud = WordCloud(max_words=100,width = 1600,height=800).generate(word_split)
    my_wordclud = WordCloud(
        background_color = 'white',                          # set background color
        mask = mask,                                         # set mask
        max_words = 100,                                     # set max words
        # stopwords = STOPWORDS,                             # set stop words
        font_path = font,                                    # set font, or can show Chinese
        max_font_size = 100,                                 # set max font size
        random_state = 30,                                   # set kinds of color plan
        scale = .5
    ).fit_words(
        dict(words_data.head(200).itertuples(index = False)) # get TOP 200 words
    )
    # recolor cloud words
    my_wordclud.recolor(color_func = ImageColorGenerator(mask))

    # save image
    txt_name = txt
    if txt.find('.') != -1:
        txt_name = '.'.join(txt.split('.')[:-1])
    maskimg_name = maskimg
    if maskimg.find('.') != -1:
        maskimg_name = '.'.join(maskimg.split('.')[:-1])
    output_filename = txt_name + '_' + maskimg_name + '_wordcloud.png'
    print('Saving', output_filename)
    my_wordclud.to_file(output_filename)

    # show cloud
    plt.imshow(my_wordclud)
    plt.axis("off")
    plt.show()


if __name__ == '__main__':
    if len(sys.argv) == 2 :
        preprocess(sys.argv[1])
        main(sys.argv[1])
    elif len(sys.argv) == 4 :
        preprocess(sys.argv[1])
        main(sys.argv[1],sys.argv[2],sys.argv[3])
    else:
        print('\n[Usage 1] python create_word_cloud.py <input.txt>\n[Usage 2] python create_word_cloud.py <input.txt> <mask.png> <font.ttf>\n[File output] __input_text.txt input_mask_wordcloud.png\n[Terminal output] TOP 5 words\n')