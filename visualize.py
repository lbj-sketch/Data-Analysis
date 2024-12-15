import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



df = pd.read_csv('ETHUSD_1m_Binance.csv')


df['Open time'] = pd.to_datetime(df['Open time'])
df['Close time'] = pd.to_datetime(df['Close time'])

df.set_index('Open time', inplace=True)

plt.figure(figsize=(12,6))
plt.plot(df.index, df['Open'], label='Open', alpha=0.7)
plt.plot(df.index, df['High'], label='High', alpha=0.7)
plt.plot(df.index, df['Low'], label='Low', alpha=0.7)
plt.plot(df.index, df['Close'], label='Close', alpha=0.7)
plt.title('ETH Price Over Time')
plt.xlabel('Time')
plt.ylabel('Price (USD)')
plt.legend()
plt.show()


plt.figure(figsize=(12,4))
plt.plot(df.index, df['Volume'], label='Volume', color='orange')
plt.title('ETH Volume Over Time')
plt.xlabel('Time')
plt.ylabel('Volume')
plt.legend()
plt.show()


corr = df[['Open','High','Low','Close','Volume','Quote asset volume','Number of trades','Taker buy base asset volume','Taker buy quote asset volume']].corr()

plt.figure(figsize=(10,8))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Feature Correlation Heatmap')
plt.show()


