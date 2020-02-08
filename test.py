import pandas as pd
import numpy as np

def something():
    np.random.seed(24)
    df = pd.DataFrame({'A': np.linspace(1, 10, 10)})
    df = pd.concat([df, pd.DataFrame(np.random.randn(10, 4), columns=list('BCDE'))],
               axis=1)
    df.iloc[0, 2] = np.nan
    var = df.style.apply(highlight_greaterthan_1, axis=1).render()
    print(var)


def highlight_greaterthan(s, column):
    is_max = pd.Series(data=False, index=s.index)
    is_max[column] = s.loc[column] >= 1
    return ['background-color: red' if is_max.any() else '' for v in is_max]


def highlight_greaterthan_1(s):
    if s.B > 1.0:
        return ['background-color: yellow'] * 5
    else:
        return ['background-color: white'] * 5



if __name__ == '__main__':
    something()