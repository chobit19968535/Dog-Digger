﻿from ctypes.wintypes import tagPOINT
from hashlib import new
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from matplotlib import font_manager

class pca():

    def __init__(self, dataframe, ticker) -> pd.DataFrame:
        self.sharp_dir = None
        self.data = dataframe
        self.ticker_name = ticker


    def ppmcc(self):
        import matplotlib.pyplot as plt
        import matplotlib
        import os
        import shutil
        
        font_custom = True
        font_style = 'NotoSansTC-Medium.ttf'
        ttf_path = None

        install_path = str(matplotlib.__file__).replace('\__init__.py','')
        install_path = install_path + '\\mpl-data\\fonts\\ttf\\'
        if(self.sharp_dir != None):
            ttf_path = self.sharp_dir + '\\fonts\\'+font_style
        if(ttf_path != None):
            if( os.path.exists (ttf_path) ):
                try:
                    shutil.copyfile( install_path + font_style)
                except:
                    if(os.path.exists(install_path + font_style)):
                        pass
                    font_custom = False
                    pass
        #資料視覺化
        cor = self.data.corr()
        if font_custom:
            plt.rcParams['font.sans-serif'] = ['Noto Sans TC Mediumn'] # 修改中文字體
        else:
            plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] # 修改中文字體


        plt.figure(figsize=(10,10))
        plt.title("Correlation Matrix(" + str(self.ticker_name) +")")
        sns.heatmap(cor, vmax=1,square=True,annot=True,cmap="cubehelix")
        plt.savefig("PPMCC_" + self.ticker_name + ".png")
        pass

    pass
    def run(self):
        #標準化
        scale = StandardScaler().fit(self.data)
        rescale = pd.DataFrame(scale.fit_transform(self.data),columns=self.data.columns,index=self.data.index)
        #標準化視覺化
        plt.figure(figsize=(20,5))
        plt.title("pca_analyize")
        rescale["毛利"].plot()
        plt.grid=True
        plt.legend()
        plt.show()

        X_train = rescale.copy()
        n_components = 9
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
        pca.components_[1]
        pass