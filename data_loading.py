#Task 1 
import pandas as pd
from sklearn.datasets import load_iris

def load_data():
    iris = load_iris()
    iris_df = pd.DataFrame(data=np.c_[iris['data'], iris['target']],
                         columns=iris['feature_names'] + ['target'])
    iris_df['species'] = iris_df['target'].map({0:'setosa', 1:'versicolor', 2:'virginica'})
    return iris_df

if __name__ == "__main__":
    df = load_data()
    print(df.head())
