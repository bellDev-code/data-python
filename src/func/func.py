import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# 질적자료 도수화
def quali_cnt(df, field, exit= False):
    sns.countplot(data=df,y=df[field])
    plt.show()

    tmp = df[field].value_counts()
    tmp_ratio = tmp / len(df)

    data={'cnt':tmp,
         'ratio':tmp_ratio}
    dfRatio=pd.DataFrame(data)
    
    if exit == True:
        dfRatio.to_csv(f'd:/data/bank_{field}_ratio.csv', index=False)
    
    return dfRatio