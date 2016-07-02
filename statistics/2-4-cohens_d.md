[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

## Explanation ##

To compare Cohen's d for the weight difference and pregnancy lengths of first versus other babies I use the following steps. First I created data frames for first and other babies data. Then I calculated the mean, variance, and Cohen's d using its formula (the code for the calculations can be found below). Using the results I compared the Cohen's d for weight difference and pregancy lengths.

Cohen's d for weight difference is -0.0886729270726, while Cohen's d for pregnancy lengths is 0.0288790446544. Cohen's d is positive showing that first baby pregnancy lengths are slightly longer, while the Cohen's d for weight difference is negative showing that first baby weights are lighter. Cohen's d is closer to 0 for pregnancy length, but both are small and show there is little difference in these categories between first and other babies. 

## Code ##
```python
"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import sys
from operator import itemgetter

import first
import thinkstats2
import math
import thinkplot

def WeightDifference(firsts, others):
    """Explore the difference in weight between first babies and others.

    firsts: DataFrame of first babies
    others: DataFrame of others
    """

    mean1 = firsts.totalwgt_lb.mean()
    mean2 = others.totalwgt_lb.mean()

    var1 = firsts.totalwgt_lb.var()
    var2 = others.totalwgt_lb.var()

    diff = mean1 - mean2
    n1, n2 = len(firsts.totalwgt_lb), len(others.totalwgt_lb)
    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)

    d = diff / math.sqrt(pooled_var)

    print('Weight Difference\n')

    print('Mean')
    print('First babies', mean1)
    print('Other babies', mean2)
    print('Difference', diff)
    print('\n')

    print('Variance')
    print('First babies', var1)
    print('Other babies', var2)
    print('\n')

    print('Cohen d', d)
    print('\n')

def PregLenDifference(firsts, others):
    """Explore the difference in pregnancy length between first babies and others.

    firsts: DataFrame of first babies
    others: DataFrame of others
    """

    p_mean1 = firsts.prglngth.mean()
    p_mean2 = others.prglngth.mean()

    p_var1 = firsts.prglngth.var()
    p_var2 = others.prglngth.var()


    p_diff = p_mean1 - p_mean2
    p_n1, p_n2 = len(firsts.prglngth), len(others.prglngth)
    p_pooled_var = (p_n1 * p_var1 + p_n2 * p_var2) / (p_n1 + p_n2)

    p_d = p_diff / math.sqrt(p_pooled_var)

    print('Pregnancy Length Difference\n')

    print('Mean')
    print('First babies', p_mean1)
    print('Other babies', p_mean2)
    print('Difference', p_diff)
    print('\n')

    print('Variance')
    print('First babies', p_var1)
    print('Other babies', p_var2)
    print('\n')

    print('Cohen d', p_d)
    print('\n')
    
    def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    live, firsts, others = first.MakeFrames()

    # explore the weight difference between first babies and others
    WeightDifference(firsts, others)

    # explore the pregnancy length difference between first babies and others
    PregLenDifference(firsts, others)

    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
```

## Results ##
### Weight Difference ###

**Mean**

First babies 7.20109443044

Other babies 7.32585561497

Difference -0.124761184535

**Variance**

First babies 2.01802730092

Other babies 1.9437810259


**Cohen d** -0.0886729270726

### Pregnancy Length Difference ###

**Mean**

First babies 38.6009517335

Other babies 38.5229144667

Difference 0.0780372667775

**Variance**

First babies 7.79471350923

Other babies 6.8426835193

**Cohen d** 0.0288790446544
