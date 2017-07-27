import jieba
train_file = "training_new.csv"
filepath = './comment_new/'

dic = []
for i in range(6000):
    with open(filepath+'comment_'+str(i)+'.txt', 'r') as fopen:
        content = ''
        for eachline in fopen:
            content += eachline
        seg_list = jieba.lcut(content.strip(), cut_all=False)
        dic.extend(seg_list)

with open('dict.txt', 'w') as f:
    for eachword in dic:
        f.writelines(eachword.encode('utf8')+'\n')
    f.close()