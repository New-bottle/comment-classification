from readin import *
from parse import *
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

data_path = '../data/'
train_ori = data_path + 'training_new.csv'
train_vec = data_path + 'training_vec.pk1'

data_set = get_training_set(train_ori)
data_set = parse_data(data_set)

corpus = []
for item in data_set:
    corpus.append(" ".join(item[0]))
vectorizer = CountVectorizer()
transformer = TfidfTransformer()
tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus)).toarray()

print tfidf
print('111')

def get_vec(data_set):
    vec_list = []
    label_list = []
    for i, each in enumerate(data_set):
        label_list.append(each[1])
        this_vec = transformer.transform(vectorizer.transform([" ".join(data_set[i][0])])).toarray()
        vec_list.extend(this_vec)
    return vec_list, label_list

vec_list, label_list = get_vec(data_set)

with open(train_vec, 'wb') as f:
    pickle.dump(vec_list, f)
    pickle.dump(label_list, f)
    f.close()

test_set = get_training_set(data_path + 'example.csv')
test_set = parse_data(test_set)
vec_list, label_list = get_vec(test_set)

with open(data_path + 'test_vec.pk1', 'wb') as f:
    pickle.dump(vec_list, f)
    f.close()