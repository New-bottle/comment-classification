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
            print(row)
            fopen = open(filepath+row['id']+'.txt', 'r')
            content = ''
            for eachLine in fopen:
                content += eachLine
            ans.append([content, row['pred']])
    return ans            

if __name__ == '__main__':
    ans = get_training_set()
    print(ans[0][1])
    test = get_test_set()
    print(test[0][1])