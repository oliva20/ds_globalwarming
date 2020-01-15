import pymongo
from pymongo import MongoClient
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import make_blobs

client =  MongoClient("localhost", 27017)
db = client["gw_data"]
col = db["methane_emissions"]


def main():
    df = load_data()
    
    print(df)

def load_data():
    #load data using pandas into a dataframe
    df = pd.DataFrame(list(col.find({"GEO":"Portugal"})))
    #delete ids
    del df['_id']
    print("Loaded: " + str(len(df)) + " rows")
    return df


def generate_clusters():
    return None

def test():
    # create dataset
    X, y = make_blobs(
    n_samples=150, n_features=2,
    centers=3, cluster_std=0.5,
    shuffle=True, random_state=0
    )

    # plot
    plt.scatter(
    X[:, 0], X[:, 1],
    c='white', marker='o',
    edgecolor='black', s=50
    )

    plt.show()




if __name__=="__main__":
    main()


