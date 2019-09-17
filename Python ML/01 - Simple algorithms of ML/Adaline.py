import numpy as np


# algorytm wsadowego gradientu prostego
class AdalineGD(object):
    
    
    def __init__(self, eta=0.01, n_iter=50, random_state=1):
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state
        #eta - współczynnik uczenia; zmiennoprzecinkowy [0.0,1.0]
        #n_iter - liczba iteracji po zestawach uczących
        #random_state - ziarno generatora licz pseudolosowych
     
     
    # trenowanie za pomocą danych uczących    
    def fit(self, X, y):
        # rgen - generator liczb pseudolosowych
        # w_ -  wagi po dopasowaniu
        # cost_ -suma kwadratów błędów w każdej epoce
        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0.0, scale=0.01, size=1+X.shape[1])
        self.cost_ = []
        
        for i in range(self.n_iter):
            net_input = self.net_input(X)
            output = self.activation(net_input)
            errors = (y - output)
            self.w_[1:] += self.eta * X.T.dot(errors)
            self.w_[0] += self.eta * errors.sum()
            cost = (errors**2).sum() / 2.0
            self.cost_.append(cost)
        return self
    
    
    # całkowite pobudzenie
    def net_input(self, X):
        return np.dot(X, self.w_[1:] + self.w_[0])
    
    
    #funkcja aktywacji
    def activation(self, X):
        return X
    
    
    # zwraca etykietę klas
    def predict(self, X):
        return np.where(self.activation(self.net_input(X)) >= 0.0, 1, -1)


# algorytm stochastycznego spadku wzdłuż gradientu
class AdalineSGD(object):
    
    
    def __init__(self, eta=0.01, n_iter=10, shuffle=True, random_state=None):
        self.eta = eta
        self.n_iter = n_iter
        self.w_initialized = False
        self.shuffle = shuffle
        self.random_state = random_state
        # shuffle -  (bool) czy tasować dane uczące przed każdą epoką
        
        
    def fit(self, X, y):
        self._initialize_weights(X.shape[1])
        self.cost_ = []
        for i in range(self.n_iter):
            if self.shuffle:
                X, y = self._shuffle(X, y)
            cost = []
            for xi, target in zip(X, y):
                cost.append(self._update_weights(xi, target))
            avg_cost = sum(cost) / len(y)
            self.cost_.append(avg_cost)
        return self
    
    
    # dopasowanie danych uczących bez ponownej inicjalizacji wag
    # słyży do aktualizacji modelu
    def partial_fit(self, X, y):
        if not self.w_initialized:
            self._initialize_weights(X.shape[1])
        if y.ravel.shape[0] > 1:
            for xi, target in zip(X, y):
                self._update_weights(xi, target)
        else:
            self._update_weights(X, y)
        return self
    
    
    def _shuffle(self, X, y):
        r = self.rgen.permutation(len(y))
        return X[r], y[r]
    
    
    def _initialize_weights(self, m):
        self.rgen = np.random.RandomState(self.random_state)
        self.w_ = self.rgen.normal(loc=0.0, scale=0.01, size=1+m)
        self.w_initialized = True
        
    
    def _update_weights(self, xi, target):
        output = self.activation(self.net_input(xi))
        error = (target - output)
        self.w_[1:] += self.eta * xi.dot(error)
        self.w_[0] += self.eta * error
        cost = 0.5 * error**2
        return cost
    
    
    def net_input(self, X):
        return np.dot(X, self.w_[1:] + self.w_[0])
    
    
    def activation(self, X):
        return X


    def predict(self, X):
        return np.where(self.activation(self.net_input(X)) >= 0.0, 1, -1)

