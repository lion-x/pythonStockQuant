import tushare as ts


df_sh_hist = ts.get_hist_data('sh', start='2009-01-01', end='2019-06-01')
print(df_sh_hist.head())
print(df_sh_hist.tail())
print(df_sh_hist.info())