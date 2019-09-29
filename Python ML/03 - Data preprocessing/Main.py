# -*- coding: utf-8 -*-

def main():
    
    
    import pandas as pd
    from io import StringIO
    
    #wykrywanie brakujących danych
    csv_data = \
                '''A,B,C,D
                    1.0,2.0,3.0,4.0
                    5.0,6.0,,8.0
                    10.0,11.0,12.0,'''
    df = pd.read_csv(StringIO(csv_data))
    print(df)
    print(df.isnull().sum())
    
    #usuwanie próbek lub cech niezwracających wartoci
    print(df.dropna(axis=0))
    print(df.dropna(axis=1))
    print(df.dropna(subset=['C']))
    
    # wstawianie brakujących danych
    # imputacja z użyciem sredniej
    from sklearn.preprocessing import Imputer
    imr = Imputer(missing_values='NaN', strategy='mean', axis=0)
    imr = imr.fit(df.values)
    imputed_data = imr.transform(df.values)
    print(imputed_data)
    
    
if __name__ == '__main__':
    main()

