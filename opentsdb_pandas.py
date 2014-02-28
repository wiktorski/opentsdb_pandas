"""

This module provides methods to fetch data from OpenTSDB HTTP interface and convert them into Pandas Timeseries object.

2014.02, Tomasz Wiktor Wlodarczyk, University of Stavanger, Norway
"""

import pandas as pd
import urllib2
import datetime as dt


def ts_get(metric, start, end, tags='', agg='avg', rate=False, downsample='', hostname='localhost', port=4242, trim=True):
  """
  This function returns a Pandas Timeseries object with data fetched from OpenTSDB basing on the provided parameters.
  If there are no results it returns an empty Pandas Series, in case of any other exception it throws that exception.
  
  Parameters:
  metric - metric name as in OpenTSDB, one metric only, e.g. 'cipsi.test1.temperature'
  start, end - start and end time for the query, should be of type datetime from datetime module, e.g. dt.datetime(2013, 4, 3, 14, 10), assuming: import datetime as dt
  tags - tags formatted according to OpenTSDB specification e.g. 'host=foo,type=user|system'
  agg - aggregate function to be used, default is 'avg', options are min, sum, max, avg
  rate - specifies if rate should be calculated instead of raw data, default False
  downsample - specifies downsample function and interval in OpenTSDB format, default none, e.g. '60m-avg'
  trim - specifies if values received from OpneTSDB should be trimed to exactly match start and end parameters, OpenTSDB by default returns additional values before the start and after the end
  
  Example useage:
  import opentsdb_pandas as opd
  ts1 = opd.ts_get('cipsi.test1.temperature', dt.datetime(2013, 4, 3, 14, 10), dt.datetime(2013, 4, 10, 11, 30), 'node=0024C3145172746B', hostname='opentsdb.at.your.place.edu')
  ts1
  """
  url = "http://%s:%s/q?start=%s&end=%s&m=%s%s%s:%s{%s}&ascii" %(hostname,port,start.strftime("%Y/%m/%d-%H:%M:%S"),end.strftime("%Y/%m/%d-%H:%M:%S"), agg , ':'+downsample if downsample.strip() else '', ':rate' if rate else '', metric, tags)
  answer = urllib2.urlopen(url).read().strip()
  if answer:
    answer_by_line = answer.split('\n')
  else:
    return pd.Series()
  ti = [dt.datetime.fromtimestamp(int(x.split(' ')[1])) for x in answer_by_line]
  val = [float(x.split(' ')[2]) for x in answer_by_line]
  ts = pd.Series(val, ti)
  if trim:
    ts = ts.ix[(ts.index >= start) & (ts.index <= end)]
  return ts

