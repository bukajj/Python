import numpy as np


class Perceptron(object):
    
    
    def __init__(self, eta=0.01, n_iter=50, random_state=1):
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state
        #eta - współczynnik uczenia; zmiennoprzecinkowy [0.0,1.0]
        #n_iter - liczba iteracji po zestawach uczących
        #random_state - ziarno generatora licz pseudolosowych
        
        
    def fit(self, X, y):
        
        rgen = np.random.RandomState(self.random_state)
        # rgen - generator liczb pseudolosowych
        
        self.w_ = rgen.normal(loc=0.0, scale=0.01, size=1+X.shape[1])
        self.errors_ = []
        # w_ -  wagi po dopasowaniu
        # errors_ - lista nieprawidłowych klasyfikacji w każdej epoce
        
        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X,y):
                # metoda zip() zwraca obiekt będący iteratorem krotek
                update = self.eta * (target - self.predict(xi))
                #aktualizaja wagi
                self.w_[1:] += update * xi
                self.w_[0] += update
                errors += int(update != 0.0)
            
            self.errors_.append(errors)
        return self
    
    
    def net_input(self, X):
        #oblicza całkowite pobudzenie
        return np.dot(X, self.w_[1:] + self.w_[0])
        #dot() iloczyn skalarny    
    
    
    def predict(self, X):
        # zwraca etykietę klas po obliczeniu funkcji skoku jednostkowego
        return np.where(self.net_input(X) >= 0.0, 1, -1)
    
    