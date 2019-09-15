from Perceptron import Perceptron
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
   
 
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
    
    #trenowanie algorytmu perceptronu:
    ppn = Perceptron(eta=0.1, n_iter=10)
    ppn.fit(X,y)
    plt.plot(range(1, len(ppn.errors_)+1), ppn.errors_, marker='o')
    plt.xlabel('Epoki')
    plt.ylabel('Liczba aktualizacji')
    plt.show()
    
    
        
    plot_decision_regions(X, y, classifier=ppn)
    plt.xlabel('Długosć działki [cm]')
    plt.ylabel('Długosć płatka [cm]')
    plt.legend(loc='upper left')
    plt.show()
        
    
if __name__=="__main__":
    main()  
    
    