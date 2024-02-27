import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


class pca():

    def __init__(self, dataframe, ticker) -> pd.DataFrame:
        self.data = dataframe
        self.ticker_name = ticker


    def ppmcc(self):
        #資料視覺化
        cor = self.data.corr()
        #plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] # 修改中文字體
        plt.rcParams['font.sans-serif'] = ['Noto Sans TC'] # 修改中文字體

        plt.figure(figsize=(12,12))
        plt.title("Correlation Matrix(" + str(self.ticker_name) +")")
        sns.heatmap(cor, vmax=1,square=True,annot=True,cmap="cubehelix")
        plt.savefig("PPMCC_" + self.ticker_name + ".png")
        pass

    def run(self):
        #標準化
        scale = StandardScaler().fit(self.data)
        rescale = pd.DataFrame(scale.fit_transform(self.data),columns=self.data.columns,index=self.data.index)
        #標準化視覺化
        plt.figure(figsize=(20,5))
        plt.title("pca_analyize")
        rescale["營收"].plot()
        plt.grid=True
        plt.legend()
        plt.show()

        X_train = rescale.copy()
        n_components = 4
        pca = PCA(n_components=n_components)
        Pc = pca.fit(X_train)

        fig, axes = plt.subplots(ncols=2)
        Series1 = pd.Series(Pc.explained_variance_ratio_[:n_components ]).sort_values()
        Series2 = pd.Series(Pc.explained_variance_ratio_[:n_components ]).cumsum()

        Series1.plot.barh(title="Explained Variance",ax=axes[0])
        Series2.plot(ylim=(0,1),ax=axes[1],title="Cumulative Explained Variance")
        print("變數累積解釋比例：")
        print(Series2[len(Series2)-1:len(Series2)].values[0])
        print("各變數解釋比例：")
        print(Series1.sort_values(ascending=False))
        pca.components_(1)
        pass