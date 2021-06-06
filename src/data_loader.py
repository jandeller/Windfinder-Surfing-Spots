import os
import yaml

import pandas as pd

from pathlib import Path


def load_data_by_facts(name: str = 'main', data_dir: Path = Path(__file__).parent / "../data/",
                       parse_dates=False, header='infer') -> pd.DataFrame:
    """
    Loads a dataset by given identifier matching any defined fact
    in data/facts.yaml and returns it as a pandas DataFrame.

    Parameters
    ----------
    name
        Identifier corresponding to defined fact in data/facts.yaml.

    data_dir
        Path object defining path to a directory containing a facts.yaml describing loadable datasets.

    Returns
    ----------
        A DataFrame containing specified dataset.
    """
    # TODO - proper exception handling
    with (data_dir / 'facts.yaml').open() as f:
        # load corresponding facts to specified dataset
        facts = yaml.load(f, Loader=yaml.FullLoader)['datasets'][name]
        # init dataframe safely not destroying int string containing leading zeros
        df = pd.read_csv(data_dir / facts['path'], dtype=str, sep=facts['sep'], parse_dates=parse_dates, header=header)
        df.columns = facts['astypes'].keys()
        # apply specified types
        for k, v in facts['astypes'].items():
            df[k] = df[k].astype(v)
        return df
