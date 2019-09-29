from sklearn import datasets
import numpy as np
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
from LogisticRegression import LogisticRegressionGD


def plot_decision_regions(X, y, classifier, 
                              test_idx=None, resolution=0.02):
        
        
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
            
            
        if test_idx:
            X_test, y_test = X[list(test_idx), :], y[list(test_idx)]
            
            plt.scatter(X_test[:, 0], X_test[:, 1], c='', edgecolor='black',
                        alpha=1.0, linewidth=1, marker='o', edgecolors='k',
                        s=100, label='Zestaw testowy')


def main():
    iris = datasets.load_iris()
    X = iris.data[:, [2,3]]
    y = iris.target
    print('Etykiety klas:', np.unique(y))
    
    
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.3, random_state=1, stratify=y)
    # parametr stratify odpowiada za zwrócenie podzbiorów
    # mających takie same proporcje etykiet klas
    print('Liczba etykiet w zbiorze y: ', np.bincount(y))
    print('Liczba etykiet w zbiorze y_test: ', np.bincount(y_test))
    print('Liczba etykiet w zbiorze y_train: ', np.bincount(y_train))
    
    
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    sc.fit(X_train)
    X_train_std = sc.transform(X_train)
    X_test_std = sc.transform(X_test)
    
    
    # użycie perceptronu z biblioteki sci-kit learn
    from sklearn.linear_model import Perceptron
    ppn = Perceptron(max_iter=40, eta0=0.1, random_state=1)
    ppn.fit(X_train_std, y_train)
    
    
    y_pred = ppn.predict(X_test_std)
    print('Nieprawidłowo sklasyfikowane próbki: %d' % (y_test != y_pred).sum())
    
    
    from sklearn.metrics import accuracy_score
    print('Dokladnosc: %.4f' % accuracy_score(y_test, y_pred))
    print('Dokladnosc: %.4f' % ppn.score(X_test_std, y_test))
    
    
    def versiontuple(v):
        return tuple(map(int, (v.split("."))))
       
            
    X_combined_std = np.vstack((X_train_std, X_test_std))
    y_combined = np.hstack((y_train, y_test))
    plot_decision_regions(X=X_combined_std, y=y_combined,
                          classifier=ppn, test_idx=range(105,150))
    plt.xlabel('Długosć działki [standaryzowana]')
    plt.ylabel('Długosć płatka [standaryzowana]')
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.show()
     
    # użycie własnego algorytmu regresji logistycznej
    X_train_01_subset = X_train[(y_train == 0) | (y_train == 1)]
    y_train_01_subset = y_train[(y_train == 0) | (y_train == 1)]
    lrgd = LogisticRegressionGD(eta=0.05, n_iter=1000, random_state=1)
    lrgd.fit(X_train_01_subset, y_train_01_subset)
    plot_decision_regions(X=X_train_01_subset, y=y_train_01_subset,
                          classifier=lrgd)
    plt.xlabel('Długosć działki [standaryzowana]')
    plt.ylabel('Długosć płatka [standaryzowana]')
    plt.legend(loc='upper left')
    plt.show()
    
    # użycie algorytmu regresji logistycznej z biblioteki sci-kit learn
    from sklearn.linear_model import LogisticRegression
    lr = LogisticRegression(C=1000.0, random_state=1)
    lr.fit(X_train_std, y_train)
    plot_decision_regions(X_combined_std, y_combined, classifier=lr, 
                          test_idx=range(105,150))
    plt.xlabel('Długosć działki [standaryzowana]')
    plt.ylabel('Długosć płatka [standaryzowana]')
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.show()
    
    
    print(lr.predict_proba(X_test_std[:3, :]))
    print(lr.predict_proba(X_test_std[:3, :]).argmax(axis=1))
    
    # użycie algorytmu wektorów nosnych z biblioteki sci-kit learn
    from sklearn.svm import SVC
    svm = SVC(kernel='linear', C=1.0, random_state=1)
    svm.fit(X_train_std, y_train)
    plot_decision_regions(X_combined_std, y_combined, classifier=svm,
                                              test_idx=range(105, 150))
    plt.xlabel('Długosć działki [standaryzowana]')
    plt.ylabel('Długosć płatka [standaryzowana]')
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.show() 
    
    # stosowanie sztuczki z funkcją jądra (RBF)
    svm = SVC(kernel='rbf', random_state=1, gamma=0.2, C=1.0)
    svm.fit(X_train_std, y_train)
    plot_decision_regions(X_combined_std, y_combined, classifier=svm,
                                              test_idx=range(105, 150))
    plt.xlabel('Długosć działki [standaryzowana]')
    plt.ylabel('Długosć płatka [standaryzowana]')
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.show() 
    
    
    svm = SVC(kernel='rbf', random_state=1, gamma=100.0, C=1.0)
    svm.fit(X_train_std, y_train)
    plot_decision_regions(X_combined_std, y_combined, classifier=svm,
                                              test_idx=range(105, 150))
    plt.xlabel('Długosć działki [standaryzowana]')
    plt.ylabel('Długosć płatka [standaryzowana]')
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.show() 
    
    
    svm = SVC(kernel='rbf', random_state=1, gamma=0.19, C=1.0)
    svm.fit(X_train_std, y_train)
    plot_decision_regions(X_combined_std, y_combined, classifier=svm,
                                              test_idx=range(105, 150))
    plt.xlabel('Długosć działki [standaryzowana]')
    plt.ylabel('Długosć płatka [standaryzowana]')
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.show() 
    
    # drzewo decyzyjne w sci-kit learn
    from sklearn.tree import DecisionTreeClassifier
    tree = DecisionTreeClassifier(criterion='gini', max_depth=4, 
                                                  random_state=1)
    tree.fit(X_train, y_train)
    X_combined = np.vstack((X_train, X_test))
    y_combined = np.hstack((y_train, y_test))
    plot_decision_regions(X_combined, y_combined, classifier=tree, 
                                          test_idx=range(105, 150))
    plt.xlabel('Długosć działki [standaryzowana]')
    plt.ylabel('Długosć płatka [standaryzowana]')
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.show()   
    
    
    from pydotplus import graph_from_dot_data
    from sklearn.tree import export_graphviz
    dot_data = export_graphviz(tree, filled=True, rounded=True, 
                               class_names=['Setosa', 'Versicolor',
                                'Virginica'], feature_names=['Dlugosc platka',
                                'Szerokosc platka'], out_file=None)
    graph = graph_from_dot_data(dot_data)
    graph.write_png('drzewo.png')
    
    # użycie losowego lasu 
    from sklearn.ensemble import RandomForestClassifier
    forest = RandomForestClassifier(criterion='gini', n_estimators=25,
                                    random_state=1, n_jobs=2)
    forest.fit(X_train, y_train)
    plot_decision_regions(X_combined, y_combined, classifier=forest, 
                                              test_idx=range(105, 150))
    plt.xlabel('Długosć działki [standaryzowana]')
    plt.ylabel('Długosć płatka [standaryzowana]')
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.show()  
    
    # KNN 
    from sklearn.neighbors import KNeighborsClassifier
    knn = KNeighborsClassifier(n_neighbors=5, p=2, metric='minkowski')
    knn.fit(X_train_std, y_train)
    plot_decision_regions(X_combined_std, y_combined, classifier=knn, 
                                              test_idx=range(105, 150))
    plt.xlabel('Długosć działki [standaryzowana]')
    plt.ylabel('Długosć płatka [standaryzowana]')
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.show()  
    

if __name__ == '__main__':
    main()

