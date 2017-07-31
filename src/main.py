from sklearn import svm
# from sklearn import cross_validation,metrics
from sklearn.decomposition import PCA
# from pca import *
import numpy as np
import pickle

train_file = '../data/training_vec.pk1'
test_file = '../data/test_vec.pk1'
cross_size = 0
do_PCA = True
cross_k = 5

with open(train_file, 'rb') as f:
    X = pickle.load(f)
    y = pickle.load(f)
    f.close()
with open(test_file, 'rb') as f:
    X_test = pickle.load(f)
    f.close()
if do_PCA:
    components = 400
    print 'components = ', components 
    pca = PCA(n_components=components)
    print 'fitting pca'
    X = pca.fit_transform(X)
    X_test = pca.transform(X_test)
    print 'pca fit end'

best_c = 0.0
best_gamma = 0.0
best_acc = 0.0

def main(c_val, gamma_v):
    X_train = []
    y_train = []
    X_cross = []
    y_cross = []

    # c_val = 6
    print 'c_val =', c_val
    # gamma_v = 0.150
    print 'gamma_v =', gamma_v


    ans_clf = svm.SVC(kernel='rbf', gamma=gamma_v, probability=True, C = c_val)
    ans_accuracy = 1.0
    cross_size = len(X) / cross_k
    total_acc = 0.0
    for i in range(cross_k):
        indices = range(len(X))
        X_cross = [X[j] for j in indices if j % cross_k == i]
        y_cross = [y[j] for j in indices if j % cross_k == i]
        X_train = [X[j] for j in indices if j % cross_k != i]
        y_train = [y[j] for j in indices if j % cross_k != i]

        clf = svm.SVC(kernel='rbf', gamma=gamma_v, probability=True, C = c_val)
        clf.fit(X_train, y_train)
        print('training over!'),

        y_ = clf.predict_proba(X_cross)[:,1]

        accuracy = 0.0
        for i in range(cross_size):
            if y_[i] >= 0.5 and y_cross[i] == '1':
                accuracy += 1.
            if y_[i] < 0.5 and y_cross[i] == '0':
                accuracy += 1.
            # if ((y_[i] >= 0.5 and y_cross[i] == 1) or (y_[i] < 0.5 and y_cross[i] == 0)):
            # 	accuracy += 1.
        # print(y_cross)
        # print(y_)
        print(accuracy / cross_size)
        ans_accuracy = accuracy / cross_size
        total_acc += ans_accuracy
        # if (accuracy < ans_accuracy):
        #     ans_accuracy = accuracy
        #     ans_clf = clf
        #   test_auc = metrics.roc_auc_score(y_cross, y_)
        #   print test_auc
        #   print metrics.roc_auc_score(y_cross, y_)
    global best_acc
    global best_c, best_gamma
    if total_acc > best_acc:
        best_acc = total_acc
        best_c = c_val
        best_gamma = gamma_v
for c_val in range(10, 21, 2):       
    for gamma_v in range(1, 101, 5):
        main(c_val / 10.0, gamma_v / 100.0)

print 'best_c =', best_c
print 'best_gamma =', best_gamma
print 'best_accuracy =', best_acc
best_clf = svm.SVC(kernel='rbf', gamma=best_gamma, probability=True, C = best_c)
best_clf.fit(X, y)
y_test = best_clf.predict_proba(X_test)[:,1]
with open('../data/ans.txt', 'w') as f:
    for each in y_test:
        f.write(str(each))
        f.write('\n')