title: Quick Sort
lang: it
tags: python
Category: Python
Date: 2012-05-09 08:44


Non è molto performante ma illustra le capacità di linguaggio funzionale di Python

    def qs(x):
        return x if len(x)<2 else qs(filter(lambda y: y<=x[-1],x[:-1]))+[x[-1]]+qs(filter(lambda y: y>x[-1] ,x[:-1]))