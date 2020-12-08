import pandas as pd
pandf =pd.read_csv("C:/Users/GODSBEER/Desktop/lstm/final.csv")
pandf = pandf[['finalday']]
nparr = pandf[['finalday']].values
##cur_price = {'종가예측치':800000}
##cur_price['종가예측치']=nparr
     


print( list(nparr))