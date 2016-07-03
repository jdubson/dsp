[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

### Explanation ###
This exercise is used to determine the percentage of the male population who fall in the height range of 5'10" and 6'1". It is assumed that the distribution of heights is roughly normal. To solve this, I created a normal distribution using the given mu and sigma. To get the percentage I took the difference of the CDF for the high and low heights, which gives the percentage under the created normal distribution that falls in the height range.

In this case, the percentage of the male population is ~34.27%.

### Code ###
```python
from __future__ import print_function

import sys
from operator import itemgetter

import first
import scipy.stats

def main(script):
    # Parameters
    mu = 178
    sigma = 7.7

    # Normal distribution
    dist = scipy.stats.norm(loc=mu, scale=sigma)

    # Heights
    low = dist.cdf(177.8)   #5'10" in cm
    high = dist.cdf(185.42) #6'1" in cm

    perc_in_range = (high - low) * 100

    print('Percentage of U.S. males in range:', perc_in_range)


    print('%s: All tests passed.' % script)

if __name__ == '__main__':
    main(*sys.argv)
```
