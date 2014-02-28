"""

This module provides tests (pytest) for methods in opentsdb_pandas module (to fetch data from OpenTSDB HTTP interface and convert them into Pandas Timeseries object)

(Most of) these tests rely on an external installation of OpenTSDB with a very specific set of data,
if you test this in a different environment you will most probably have to modify the tests 
to reflect different OpenTSDB location, metric, etc., and of course expected results
however, the general test structure should remain unchanges

2014.02, Tomasz Wiktor Wlodarczyk, University of Stavanger, Norway
"""

import opentsdb_pandas as opd
import datetime as dt
import pytest
import urllib2

def test_basic_with_trim(): #assumes all default values except hostname and tag: agg='avg', rate=False, downsample='', port=4242, trim=True
  ts1 = opd.ts_get('cipsi.seeds.test1.temperature', dt.datetime(2013, 04, 03), dt.datetime(2013, 04, 10), 'node=0013A2004061646F', hostname='haisen23.ux.uis.no')
  assert len(ts1) == 5607

def test_basic_without_trim():
  ts1 = opd.ts_get('cipsi.seeds.test1.temperature', dt.datetime(2013, 04, 03), dt.datetime(2013, 04, 10), 'node=0013A2004061646F', hostname='haisen23.ux.uis.no', trim=False)
  assert len(ts1) == 5728

def test_wrong_time_span():
  ts1 = opd.ts_get('cipsi.seeds.test1.temperature', dt.datetime(2015, 04, 03), dt.datetime(2015, 04, 10), 'node=0013A2004061646F', hostname='haisen23.ux.uis.no')
  assert len(ts1) == 0
  
def test_wrong_metric_name():
  with pytest.raises(urllib2.HTTPError):
    ts1 = opd.ts_get('cipsi.seeds.test1.temperaturewrong', dt.datetime(2013, 04, 03), dt.datetime(2013, 04, 10), 'node=0013A2004061646F', hostname='haisen23.ux.uis.no', trim=False)
    
def test_wrong_tag():
  with pytest.raises(urllib2.HTTPError):
    ts1 = opd.ts_get('cipsi.seeds.test1.temperature', dt.datetime(2013, 04, 03), dt.datetime(2013, 04, 10), 'nodes=0013A2004061646F', hostname='haisen23.ux.uis.no', trim=False)

def test_wrong_host():
  with pytest.raises(urllib2.URLError):
    ts1 = opd.ts_get('cipsi.seeds.test1.temperature', dt.datetime(2013, 04, 03), dt.datetime(2013, 04, 10), 'nodes=0013A2004061646F', hostname='haisen23.ux.ui.no', trim=False)

