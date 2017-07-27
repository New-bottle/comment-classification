# -*- coding:utf-8 -*-
import pickle
import numpy as np
import sys, os
import csv

# return a list
'''
[
    ['balabala', float]
    ['balabala', float]
    ...
]
'''
def get_training_set(filename):
    filepath = '../comment_new/'
    ans = []
    with open(filename, 'rb') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            fopen = open(filepath+row['id']+'.txt', 'r')
            content = ''
            for eachLine in fopen:
                content += eachLine
            ans.append([content,row['pred']])
    return ans

if __name__ == '__main__':
    train_file = 'training_origin.pk1'
    test_file = 'test_origin.pk1'
    train = get_training_set("training_new.csv")
    with open(train_file, 'wb') as f:
        pickle.dump(train, f)