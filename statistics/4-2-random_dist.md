[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

### Explanation ###

For this exercise we are determining if the random.random function in Python is uniform. To do this I generate 1000 random numbers using the function and plot their PMF and CDF.

Based on the PMF and CDF plot, random.random is uniform. The PMF plot fills up almost the entire plot, which is expected for a uniform distribution. The CDF is roughly linear, which is also an indication for a uniform distribution.

### Code ###

```python
from __future__ import print_function

import sys
from operator import itemgetter

import first
import thinkstats2
import thinkplot
import random

def main(script):
    rand_num = [random.random() for x in range(1000)]

    pmf = thinkstats2.Pmf(rand_num, label = 'pmf')
    cdf = thinkstats2.Cdf(rand_num, label = 'cdf')

    thinkplot.Pmf(pmf, linewidth=0.1)
    thinkplot.Save(root='rand_pmf',
                   title='Random Number PMF',
                   xlabel='Number',
                   ylabel='PMF')

    thinkplot.Cdf(cdf)
    thinkplot.Save(root='rand_cdf',
                   title='Random Number CDF',
                   xlabel='Number',
                   ylabel='CDF')

    print('%s: All tests passed.' % script)

if __name__ == '__main__':
    main(*sys.argv)
```

### Results ###
![pmf](https://cloud.githubusercontent.com/assets/18509634/16541887/ee20e5a6-4046-11e6-908e-13bce3fc9e8f.jpg)
![cdf](https://cloud.githubusercontent.com/assets/18509634/16541888/f22b292c-4046-11e6-888e-03a308751bbc.jpg)
