from sklearn import datasets
import numpy as np


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


if __name__ == '__main__':
    main()

