import pickle
import jieba
import opencc

def parse_data(ori_data):
    ans = []
    for obj in ori_data:
        line = obj[0]
        seg_list = jieba.lcut(line.strip(), cut_all=False)
        ans.append([seg_list, obj[1]])
    return ans

if __name__ == '__main__':
    train_ori = 'training_origin.pk1'
    with open(train_ori, 'rb') as f:
        ori_data = pickle.load(f)
    train = parse_data(ori_data)
    for i in train[0][0]:
        print i,
    print(train[0][1])