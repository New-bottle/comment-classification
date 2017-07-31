import jieba
import pandas as pd
train_file = "../data/training_new.csv"
filepath = '../comment_new/'
data_path = '../data/'

bag = []
for i in range(5000,6000):
    with open(filepath+'comment_'+str(i)+'.txt', 'r') as fopen:
        content = ''
        for eachline in fopen:
            content += eachline
        seg_list = jieba.lcut(content.strip(), cut_all=False)
        bag.extend(seg_list)
# get word bag for every comment
with open('../data/remove.txt', 'r') as f:
    punctuation = f.read().split('\n')

cleanbag = []              
for token in bag:
    for punc in punctuation:
        token = token.replace(punc, "")               
    if token != "":
        cleanbag.append(token)
# remove the puncuations

# (pd.Series(cleanbag).value_counts())
dic = list(set(cleanbag))



counts = pd.Series(cleanbag).value_counts()
# get the union-set
with open(data_path + 'dict.txt', 'w') as f:
    for index, each in enumerate(counts):
        if each > 0:
            print >>f, str(counts.index[index])
    # print >>f, str(list(counts)).decode('utf-8')
    # for eachword in dic:
    #     f.writelines(eachword.encode('utf8')+'\n')
    f.close()

pd.set_option('display.max_rows', None)
with open(data_path + 'dict_count.txt', 'w') as f:
    print >>f, str(counts)
    f.close()
