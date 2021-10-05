import numpy as np #数値計算ライブラリ
import pandas as pd #データ解析ライブラリ
#グラフ描画
#%matplotlib inline
from matplotlib import pylab as plt
#グラフ横長にする
from matplotlib.pylab import rcParams
rcParams['figure.figsize']=15,6
#データ読み込み
filepath='ScoreData.csv'
data=pd.read_csv(filepath)
data.head()#行すべてを返す(引数の数字の数だけ行を返すことも可)
print(data.head())