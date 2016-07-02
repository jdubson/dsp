[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

### Explanation ###

This exercise explores the observation of how certain types of surveys like the class size in a university can lead to a biased distribution compared to the actual distribution. This exercise explores such a paradox for how many children are in a family.

In order to see the paradox, I created a PMF of the actual distribution and then a PMF of the biased distribution which is created by multiplying the probability for each number of children per family by the number of children who observe that family size. The plot of the distributions below shows that the biased distribution is shifted to the right.

### Code ###

```python
from __future__ import print_function

import sys
from operator import itemgetter

import first
import thinkstats2
import thinkplot
import chap01soln

def ActualDist(resp):
    pmf = thinkstats2.Pmf(resp.numkdhh, label='actual')
    print('actual mean', pmf.Mean())

    return pmf

def BiasDist(pmf):
    new_pmf = pmf.Copy(label='biased')

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)

    new_pmf.Normalize()
    print('biased mean', new_pmf.Mean())

    return new_pmf

def MakeComparison(pmf, biased):
    thinkplot.PrePlot(2)
    thinkplot.Pmfs([pmf, biased])
    thinkplot.Save(root='actual_vs_biased',
                   title='Actual vs Biased',
                   xlabel='Number of Children (under 18)',
                   ylabel='PMF')

def main(script):
    resp = chap01soln.ReadFemResp()

    pmf = ActualDist(resp)
    biased = BiasDist(pmf)

    MakeComparison(pmf, biased)

    print('%s: All tests passed.' % script)

if __name__ == '__main__':
    main(*sys.argv)
```

### Results ###
![](https://cloud.githubusercontent.com/assets/18509634/16541748/e75cfe86-4040-11e6-942a-8023d9c726e2.jpg)
