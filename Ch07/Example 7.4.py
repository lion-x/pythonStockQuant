import tushare as ts



token = '7348ee79fa91184728e38d6dae0ba9757ed58df19b7aa6563794651b'
pro = ts.pro_api(token)

df_gldq = pro.daily(ts_code='000651.SZ', start_date='20090101', end_date='20190601')

print(df_gldq.head())
print(df_gldq.tail())
print(df_gldq.info())
print(df_gldq.axes)