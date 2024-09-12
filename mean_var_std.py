import numpy as np

# 0, 1, 2
# 3, 4, 5
# 6, 7, 8

def calculate(list):
    if len(list) != 9 :
        raise ValueError('List must contain nine numbers.')

    ls = np.array(list).reshape(3, 3)

    print(ls)

    calculates = {
        'mean' : [ls.mean(axis=0).tolist(), ls.mean(axis=1).tolist(), ls.mean()],
        'variance' : [ls.var(axis=0).tolist(), ls.var(axis=1).tolist(), ls.var()],
        'standard deviation' : [ls.std(axis=0).tolist(), ls.std(axis=1).tolist(), ls.std()],
        'max' : [ls.max(axis=0).tolist(), ls.max(axis=1).tolist(), ls.max()],
        'min' : [ls.min(axis=0).tolist(), ls.min(axis=1).tolist(), ls.min()],
        'sum' : [ls.sum(axis=0).tolist(), ls.sum(axis=1).tolist(), ls.sum()]
    }

    return calculates