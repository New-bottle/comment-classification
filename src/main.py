from sklearn import svm
# from sklearn import cross_validation,metrics
from sklearn.decomposition import PCA
# from pca import *
import numpy as np
import pickle

do_PCA = True
train_file = '../data/training_vec.pk1'
test_file = '../data/test_vec.pk1'
cross_size = 0

with open(train_file, 'rb') as f:
    X = pickle.load(f)
    y = pickle.load(f)
    f.close()
with open(test_file, 'rb') as f:
    X_test = pickle.load(f)
    f.close()
X_train = []
y_train = []
X_cross = []
y_cross = []
for i in range(1000-cross_size):
    X_train.append(X[i])
    y_train.append(y[i])
for i in range(1000-cross_size, 1000):
    X_cross.append(X[i])
    y_cross.append(y[i])

c_val = 5
print 'c_val =', c_val
gamma_v = 0.150
print 'gamma_v =', gamma_v

if do_PCA:
    components = 400
    print 'components = ', components 
    pca = PCA(n_components=components)
    print 'fitting pca'
    X_train = pca.fit_transform(X_train)
    print 'pca fit end'
    if cross_size > 0:
        X_cross = pca.transform(X_cross)
    X_test = pca.transform(X_test)
clf = svm.SVC(kernel='rbf', gamma=gamma_v, probability=True, C = c_val)
clf.fit(X_train, y_train)
print('training over!')

# y_ = np.zeros(200)
if cross_size > 0:
    y_ = clf.predict_proba(X_cross)[:,1]
    print(np.array(y_).shape[0])

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
#   test_auc = metrics.roc_auc_score(y_cross, y_)
#   print test_auc
#   print metrics.roc_auc_score(y_cross, y_)
else:
    y_test = clf.predict_proba(X_test)[:,1]
    with open('../data/ans.txt', 'w') as f:
        for each in y_test:
            print each
            f.write(str(each))
            f.write('\n')