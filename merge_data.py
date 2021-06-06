#!/usr/bin/env python

from src.data_loader import load_data_by_facts as load


weather_kiel = load('weather_st.peter.ording', header=None)
weather_kiel['day'] = weather_kiel['date'].dt.normalize()
page_views = load('pageviews_st.peter.ording', header=None)
page_views['day'] = page_views['date']
weather_kiel = weather_kiel.merge(page_views, on='day', how='left')
weather_kiel = weather_kiel[['date_x', 'wind_speed', 'wind_direction', 'wind_gust', 'temp', 'count']]
weather_kiel.to_csv('data/_weather_data_10044N_2016-2019.csv', index=False)


weather_spo = load('weather_st.peter.ording', header=None)
weather_spo['day'] = weather_spo['date'].dt.normalize()
page_views = load('pageviews_st.peter.ording', header=None)
page_views['day'] = page_views['date']
weather_spo = weather_spo.merge(page_views, on='day', how='left')
weather_spo = weather_spo[['date_x', 'wind_speed', 'wind_direction', 'wind_gust', 'temp', 'count']]
weather_spo.to_csv('data/_weather_data_10028_2016-2019.csv', index=False)
