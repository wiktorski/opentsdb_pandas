opentsdb_pandas
===============

This module provides methods to fetch data from OpenTSDB HTTP interface and convert them into Pandas Timeseries object.
Basic structure is based mostly on opentsdbr library.

Example usage
-------------

import opentsdb_pandas as opd

ts1 = opd.ts_get('cipsi.test1.temperature', dt.datetime(2013, 4, 3, 14, 10), dt.datetime(2013, 4, 10, 11, 30), 'node=0024C3145172746B', hostname='opentsdb.at.your.place.edu')

ts1

help(opd)

help(opd.ts_get)