# -*- coding:utf-8 -*-
import pickle
import numpy as np
import sys, os
import csv

train_file = 'training_origin.pk1'
test_file = 'test_origin.pk1'
# return a list
'''
[
    ['balabala', float]
    ['balabala', float]
    ...
]
'''
def get_training_set():
    filepath = './comment_new/'
    ans = []
    with open('example.csv', 'rb') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            fopen = open(filepath+row['id']+'.txt', 'r')
            content = ''
            for eachLine in fopen:
                content += eachLine
            ans.append([content,row['pred']])
    return ans

def get_test_set():
    filepath = './comment_new/'
    ans = []
    with open('training_new.csv', 'rb') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            fopen = open(filepath+row['id']+'.txt', 'r')
            content = ''
            for eachLine in fopen:
                content += eachLine
            ans.append([content, row['pred']])
    return ans            

if __name__ == '__main__':
    train = get_training_set()
    test = get_test_set()
    with open(train_file, 'wb') as f:
        pickle.dump(train, f)
    with open(test_file, 'wb') as f:
        pickle.dump(test, f)