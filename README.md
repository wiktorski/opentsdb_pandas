opentsdb_pandas
===============

This module provides methods to fetch data from OpenTSDB HTTP interface and convert them into Pandas Timeseries object.
Basic structure is based mostly on opentsdbr library.

Example usage
-------------

import opentsdb_pandas as opd

import datetime as dt

ts1 = opd.ts_get('cipsi.test1.temperature', dt.datetime(2013, 4, 3, 14, 10), dt.datetime(2013, 4, 10, 11, 30), 'node=0024C3145172746B', hostname='opentsdb.at.your.place.edu')

ts1

2013-04-03 17:08:12    30.160000

2013-04-03 17:09:12    30.139999

2013-04-03 17:10:12    30.150000

...

2013-04-10 11:27:57    29.270000

2013-04-10 11:28:58    29.280001

2013-04-10 11:29:58    29.280001

Length: 5514, dtype: float64



help(opd)

help(opd.ts_get)