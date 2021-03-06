# Windfinder-Surfing-Spots
[Coding.Waterkant 2021](https://coding-waterkant-2021.devpost.com/) 

Project from Windfinder.

## Setup

### Virtual Environment

Setting up a virtual environment.

```shell
virtualenv -p python3 venv
source venv/bin/activate
```

Install projects requirements.

```shell
pip install -r requirements.txt
```

### Data Sets
Build Data
```shell
./concat.sh
```
```shell
./merge_data.py
```
## Content
### `notebooks`
#### `0maximum_views`
This notebook has some first EDA and also contains an analysis of the top x percent
of highest page views after deseasonalizing and detrending the page views time series.
It additionally includes the clustering model.

#### `1maximum_diffs`
This notebook explores some alternative ideas, e.g., 'do people check for that day or
for the weather two or three days in advance' and 'are diffs maybe more important than
the absolute hight?' (the answer to both questions seems to be closer to no.)
