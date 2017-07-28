import numpy as np
import pickle

def reduce_dim(X, percent):
    X = np.array(X)
    m,n = X.shape
    mu = np.zeros(n)
    print(X.shape)
    print(mu.shape)
    for i in range(n):
        tmp = X[:,i].copy()
        mu[i] = tmp.T.sum()
    tmp_x = X.copy()
    for i in range(n):
        tmp_x[:,i] -= mu[i]
    sigma = np.zeros([n,n])
    sigma = np.dot(tmp_x.T, tmp_x) / m

    print ('start svd')
    [U,S,Vh] = np.linalg.svd(sigma)
    print ('end svd')
    V = Vh.T
    total = 0.
    tmp = 0.
    k = n
    print(S)
    for i in range(n):
        total += S[i]
    print('total = ' , total)
    for i in range(n):
        tmp += S[i]
        if (tmp / total > 0.99) :
            k = i + 1
            break
    print('k = ' + str(k))
    Ureduce = U[:,0:k]
    return np.dot(tmp_x, Ureduce), Ureduce
'''
    # [U,S,V] = np.linalg.svd(X)
    with open('../data/training_pca.pk1','wb') as f:
    	pickle.dump(U,f)
    	pickle.dump(S,f)
    	pickle.dump(V,f)
    # with open('../data/training_pca.pk1', 'rb') as f:
    #     U = pickle.load(f)
    #     S = pickle.load(f)
    #     V = pickle.load(f)
    print(U)
    print(S)
    print(V)
    n,m = X.shape
    total = 0.
    tmp = 0.
    num = 0
    for i in range(n):
        total += S[i]
    for i in range(n):
        tmp += S[i]
        if (tmp / total > percent):
            num = i
            break
    print('n =  ' + str(n)),
    print('num = ' + str(num))
    return U[:,0:num]*S[0:num]*V[0:num]
'''

if __name__ == '__main__':
    with open('../data/training_vec.pk1', 'rb') as f:
        X = pickle.load(f)
    newx = reduce_dim(X, 25)