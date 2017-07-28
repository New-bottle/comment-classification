from sklearn import svm
import numpy as np
import pickle

train_file = '../data/training_vec.pk1'
test_size = 200
with open(train_file, 'rb') as f:
	X = pickle.load(f)
	y = pickle.load(f)
	f.close()
X_train = []
y_train = []
X_test = []
y_test = []
for i in range(1000-test_size):
	X_train.append(X[i])
	y_train.append(y[i])
for i in range(1000-test_size, 1000):
	X_test.append(X[i])
	y_test.append(y[i])

# for index, each in enumerate(X_train[0]):
# 	if (each != 0):
# 		print(index, each)
# print(y_train)
clf = svm.SVC(kernel='linear', gamma=0.022)
clf.fit(X_train, y_train)
print('training over!')

# y_ = np.zeros(200)
y_ = clf.predict(X_test)
print(y_)
print(np.array(y_).shape[0])
# for index, each in enumerate(X_test):
# 	y_[index] = clf.predict(each)

# for i in range(200):
# 	if (y_[i] >= 0.5):
# 		 y_[i] = 1
# 	else:
# 		 y_[i] = 0

# accuracy = np.sum(y_ == y_test) / 200
accuracy = 0.0
for i in range(test_size):
	if y_[i] == y_test[i]:
		accuracy += 1.
accuracy /= test_size
print(y_)
print(accuracy)