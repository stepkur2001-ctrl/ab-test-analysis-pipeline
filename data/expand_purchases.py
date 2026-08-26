import pandas as pd
buyers = pd.read_csv('buyers.csv', sep=';')
raw_events = buyers.loc[buyers.index.repeat(buyers['n_purchases'])].reset_index(drop=True)
raw_events['event_id'] = range(1, len(raw_events)+1)
raw_events.to_csv('raw_events_expanded.csv', index=False, sep=';')
print(f'Получилось {len(raw_events)} строк')
raw_events.head(10)
from google.colab import files
files.download('raw_events_expanded.csv')
