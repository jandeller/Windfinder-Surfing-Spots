#!/usr/bin/env bash

data_folder='data/raw'

echo "Generating concatinated Kiel data"
for f in $data_folder/weatherdata_10044N_201*.csv; do sed '1d;$d' $f >> $data_folder/_weather_data_10044N_2016-2019.csv; done
for f in $data_folder/pageviews_10044N_201*.csv; do cat $f >> $data_folder/_pageviews_data_10044N_2016-2019.csv; done

echo "Generating concatinated St. Peter Ording data"
for f in $data_folder/weatherdata_10028_201*.csv; do sed '1d;$d' $f >> $data_folder/_weather_data_10028_2016-2019.csv; done
for f in $data_folder/pageviews_10028_201*.csv; do cat $f >> $data_folder/_pageviews_data_10028_2016-2019.csv; done

