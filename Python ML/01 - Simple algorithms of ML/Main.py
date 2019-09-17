from Perceptron import Perceptron
from Adaline import AdalineGD, AdalineSGD
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
   
 
def plot_decision_regions(X, y, classifier, resolution=0.02):
        
    #konfiguracja generatora znaczników i mapy kolorów
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])
        
    #rysowanie wykresu powierzchni decyzyjnej:
    x1_min, x1_max = X[:, 0].min()-1, X[:, 0].max()+1
    x2_min, x2_max = X[:, 1].min()-1, X[:, 1].max()+1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.3, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())
    
    # rysowanie wykresu próbek:
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0], y=X[y == cl, 1],
                    alpha=0.8, c=colors[idx],
                    marker=markers[idx], label=cl,
                    edgecolor='black')


def perceptron_main(X,y):
    
    #trenowanie algorytmu perceptronu:
    ppn = Perceptron(eta=0.1, n_iter=10)
    ppn.fit(X,y)
    plt.plot(range(1, len(ppn.errors_)+1), ppn.errors_, marker='o')
    plt.xlabel('Epoki')
    plt.ylabel('Liczba aktualizacji')
    plt.show()
    
    #wykres regionów decyzyjnych
    plot_decision_regions(X, y, classifier=ppn)
    plt.xlabel('Długosć działki [cm]')
    plt.ylabel('Długosć płatka [cm]')
    plt.legend(loc='upper left')
    plt.show()
    
    
def adalineGD_main(X,y):
    
    # wykres kosztów dla danej liczby epok przy założeniu dwóch różnych
    # wartosci współczynnika uczenia: {0.01, 0.0001}
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10,4))
    
    ada1 = AdalineGD(n_iter=10, eta=0.01).fit(X,y)
    ax[0].plot(range(1, len(ada1.cost_) + 1),
              np.log10(ada1.cost_), marker='o')
    ax[0].set_xlabel('Epoki')
    ax[0].set_ylabel('Log(suma kwadratów błędów)')
    ax[0].set_title('Adaline - wsp. uczenia: 0.01')
    
    ada2 = AdalineGD(n_iter=10, eta=0.0001).fit(X,y)
    ax[1].plot(range(1, len(ada2.cost_) + 1),
              ada2.cost_, marker='o')
    ax[1].set_xlabel('Epoki')
    ax[1].set_ylabel('Suma kwadratów błędów')
    ax[1].set_title('Adaline - wsp. uczenia: 0.0001')
    plt.show()
    
    # standaryzacja modelu:
    X_std = np.copy(X)
    X_std[:,0] = (X[:, 0] - X[:, 0].mean()) / X[:, 0].std()
    X_std[:,1] = (X[:, 1] - X[:, 1].mean()) / X[:, 1].std()
    
    # ponowne uczenie modelu Adaline po wprowadzeniu standaryzacji
    # wsp. uczenia: 0.01
    ada = AdalineGD(n_iter=15, eta=0.01).fit(X_std, y)
    plot_decision_regions(X_std, y, classifier=ada)
    plt.title('Adaline - Gradient prosty')
    plt.xlabel('Długosć działki [standaryzowana]')
    plt.ylabel('Długosć płatka [standaryzowana]')
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.show()
    
    plt.plot(range(1, len(ada.cost_) + 1), ada.cost_, marker='o')
    plt.xlabel('Epoki')
    plt.ylabel('Suma kwadratów błędów')
    plt.show()
    
    
def adalineSGD_main(X,y):
    X_std = np.copy(X)
    X_std[:,0] = (X[:, 0] - X[:, 0].mean()) / X[:, 0].std()
    X_std[:,1] = (X[:, 1] - X[:, 1].mean()) / X[:, 1].std()
    
    ada = AdalineSGD(n_iter=15, eta=0.01, random_state=1)
    ada.fit(X_std, y)
    plot_decision_regions(X_std, y, classifier=ada)
    plt.title('Adaline - sochastyczny spadek wzdłuż gradientu')
    plt.xlabel('Długosć działki [standaryzowana]')
    plt.ylabel('Długosć płatka [standaryzowana]')
    plt.legend(loc='upper left')
    plt.show()
    
    plt.plot(range(1, len(ada.cost_) + 1), ada.cost_, marker='o')
    plt.xlabel('Epoki')
    plt.ylabel('Średni koszt')
    plt.show()
    

def main():
    
    df = pd.read_csv('https://archive.ics.uci.edu/ml/'
        'machine-learning-databases/iris/iris.data', header=None)
    print(df.tail())
    
    # bierzemy pod uwagę tylko 100 pierszych wyników, czyli rozwiązujemy
    # problem binarny, czy jest to iris-setosa czy iris-versicolor
    # pomijamy iris-virginica
    y = df.iloc[0:100,4].values
    y = np.where(y == 'Iris-setosa', -1, 1)
    
    # wybieramy długosć działki i płatka
    X = df.iloc[0:100, [0,2]].values
    
    # wykres danych:
    plt.scatter(X[:50, 0], X[:50, 1],
                color='red', marker='o', label='Setosa')
    plt.scatter(X[50:100, 0], X[50:100, 1], 
                color='blue', marker='x', label='Versicolor')
    plt.xlabel('Długosć działki [cm]')
    plt.ylabel('Długosć płatka [cm]')
    plt.show()
    
    #perceptron_main(X,y)
    #adalineGD_main(X,y)
    adalineSGD_main(X,y)
    
    
if __name__=="__main__":
    main()  
    
    