import pandas as pd 
import matplotlib.pyplot as plt 
import plotly
import plotly.graph_objects as go
import plotly.express as px


stock_code = pd.read_html('http://kind.krx.co.kr/corpgeneral/', header=0)[0] 

stock_code.sort_values(['상장일'], ascending=True)


stock_code = stock_code[['회사명', '종목코드']] 

 
stock_code = stock_code.rename(columns={'회사명': 'company', '종목코드': 'code'}) 


 
stock_code.code = stock_code.code.map('{:06d}'.format) 
company='LG화학' 
code = stock_code[stock_code.company==company].code.values[0].strip() 

df = pd.DataFrame()
for page in range(1,21):
    url = 'http://finance.naver.com/item/sise_day.nhn?code={code}'.format(code=code)     
    url = '{url}&page={page}'.format(url=url, page=page)
    print(url)
    df = df.append(pd.read_html(url, header=0)[0], ignore_index=True)
df = df.dropna() 


df = df.rename(columns= {'날짜': 'date', '종가': 'close', '전일비': 'diff', '시가': 'open', '고가': 'high', '저가': 'low', '거래량': 'volume'}) 
 
df[['close', 'diff', 'open', 'high', 'low', 'volume']] = df[['close', 'diff', 'open', 'high', 'low', 'volume']].astype(int) 

 
df['date'] = pd.to_datetime(df['date']) 

 
df = df.sort_values(by=['date'], ascending=True) 

 
df.head()
fig = px.line(df, x='date', y='close', title='{}의 종가(close) Time Series'.format(company))

fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=3, label="3m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(step="all")
        ])
    )
)
fig.write_html("file.html")