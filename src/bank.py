import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from func.func import quali_cnt

file_path = 'd:/data/bank.csv'

df = pd.read_csv('d:/data/bank.csv', sep=',')
df.info()

quali_cnt(df, 'age')
