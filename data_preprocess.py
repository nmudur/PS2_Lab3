import pandas as pd
df = pd.read_csv('time_series_covid19_confirmed_global.csv')
country_filter = ['Italy', 'US', 'New Zealand', 'Spain', 'India', 'South Africa', 'Taiwan', 'Brazil']
df_tiny = df.loc[df['Country/Region'].isin(country_filter)]
print (df.loc[df['Country/Region']=='India']  == df_tiny.loc[df_tiny['Country/Region']=='India'])
df_tiny.to_csv('time_series_covid19_confirmed_global_tiny.csv')
print (34)