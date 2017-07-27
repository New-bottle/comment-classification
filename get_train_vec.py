from readin import *
from parse import *
import numpy as np

train_ori = 'training_new.csv'
train_vec = 'training_vec.pk1'

data_set = get_training_set(train_ori)
data_set = parse_data(data_set)

with open('dict.txt', 'r') as f:
    dic = f.read().split('\n')

dic_arr = np.array(dic)
dic_set = set(dic)
dic_rev = dict()
for index, each in enumerate(dic):
    dic_rev[each] = index


vec_list = []
label_list = []
for each in data_set:
    label_list.append(each[1])
    this_vec = np.zeros(dic_arr.shape[0])
    for token in each[0]:
        if dic_rev.has_key(token.encode('utf-8')):
            this_vec[dic_rev[token.encode('utf-8')]] = 1
    vec_list.append(this_vec)

with open(train_vec, 'wb') as f:
    pickle.dump(vec_list, f)
    pickle.dump(label_list, f)
    f.close()