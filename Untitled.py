Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 26 2016, 10:47:25) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

>>> import
SyntaxError: invalid syntax
>>>  import os
 
SyntaxError: unexpected indent
>>> import os
>>> os.getcwd()
'/Users/tata/Documents'
>>> import pandas
>>> df = pandas.read_excel('ChartSwap.xlsx')
>>> print df.columns
SyntaxError: Missing parentheses in call to 'print'
>>> print(df.columns)
Index(['Account Site', 'Account Name', 'Attention', 'Date Range',
       'Record Types Available'],
      dtype='object')
>>> values = df['Account Site'].values
>>> print(values)
['Alabama' 'Alabama' 'Alabama' ..., 'Wyoming' 'Wyoming' 'Wyoming']
>>> for i in values:
	if i == 'Washington':
		print(i)

		
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Washington
Traceback (most recent call last):
  File "<pyshell#14>", line 3, in <module>
    print(i)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/idlelib/PyShell.py", line 1344, in write
    return self.shell.write(s, self.tags)
KeyboardInterrupt
>>> help(pandas)
Help on package pandas:

NAME
    pandas

DESCRIPTION
    pandas - a powerful data analysis and manipulation library for Python
    =====================================================================
    
    See http://pandas.pydata.org/ for full documentation. Otherwise, see the
    docstrings of the various objects in the pandas namespace:
    
    Series
    DataFrame
    Panel
    Index
    DatetimeIndex
    HDFStore
    bdate_range
    date_range
    read_csv
    read_fwf
    read_table
    ols

PACKAGE CONTENTS
    _hash
    _join
    _period
    _sparse
    _testing
    _version
    _window
    algos
    api (package)
    compat (package)
    computation (package)
    core (package)
    formats (package)
    hashtable
    index
    indexes (package)
    info
    io (package)
    json
    lib
    msgpack (package)
    parser
    rpy (package)
    sparse (package)
    stats (package)
    tests (package)
    tools (package)
    tseries (package)
    tslib
    types (package)
    util (package)

SUBMODULES
    offsets

DATA
    IndexSlice = <pandas.core.indexing._IndexSlice object>
    NaT = NaT
    __docformat__ = 'restructuredtext'
    datetools = <module 'pandas.core.datetools' from '/Library/F...ython3....
    describe_option = <pandas.core.config.CallableDynamicDoc object>
    get_option = <pandas.core.config.CallableDynamicDoc object>
    options = <pandas.core.config.DictWrapper object>
    plot_params = {'xaxis.compat': False}
    reset_option = <pandas.core.config.CallableDynamicDoc object>
    set_option = <pandas.core.config.CallableDynamicDoc object>

VERSION
    0.19.2

FILE
    /Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/pandas/__init__.py


>>> for i in values:
	if i == 'Washington':
		print(values[i])

		

Warning (from warnings module):
  File "__main__", line 3
VisibleDeprecationWarning: using a non-integer number instead of an integer will result in an error in the future
Traceback (most recent call last):
  File "<pyshell#19>", line 3, in <module>
    print(values[i])
IndexError: only integers, slices (`:`), ellipsis (`...`), numpy.newaxis (`None`) and integer or boolean arrays are valid indices
>>> values = df['Account Site'].values
>>> print(values)
['Alabama' 'Alabama' 'Alabama' ..., 'Wyoming' 'Wyoming' 'Wyoming']
>>> df
      Account Site                                    Account Name  \
0          Alabama               Albert Rains Emergency Physicians   
1          Alabama                              ARIS Teleradiology   
2          Alabama                 Ashford Ambulance & Rescue Inc.   
3          Alabama                 BALDWIN EMERGENCY PHYSICIANS PC   
4          Alabama                 BALDWIN EMERGENCY PHYSICIANS PC   
5          Alabama                   Bankhead Emergency Physicians   
6          Alabama                   Bankhead Emergency Physicians   
7          Alabama                Bichir Emergency Physicians, LLC   
8          Alabama                                 Butler ER Group   
9          Alabama    Buttahatchee River Emergency Physicians, LLC   
10         Alabama                         Calhoun Emergency Group   
11         Alabama                                Calhoun ER Group   
12         Alabama                   Camellia Emergency Physicians   
13         Alabama                  Cardiology Associates of Ozark   
14         Alabama                     Carney Emergency Physicians   
15         Alabama                        Champion Sports Medicine   
16         Alabama              Cherokee Emergency Medical Service   
17         Alabama                     City of Albertville Amb Svc   
18         Alabama                                    City of Boaz   
19         Alabama                            City of Jacksonville   
20         Alabama                        City of Lanett Ambulance   
21         Alabama                                   City of Ozark   
22         Alabama                              City of Valley EMS   
23         Alabama                        Clay County Rescue Squad   
24         Alabama                           Clayton Fire & Rescue   
25         Alabama                             Cleburne County EMS   
26         Alabama                               Clio Rescue Squad   
27         Alabama                                Colbert ER Group   
28         Alabama                    Crimson Emergency Physicians   
29         Alabama  Daleville Police Volunteer Rescue Service Inc.   
...            ...                                             ...   
15691      Wyoming                                       Chugwater   
15692      Wyoming                                DAKOTA RADIOLOGY   
15693      Wyoming                                DAKOTA RADIOLOGY   
15694      Wyoming                                DAKOTA RADIOLOGY   
15695      Wyoming                                DAKOTA RADIOLOGY   
15696      Wyoming          DBA ST JOHNS MEDICAL CTR ER PHYSICIANS   
15697      Wyoming     Emergency Physicians Integrated Care (EPIC)   
15698      Wyoming                   Evanston Emergency Physicians   
15699      Wyoming                      Gregrory P Clifford MD, PC   
15700      Wyoming                                 Hawk Springs FD   
15701      Wyoming                         Jackson Hole Fire / EMS   
15702      Wyoming                                        Mills FD   
15703      Wyoming               Oregon Trail Emergency Physicians   
15704      Wyoming               Osage Volunteer Ambulance Service   
15705      Wyoming                       OutPatient Radiology, LLC   
15706      Wyoming                       Peak Emergency Physicians   
15707      Wyoming                       Peak Emergency Physicians   
15708      Wyoming                               Pine Bluffs - EMS   
15709      Wyoming                    Rangeland Inpatient Services   
15710      Wyoming                         ST JOHNS MEDICAL CENTER   
15711      Wyoming                              Tensleep Ambulance   
15712      Wyoming                    Trailhead Inpatient Services   
15713      Wyoming         Union Pacific Emergency Physicians, LLC   
15714      Wyoming             White Mountain Emergency Physicians   
15715      Wyoming                            WIND RIVER RADIOLOGY   
15716      Wyoming                            WIND RIVER RADIOLOGY   
15717      Wyoming                            WIND RIVER RADIOLOGY   
15718      Wyoming                            WIND RIVER RADIOLOGY   
15719      Wyoming                            WIND RIVER RADIOLOGY   
15720      Wyoming                            WIND RIVER RADIOLOGY   

                                               Attention  \
0                      Riverview Regional Medical Center   
1                                    Grove Hill Memorial   
2                                                    NaN   
3                         SOUTH BALDWIN REGIONAL MEDICAL   
4                                        THOMAS HOSPITAL   
5                                 Parkway Medical Center   
6                         Stringfellow Memorial Hospital   
7                               Wiregrass Medical Center   
8                         L.V. Stabler Memorial Hospital   
9                   Marion Regional Medical Center, Inc.   
10                           Jacksonville Medical Center   
11                           Jacksonville Medical Center   
12                             Lakeview Community Center   
13                                   Dale Medical Center   
14                             Atmore Community Hospital   
15                                 All Alabama Locations   
16                                                   NaN   
17                                                   NaN   
18                                                   NaN   
19                                                   NaN   
20                                                   NaN   
21                                                   NaN   
22                                                   NaN   
23                                                   NaN   
24                                                   NaN   
25                                                   NaN   
26                                                   NaN   
27                                       Shoals Hospital   
28                                   Dale Medical Center   
29                                                   NaN   
...                                                  ...   
15691                                                NaN   
15692  * USE FOR UNKNOWN, UNLISTED OR MULTIPLE LOCATI...   
15693                     Crook County Memorial Hospital   
15694                  Regional Medical Clinic Newcastle   
15695                             WESTON COUNTY HOSPITAL   
15696                            ST JOHNS MEDICAL CENTER   
15697                         Evanston Regional Hospital   
15698                         Evanston Regional Hospital   
15699                                 Sage West Hospital   
15700                                                NaN   
15701                                                NaN   
15702                                                NaN   
15703                    Mountain View Regional Hospital   
15704                                                NaN   
15705                               OutPatient Radiology   
15706               Memorial Hospital of Converse County   
15707               Memorial Hospital of Converse County   
15708                                                NaN   
15709                      Weston County Health Services   
15710                            ST JOHNS MEDICAL CENTER   
15711                                                NaN   
15712               Memorial Hospital of Converse County   
15713                   Cheyenne Regional Medical Center   
15714                    Memorial Hospital of Sweetwater   
15715                           LANDER REGIONAL HOSPITAL   
15716                           LANDER REGIONAL HOSPITAL   
15717                              SAGE WEST HEALTH CARE   
15718                              SAGE WEST HEALTH CARE   
15719                       WYOMING LIFE RESOURCE CENTER   
15720                       WYOMING LIFE RESOURCE CENTER   

                   Date Range                   Record Types Available  
0      8/11/2008 - 11/30/2010  Emergency Physician Billing and Medical  
1        11/29/2012 - Present                        Radiology Billing  
2                NA - Present     EMS Billing and Patient Care Reports  
3        7/1/2008 - 6/30/2011              Emergency Physician Billing  
4          1/1/2005 - Present              Emergency Physician Billing  
5        12/1/2006 - 5/1/2008  Emergency Physician Billing and Medical  
6      4/10/2009 - 11/15/2010  Emergency Physician Billing and Medical  
7          9/1/2015 - Present  Emergency Physician Billing and Medical  
8        9/1/2005 - 1/21/2009              Emergency Physician Billing  
9         11/1/2015 - Present  Emergency Physician Billing and Medical  
10      9/16/2009 - 3/31/2013              Emergency Physician Billing  
11      9/16/2009 - 3/31/2013              Emergency Physician Billing  
12      8/30/2004 - 8/30/2005  Emergency Physician Billing and Medical  
13         4/1/2007 - Present                       Cardiology Billing  
14        2/1/1999 - 9/1/2000  Emergency Physician Billing and Medical  
15               NA - Present                      Medical and Billing  
16               NA - Present     EMS Billing and Patient Care Reports  
17         4/1/2013 - Present     EMS Billing and Patient Care Reports  
18               NA - Present     EMS Billing and Patient Care Reports  
19        6/28/2013 - Present     EMS Billing and Patient Care Reports  
20               NA - Present     EMS Billing and Patient Care Reports  
21               NA - Present     EMS Billing and Patient Care Reports  
22               NA - Present     EMS Billing and Patient Care Reports  
23               NA - Present     EMS Billing and Patient Care Reports  
24               NA - Present     EMS Billing and Patient Care Reports  
25               NA - Present     EMS Billing and Patient Care Reports  
26               NA - Present     EMS Billing and Patient Care Reports  
27       9/1/2010 - 1/14/2012              Emergency Physician Billing  
28       8/8/1997 - 4/15/2010  Emergency Physician Billing and Medical  
29         4/1/2013 - Present     EMS Billing and Patient Care Reports  
...                       ...                                      ...  
15691            NA - Present     EMS Billing and Patient Care Reports  
15692      1/1/2010 - Present                        Radiology Billing  
15693      1/1/2010 - Present                        Radiology Billing  
15694      1/1/2010 - Present                        Radiology Billing  
15695      1/1/2010 - Present                        Radiology Billing  
15696     10/1/2010 - Present              Emergency Physician Billing  
15697     10/1/2015 - Present              Emergency Physician Billing  
15698    2/1/2007 - 9/30/2015              Emergency Physician Billing  
15699      9/1/2015 - Present               Emergency Medicine Billing  
15700            NA - Present     EMS Billing and Patient Care Reports  
15701            NA - Present     EMS Billing and Patient Care Reports  
15702            NA - Present     EMS Billing and Patient Care Reports  
15703      6/2/2008 - Present  Emergency Physician Billing and Medical  
15704            NA - Present     EMS Billing and Patient Care Reports  
15705            NA - Present                        Radiology Billing  
15706     4/1/2013 - 4/1/2014  Emergency Physician Billing and Medical  
15707    4/22/2013 - 4/1/2014          Hospitalist Billing and Medical  
15708            NA - Present     EMS Billing and Patient Care Reports  
15709   4/1/2012 - 10/31/2015          Hospitalist Billing and Medical  
15710   11/27/2010 - 6/1/2011              Emergency Physician Billing  
15711            NA - Present     EMS Billing and Patient Care Reports  
15712  4/22/2013 - 11/30/2013          Hospitalist Billing and Medical  
15713      2/1/2014 - Present  Emergency Physician Billing and Medical  
15714    7/1/2004 - 1/31/2006  Emergency Physician Billing and Medical  
15715     10/1/2010 - Present                        Radiology Billing  
15716     10/1/2010 - Present                        Radiology Billing  
15717     10/1/2010 - Present                        Radiology Billing  
15718     10/1/2010 - Present                        Radiology Billing  
15719     10/1/2010 - Present                        Radiology Billing  
15720     10/1/2010 - Present                        Radiology Billing  

[15721 rows x 5 columns]
>>> print(df.columns)
Index(['Account Site', 'Account Name', 'Attention', 'Date Range',
       'Record Types Available'],
      dtype='object')
>>> d = ['Account Site', 'Account Name']
>>> 
>>> df[d]
      Account Site                                    Account Name
0          Alabama               Albert Rains Emergency Physicians
1          Alabama                              ARIS Teleradiology
2          Alabama                 Ashford Ambulance & Rescue Inc.
3          Alabama                 BALDWIN EMERGENCY PHYSICIANS PC
4          Alabama                 BALDWIN EMERGENCY PHYSICIANS PC
5          Alabama                   Bankhead Emergency Physicians
6          Alabama                   Bankhead Emergency Physicians
7          Alabama                Bichir Emergency Physicians, LLC
8          Alabama                                 Butler ER Group
9          Alabama    Buttahatchee River Emergency Physicians, LLC
10         Alabama                         Calhoun Emergency Group
11         Alabama                                Calhoun ER Group
12         Alabama                   Camellia Emergency Physicians
13         Alabama                  Cardiology Associates of Ozark
14         Alabama                     Carney Emergency Physicians
15         Alabama                        Champion Sports Medicine
16         Alabama              Cherokee Emergency Medical Service
17         Alabama                     City of Albertville Amb Svc
18         Alabama                                    City of Boaz
19         Alabama                            City of Jacksonville
20         Alabama                        City of Lanett Ambulance
21         Alabama                                   City of Ozark
22         Alabama                              City of Valley EMS
23         Alabama                        Clay County Rescue Squad
24         Alabama                           Clayton Fire & Rescue
25         Alabama                             Cleburne County EMS
26         Alabama                               Clio Rescue Squad
27         Alabama                                Colbert ER Group
28         Alabama                    Crimson Emergency Physicians
29         Alabama  Daleville Police Volunteer Rescue Service Inc.
...            ...                                             ...
15691      Wyoming                                       Chugwater
15692      Wyoming                                DAKOTA RADIOLOGY
15693      Wyoming                                DAKOTA RADIOLOGY
15694      Wyoming                                DAKOTA RADIOLOGY
15695      Wyoming                                DAKOTA RADIOLOGY
15696      Wyoming          DBA ST JOHNS MEDICAL CTR ER PHYSICIANS
15697      Wyoming     Emergency Physicians Integrated Care (EPIC)
15698      Wyoming                   Evanston Emergency Physicians
15699      Wyoming                      Gregrory P Clifford MD, PC
15700      Wyoming                                 Hawk Springs FD
15701      Wyoming                         Jackson Hole Fire / EMS
15702      Wyoming                                        Mills FD
15703      Wyoming               Oregon Trail Emergency Physicians
15704      Wyoming               Osage Volunteer Ambulance Service
15705      Wyoming                       OutPatient Radiology, LLC
15706      Wyoming                       Peak Emergency Physicians
15707      Wyoming                       Peak Emergency Physicians
15708      Wyoming                               Pine Bluffs - EMS
15709      Wyoming                    Rangeland Inpatient Services
15710      Wyoming                         ST JOHNS MEDICAL CENTER
15711      Wyoming                              Tensleep Ambulance
15712      Wyoming                    Trailhead Inpatient Services
15713      Wyoming         Union Pacific Emergency Physicians, LLC
15714      Wyoming             White Mountain Emergency Physicians
15715      Wyoming                            WIND RIVER RADIOLOGY
15716      Wyoming                            WIND RIVER RADIOLOGY
15717      Wyoming                            WIND RIVER RADIOLOGY
15718      Wyoming                            WIND RIVER RADIOLOGY
15719      Wyoming                            WIND RIVER RADIOLOGY
15720      Wyoming                            WIND RIVER RADIOLOGY

[15721 rows x 2 columns]
>>> df_f = df[d]
>>> for i, j in df_f:
	if i == 'Washington':
		print(j)

		
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    for i, j in df_f:
ValueError: too many values to unpack (expected 2)
>>> for (i, j) in df_f:
	print(j)

	
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    for (i, j) in df_f:
ValueError: too many values to unpack (expected 2)
>>> print(df_f)
      Account Site                                    Account Name
0          Alabama               Albert Rains Emergency Physicians
1          Alabama                              ARIS Teleradiology
2          Alabama                 Ashford Ambulance & Rescue Inc.
3          Alabama                 BALDWIN EMERGENCY PHYSICIANS PC
4          Alabama                 BALDWIN EMERGENCY PHYSICIANS PC
5          Alabama                   Bankhead Emergency Physicians
6          Alabama                   Bankhead Emergency Physicians
7          Alabama                Bichir Emergency Physicians, LLC
8          Alabama                                 Butler ER Group
9          Alabama    Buttahatchee River Emergency Physicians, LLC
10         Alabama                         Calhoun Emergency Group
11         Alabama                                Calhoun ER Group
12         Alabama                   Camellia Emergency Physicians
13         Alabama                  Cardiology Associates of Ozark
14         Alabama                     Carney Emergency Physicians
15         Alabama                        Champion Sports Medicine
16         Alabama              Cherokee Emergency Medical Service
17         Alabama                     City of Albertville Amb Svc
18         Alabama                                    City of Boaz
19         Alabama                            City of Jacksonville
20         Alabama                        City of Lanett Ambulance
21         Alabama                                   City of Ozark
22         Alabama                              City of Valley EMS
23         Alabama                        Clay County Rescue Squad
24         Alabama                           Clayton Fire & Rescue
25         Alabama                             Cleburne County EMS
26         Alabama                               Clio Rescue Squad
27         Alabama                                Colbert ER Group
28         Alabama                    Crimson Emergency Physicians
29         Alabama  Daleville Police Volunteer Rescue Service Inc.
...            ...                                             ...
15691      Wyoming                                       Chugwater
15692      Wyoming                                DAKOTA RADIOLOGY
15693      Wyoming                                DAKOTA RADIOLOGY
15694      Wyoming                                DAKOTA RADIOLOGY
15695      Wyoming                                DAKOTA RADIOLOGY
15696      Wyoming          DBA ST JOHNS MEDICAL CTR ER PHYSICIANS
15697      Wyoming     Emergency Physicians Integrated Care (EPIC)
15698      Wyoming                   Evanston Emergency Physicians
15699      Wyoming                      Gregrory P Clifford MD, PC
15700      Wyoming                                 Hawk Springs FD
15701      Wyoming                         Jackson Hole Fire / EMS
15702      Wyoming                                        Mills FD
15703      Wyoming               Oregon Trail Emergency Physicians
15704      Wyoming               Osage Volunteer Ambulance Service
15705      Wyoming                       OutPatient Radiology, LLC
15706      Wyoming                       Peak Emergency Physicians
15707      Wyoming                       Peak Emergency Physicians
15708      Wyoming                               Pine Bluffs - EMS
15709      Wyoming                    Rangeland Inpatient Services
15710      Wyoming                         ST JOHNS MEDICAL CENTER
15711      Wyoming                              Tensleep Ambulance
15712      Wyoming                    Trailhead Inpatient Services
15713      Wyoming         Union Pacific Emergency Physicians, LLC
15714      Wyoming             White Mountain Emergency Physicians
15715      Wyoming                            WIND RIVER RADIOLOGY
15716      Wyoming                            WIND RIVER RADIOLOGY
15717      Wyoming                            WIND RIVER RADIOLOGY
15718      Wyoming                            WIND RIVER RADIOLOGY
15719      Wyoming                            WIND RIVER RADIOLOGY
15720      Wyoming                            WIND RIVER RADIOLOGY

[15721 rows x 2 columns]
>>> for (i, j, k) in df_f:
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    for (i, j, k) in df_f:
ValueError: too many values to unpack (expected 3)
>>> fd_f(0)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    fd_f(0)
NameError: name 'fd_f' is not defined
>>> df_f[0]
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/pandas/indexes/base.py", line 2134, in get_loc
    return self._engine.get_loc(key)
  File "pandas/index.pyx", line 132, in pandas.index.IndexEngine.get_loc (pandas/index.c:4433)
  File "pandas/index.pyx", line 154, in pandas.index.IndexEngine.get_loc (pandas/index.c:4279)
  File "pandas/src/hashtable_class_helper.pxi", line 732, in pandas.hashtable.PyObjectHashTable.get_item (pandas/hashtable.c:13742)
  File "pandas/src/hashtable_class_helper.pxi", line 740, in pandas.hashtable.PyObjectHashTable.get_item (pandas/hashtable.c:13696)
KeyError: 0

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    df_f[0]
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/pandas/core/frame.py", line 2059, in __getitem__
    return self._getitem_column(key)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/pandas/core/frame.py", line 2066, in _getitem_column
    return self._get_item_cache(key)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/pandas/core/generic.py", line 1386, in _get_item_cache
    values = self._data.get(item)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/pandas/core/internals.py", line 3543, in get
    loc = self.items.get_loc(item)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/pandas/indexes/base.py", line 2136, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas/index.pyx", line 132, in pandas.index.IndexEngine.get_loc (pandas/index.c:4433)
  File "pandas/index.pyx", line 154, in pandas.index.IndexEngine.get_loc (pandas/index.c:4279)
  File "pandas/src/hashtable_class_helper.pxi", line 732, in pandas.hashtable.PyObjectHashTable.get_item (pandas/hashtable.c:13742)
  File "pandas/src/hashtable_class_helper.pxi", line 740, in pandas.hashtable.PyObjectHashTable.get_item (pandas/hashtable.c:13696)
KeyError: 0
>>> for i in df_f:
	if i == 'Washington':
		print(i)

		
>>> df_f
      Account Site                                    Account Name
0          Alabama               Albert Rains Emergency Physicians
1          Alabama                              ARIS Teleradiology
2          Alabama                 Ashford Ambulance & Rescue Inc.
3          Alabama                 BALDWIN EMERGENCY PHYSICIANS PC
4          Alabama                 BALDWIN EMERGENCY PHYSICIANS PC
5          Alabama                   Bankhead Emergency Physicians
6          Alabama                   Bankhead Emergency Physicians
7          Alabama                Bichir Emergency Physicians, LLC
8          Alabama                                 Butler ER Group
9          Alabama    Buttahatchee River Emergency Physicians, LLC
10         Alabama                         Calhoun Emergency Group
11         Alabama                                Calhoun ER Group
12         Alabama                   Camellia Emergency Physicians
13         Alabama                  Cardiology Associates of Ozark
14         Alabama                     Carney Emergency Physicians
15         Alabama                        Champion Sports Medicine
16         Alabama              Cherokee Emergency Medical Service
17         Alabama                     City of Albertville Amb Svc
18         Alabama                                    City of Boaz
19         Alabama                            City of Jacksonville
20         Alabama                        City of Lanett Ambulance
21         Alabama                                   City of Ozark
22         Alabama                              City of Valley EMS
23         Alabama                        Clay County Rescue Squad
24         Alabama                           Clayton Fire & Rescue
25         Alabama                             Cleburne County EMS
26         Alabama                               Clio Rescue Squad
27         Alabama                                Colbert ER Group
28         Alabama                    Crimson Emergency Physicians
29         Alabama  Daleville Police Volunteer Rescue Service Inc.
...            ...                                             ...
15691      Wyoming                                       Chugwater
15692      Wyoming                                DAKOTA RADIOLOGY
15693      Wyoming                                DAKOTA RADIOLOGY
15694      Wyoming                                DAKOTA RADIOLOGY
15695      Wyoming                                DAKOTA RADIOLOGY
15696      Wyoming          DBA ST JOHNS MEDICAL CTR ER PHYSICIANS
15697      Wyoming     Emergency Physicians Integrated Care (EPIC)
15698      Wyoming                   Evanston Emergency Physicians
15699      Wyoming                      Gregrory P Clifford MD, PC
15700      Wyoming                                 Hawk Springs FD
15701      Wyoming                         Jackson Hole Fire / EMS
15702      Wyoming                                        Mills FD
15703      Wyoming               Oregon Trail Emergency Physicians
15704      Wyoming               Osage Volunteer Ambulance Service
15705      Wyoming                       OutPatient Radiology, LLC
15706      Wyoming                       Peak Emergency Physicians
15707      Wyoming                       Peak Emergency Physicians
15708      Wyoming                               Pine Bluffs - EMS
15709      Wyoming                    Rangeland Inpatient Services
15710      Wyoming                         ST JOHNS MEDICAL CENTER
15711      Wyoming                              Tensleep Ambulance
15712      Wyoming                    Trailhead Inpatient Services
15713      Wyoming         Union Pacific Emergency Physicians, LLC
15714      Wyoming             White Mountain Emergency Physicians
15715      Wyoming                            WIND RIVER RADIOLOGY
15716      Wyoming                            WIND RIVER RADIOLOGY
15717      Wyoming                            WIND RIVER RADIOLOGY
15718      Wyoming                            WIND RIVER RADIOLOGY
15719      Wyoming                            WIND RIVER RADIOLOGY
15720      Wyoming                            WIND RIVER RADIOLOGY

[15721 rows x 2 columns]
>>> for i in df_f:
	if df_f['Account Site'][i] == 'Washington':
		print(df_f['Account Name'][i])

		
Traceback (most recent call last):
  File "pandas/index.pyx", line 154, in pandas.index.IndexEngine.get_loc (pandas/index.c:4279)
  File "pandas/src/hashtable_class_helper.pxi", line 404, in pandas.hashtable.Int64HashTable.get_item (pandas/hashtable.c:8543)
TypeError: an integer is required

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#49>", line 2, in <module>
    if df_f['Account Site'][i] == 'Washington':
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/pandas/core/series.py", line 603, in __getitem__
    result = self.index.get_value(self, key)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/pandas/indexes/base.py", line 2169, in get_value
    tz=getattr(series.dtype, 'tz', None))
  File "pandas/index.pyx", line 98, in pandas.index.IndexEngine.get_value (pandas/index.c:3557)
  File "pandas/index.pyx", line 106, in pandas.index.IndexEngine.get_value (pandas/index.c:3240)
  File "pandas/index.pyx", line 156, in pandas.index.IndexEngine.get_loc (pandas/index.c:4363)
KeyError: 'Account Site'
>>> for i in pf.index:
	if pd['Account Site'][i] == 'Washington':
		print(pd['Account Name'][i])

		
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    for i in pf.index:
NameError: name 'pf' is not defined
>>> for i in pd.index:
	if pd['Account Site'][i] == 'Washington':
		print(pd['Account Name'][i])

		
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    for i in pd.index:
NameError: name 'pd' is not defined
>>> for i in df.index:
	if df['Account Site'][i] == 'Washington':
		print(df['Account Name'][i])

		
ADVANCED OPEN IMAGING
ADVANCED OPEN IMAGING
ADVANCED OPEN IMAGING
ADVANCED OPEN IMAGING
AMERICAN MEDICAL RESPONSE
Ballard Emergency Physicians
Ballard Emergency Physicians PS
Beezley Springs Inpatient Services
Beezley Springs Inpatient Services
Black Hill Emergency Physiicans
Black Hill Emergency Physiicans
Bridgeport Ambulance
Cascade Emergency Physicians
Cascade Radiology Consultants
Cascade Radiology Consultants
Cascade Radiology Consultants
Cascade Radiology Consultants
Cascade Radiology Consultants
Cedra Emergency Physicians
Cedra Emergency Physicians
CEP AMERICA LLC
City of Mukilteo Fire Department
COLUMBIA BASIN IMAGING, P.C
Columbia Valley Emergency Physicians
Columbia Valley Emergency Physicians
Cowiche Creek Emergency Physicians
Cowiche Creek Emergency Physicians
Direct Radiology
Direct Radiology
Discovery Coast Emergency Physicians
Discovery Coast Emergency Physicians
Eastside Emergency Physicians, PLLC
Eastside Emergency Physicians, PLLC
Eastside Emergency Physicians, PLLC
Emergency Physicians Services
EVERETT RADIA LLC
EVERETT RADIA LLC
EVERETT RADIA LLC
EVERETT RADIA LLC
EVERGREEN RADIA LLC
EVERGREEN RADIA LLC
Gage Inpatient Physicians
Gage Inpatient Physicians
Galen Inpatient Services
Galen Inpatient Services
GEPS PHYSICIAN GROUP OF PENNSYLVANIA PC
GEPS PHYSICIAN GROUP OF PENNSYLVANIA PC
GEPS PHYSICIAN GROUP OF PENNSYLVANIA PC
Highline Emergency Physicians
HMC, DBA HIGHLINE IMAGING
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
INTEGRA IMAGING BUSINESS ASSOCIATES
KADLEC MEDICAL ASSOCIATES
KENNEWICK RADIOLOGY GROUP PC
Lake Tye Emergency Physicians
Lake Tye Emergency Physicians
Lewis County Emergency Physicians
MEDICAL INSIGHTS DIAGNOSTIC CENTERS
Monroe Inpatient Services , PLLC
Monroe Inpatient Services , PLLC
Mount Baker Imaging (MBI)
Mt. Rainier Emergency Physicians, PLLC
North Sound Emergency Medicine
North Sound Emergency Medicine
NORTHWEST EMERG PHYS
NORTHWEST EMERG PHYS
NORTHWEST EMERG PHYS INC
NORTHWEST EMERG PHYS INC
NORTHWEST EMERG PHYS INC
NORTHWEST EMERG PHYS INC
NORTHWEST EMERG PHYS INC
NORTHWEST EMERG PHYS INC
NORTHWEST EMERGENCY PHYS
NORTHWEST EMERGENCY PHYSICIANS
NORTHWEST EMERGENCY PHYSICIANS
NORTHWEST EMERGENCY PHYSICIANS
NORTHWEST EMERGENCY PHYSICIANS
Northwest Pacific Emergency Physicians, LLP
Northwest Radiologists (NWR)
Northwest Radiologists (NWR)
Northwest Radiologists (NWR)
Northwest Radiologists (NWR)
Northwest Radiologists (NWR)
Northwest Radiologists (NWR)
Northwest Radiologists (NWR)
Northwest Radiologists (NWR)
Northwest Radiologists (NWR)
Northwest Radiologists (NWR)
Okanogan Emergency Physicians
Okanogan Emergency Physicians
OLYMPIC MEDICAL IMAGING CONSULTANTS
OLYMPIC MEDICAL IMAGING CONSULTANTS
OLYMPIC MEDICAL IMAGING CONSULTANTS
OLYMPIC MEDICAL IMAGING CONSULTANTS
OLYMPIC MEDICAL IMAGING CONSULTANTS
OLYMPIC MEDICAL IMAGING CONSULTANTS
Olympic Medical Imaging Consultants, PLLC
Olympic Medical Imaging Consultants, PLLC
Olympic Medical Imaging Consultants, PLLC
Olympic Medical Imaging Consultants, PLLC
Olympic Medical Imaging Consultants, PLLC
Olympic Medical Imaging Consultants, PLLC
Olympic Medical Imaging Consultants, PLLC
Olympic Medical Imaging Consultants, PLLC
Olympic Medical Imaging Consultants, PLLC
Olympic Medical Imaging Consultants, PLLC
Olympic Medical Imaging Consultants, PLLC
Olympic Medical Imaging Consultants, PLLC
Olympic Medical Imaging Consultants, PLLC
OVERLAKE IMAGING ASSOCIATES
OVERLAKE IMAGING ASSOCIATES
OVERLAKE IMAGING ASSOCIATES
OVERLAKE IMAGING ASSOCIATES
OVERLAKE IMAGING ASSOCIATES
OVERLAKE IMAGING ASSOCIATES
OVERLAKE IMAGING ASSOCIATES
OVERLAKE IMAGING ASSOCIATES
OVERLAKE IMAGING ASSOCIATES
PATHOLOGIST REGIONAL LABORATORY
Pend Oreille River Emergency Physicians, PLLC
Pend Oreille River Emergency Physicians, PLLC
Physiotherapy Associates
Plateau Emergency Physicians
Plateau Emergency Physicians
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
RADIA INC PS
Rural/Metro of Greater Seattle, Inc.
Scheuber Road Emergency Physicians
Scheuber Road Emergency Physicians
Seahawk Emergency Physicians
Seahawk Emergency Physicians
Seattle Emergency Physicians
Seattle Emergency Physicians
Seattle Nuclear Medicine (SNM)
Seattle Nuclear Medicine (SNM)
Seattle Nuclear Medicine (SNM)
Sedro-Woolley Emergency Physicians
Sedro-Woolley Emergency Physicians
SOUTH SOUND RADIOLOGY
SOUTH SOUND RADIOLOGY
SOUTH SOUND RADIOLOGY
SOUTH SOUND RADIOLOGY
SOUTH SOUND RADIOLOGY
SOUTH SOUND RADIOLOGY
SOUTH SOUND RADIOLOGY
SOUTH SOUND RADIOLOGY
SOUTH SOUND RADIOLOGY
SOUTH SOUND RADIOLOGY
SOUTH SOUND RADIOLOGY
SOUTH SOUND RADIOLOGY
SOUTH SOUND RADIOLOGY
SOUTH SOUND RADIOLOGY
SOUTH SOUND RADIOLOGY
SOUTH SOUND RADIOLOGY
SOUTH SOUND RADIOLOGY
SOUTH SOUND RADIOLOGY
SOUTH SOUND RADIOLOGY
SOUTH SOUND RADIOLOGY
SOUTH SOUND RADIOLOGY
SOUTH SOUND RADIOLOGY
SOUTH SOUND RADIOLOGY
SOUTH SOUND RADIOLOGY
SOUTH SOUND RADIOLOGY
SOUTH SOUND RADIOLOGY
Southland Hospitalist
Spokane Emergency Physicians
Spokane Tribal Emergency Response
Stewards Inpatient Services
Stewards Inpatient Services
SWEDISH RADIA EDMONDS
SWEDISH RADIA EDMONDS
SWEDISH RADIA EDMONDS
SWEDISH RADIA EDMONDS
Tacoma Emergency Care Physicians, Inc., P.S.
Tacoma Emergency Care Physicians, Inc., P.S.
Tacoma Emergency Care Physicians, Inc., P.S.
Thurston ER Group
TRI-CITY RADIOLOGY, INC
Tri-State Hospitalist Group
Tri-State Hospitalist Group
West Sound Emergency Physicians
West Sound Emergency Physicians
Yakima Emergency Group
>>> for i in df.index:
	if df['Account Site'][i] == 'Washington':
		print(df['Account Name'][i], df['Attantion'][i])

		
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/pandas/indexes/base.py", line 2134, in get_loc
    return self._engine.get_loc(key)
  File "pandas/index.pyx", line 132, in pandas.index.IndexEngine.get_loc (pandas/index.c:4433)
  File "pandas/index.pyx", line 154, in pandas.index.IndexEngine.get_loc (pandas/index.c:4279)
  File "pandas/src/hashtable_class_helper.pxi", line 732, in pandas.hashtable.PyObjectHashTable.get_item (pandas/hashtable.c:13742)
  File "pandas/src/hashtable_class_helper.pxi", line 740, in pandas.hashtable.PyObjectHashTable.get_item (pandas/hashtable.c:13696)
KeyError: 'Attantion'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#59>", line 3, in <module>
    print(df['Account Name'][i], df['Attantion'][i])
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/pandas/core/frame.py", line 2059, in __getitem__
    return self._getitem_column(key)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/pandas/core/frame.py", line 2066, in _getitem_column
    return self._get_item_cache(key)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/pandas/core/generic.py", line 1386, in _get_item_cache
    values = self._data.get(item)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/pandas/core/internals.py", line 3543, in get
    loc = self.items.get_loc(item)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/pandas/indexes/base.py", line 2136, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas/index.pyx", line 132, in pandas.index.IndexEngine.get_loc (pandas/index.c:4433)
  File "pandas/index.pyx", line 154, in pandas.index.IndexEngine.get_loc (pandas/index.c:4279)
  File "pandas/src/hashtable_class_helper.pxi", line 732, in pandas.hashtable.PyObjectHashTable.get_item (pandas/hashtable.c:13742)
  File "pandas/src/hashtable_class_helper.pxi", line 740, in pandas.hashtable.PyObjectHashTable.get_item (pandas/hashtable.c:13696)
KeyError: 'Attantion'
>>> for i in df.index:
	if df['Account Site'][i] == 'Washington':
		print(df['Account Name'][i], df['Attention'][i])

		
ADVANCED OPEN IMAGING * USE FOR UNKNOWN, UNLISTED OR MULTIPLE LOCATIONS *
ADVANCED OPEN IMAGING ADVANCED EN IMAG
ADVANCED OPEN IMAGING ADVANCED IMAGING SVC
ADVANCED OPEN IMAGING AOI GRP HEALTH
AMERICAN MEDICAL RESPONSE nan
Ballard Emergency Physicians Swedish Medical Center/Ballard
Ballard Emergency Physicians PS Swedish Medical Center
Beezley Springs Inpatient Services Columbia Basin Hospital
Beezley Springs Inpatient Services Columbia Basin Hospital
Black Hill Emergency Physiicans Capital Medical Center
Black Hill Emergency Physiicans Capital Medical Center
Bridgeport Ambulance nan
Cascade Emergency Physicians Auburn Regional Medical Center
Cascade Radiology Consultants Cascade Valley Hospital
Cascade Radiology Consultants Darrington Clinic
Cascade Radiology Consultants Granite Falls Clinic
Cascade Radiology Consultants Skagit Valley Clinic
Cascade Radiology Consultants Smokey Point Clinic
Cedra Emergency Physicians United General Hospital
Cedra Emergency Physicians United General Hospital
CEP AMERICA LLC Swedish Edmonds
City of Mukilteo Fire Department nan
COLUMBIA BASIN IMAGING, P.C KADLEC MEDICAL CENTER
Columbia Valley Emergency Physicians Sunnyside Community Hospital
Columbia Valley Emergency Physicians Sunnyside Community Hospital
Cowiche Creek Emergency Physicians Yakima Regional Medical & Heart Center
Cowiche Creek Emergency Physicians Yakima Regional Medical & Heart Center
Direct Radiology CASCADE MEDICAL
Direct Radiology OCEAN BEACH HOSP
Discovery Coast Emergency Physicians Ocean Beach Hospital
Discovery Coast Emergency Physicians Ocean Beach Hospital
Eastside Emergency Physicians, PLLC Swedish Medical Center
Eastside Emergency Physicians, PLLC Swedish Medical Center Mill Creek
Eastside Emergency Physicians, PLLC Swedish Medical Center Redmond
Emergency Physicians Services Providence Holy Family Hospital
EVERETT RADIA LLC * USE FOR UNKNOWN, UNLISTED OR MULTIPLE LOCATIONS *
EVERETT RADIA LLC Ben Harmon MD
EVERETT RADIA LLC Everett Radia Imaging Center
EVERETT RADIA LLC Mark Mayhle MD
EVERGREEN RADIA LLC * USE FOR UNKNOWN, UNLISTED OR MULTIPLE LOCATIONS *
EVERGREEN RADIA LLC Evergreen Radia Imaging Center
Gage Inpatient Physicians TriState Memorial Hospital
Gage Inpatient Physicians TriState Memorial Hospital
Galen Inpatient Services Capital Medical Center
Galen Inpatient Services Capital Medical Center
GEPS PHYSICIAN GROUP OF PENNSYLVANIA PC * USE FOR UNKNOWN, UNLISTED OR MULTIPLE LOCATIONS *
GEPS PHYSICIAN GROUP OF PENNSYLVANIA PC Columbia Crest Center
GEPS PHYSICIAN GROUP OF PENNSYLVANIA PC Everett Center
Highline Emergency Physicians Highline Medical Center
HMC, DBA HIGHLINE IMAGING HMC, DBA HIGHLINE IMAGING
INTEGRA IMAGING BUSINESS ASSOCIATES * USE FOR UNKNOWN, UNLISTED OR MULTIPLE LOCATIONS *
INTEGRA IMAGING BUSINESS ASSOCIATES Adventist Health Medical Group
INTEGRA IMAGING BUSINESS ASSOCIATES Arthritis NW Rheumatology PLLC
INTEGRA IMAGING BUSINESS ASSOCIATES Cancer Care Northwest
INTEGRA IMAGING BUSINESS ASSOCIATES CHAS
INTEGRA IMAGING BUSINESS ASSOCIATES Columbia Medical Associates North
INTEGRA IMAGING BUSINESS ASSOCIATES Columbia Medical Associates South
INTEGRA IMAGING BUSINESS ASSOCIATES Deaconess Medical Center
INTEGRA IMAGING BUSINESS ASSOCIATES Deer Park Mobile MRI
INTEGRA IMAGING BUSINESS ASSOCIATES East Adams Rural Hospital
INTEGRA IMAGING BUSINESS ASSOCIATES Everett Clinic Gunderson Building
INTEGRA IMAGING BUSINESS ASSOCIATES Everett Clinic Harbour Pointe
INTEGRA IMAGING BUSINESS ASSOCIATES Everett Clinic Lake Stevens
INTEGRA IMAGING BUSINESS ASSOCIATES Everett Clinic Main Clinic
INTEGRA IMAGING BUSINESS ASSOCIATES Everett Clinic Marysville
INTEGRA IMAGING BUSINESS ASSOCIATES Everett Clinic Mill Creek
INTEGRA IMAGING BUSINESS ASSOCIATES Everett Clinic Silver Lake
INTEGRA IMAGING BUSINESS ASSOCIATES Everett Clinic Smokey Point
INTEGRA IMAGING BUSINESS ASSOCIATES Everett Clinic Snohomish
INTEGRA IMAGING BUSINESS ASSOCIATES Everett Clinic Stanwood
INTEGRA IMAGING BUSINESS ASSOCIATES Evergreen Hematology Oncology
INTEGRA IMAGING BUSINESS ASSOCIATES Ferry County Hospital
Traceback (most recent call last):
  File "<pyshell#61>", line 3, in <module>
    print(df['Account Name'][i], df['Attention'][i])
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/idlelib/PyShell.py", line 1344, in write
    return self.shell.write(s, self.tags)
KeyboardInterrupt
>>> for i in df.index:
	if df['Account Site'][i] == 'Washington':
		print(df['Account Name'][i], '\t',  df['Attention'][i])

		
ADVANCED OPEN IMAGING 	 * USE FOR UNKNOWN, UNLISTED OR MULTIPLE LOCATIONS *
ADVANCED OPEN IMAGING 	 ADVANCED EN IMAG
ADVANCED OPEN IMAGING 	 ADVANCED IMAGING SVC
ADVANCED OPEN IMAGING 	 AOI GRP HEALTH
AMERICAN MEDICAL RESPONSE 	 nan
Ballard Emergency Physicians 	 Swedish Medical Center/Ballard
Ballard Emergency Physicians PS 	 Swedish Medical Center
Beezley Springs Inpatient Services 	 Columbia Basin Hospital
Beezley Springs Inpatient Services 	 Columbia Basin Hospital
Black Hill Emergency Physiicans 	 Capital Medical Center
Black Hill Emergency Physiicans 	 Capital Medical Center
Bridgeport Ambulance 	 nan
Cascade Emergency Physicians 	 Auburn Regional Medical Center
Cascade Radiology Consultants 	 Cascade Valley Hospital
Cascade Radiology Consultants 	 Darrington Clinic
Cascade Radiology Consultants 	 Granite Falls Clinic
Cascade Radiology Consultants 	 Skagit Valley Clinic
Cascade Radiology Consultants 	 Smokey Point Clinic
Cedra Emergency Physicians 	 United General Hospital
Cedra Emergency Physicians 	 United General Hospital
CEP AMERICA LLC 	 Swedish Edmonds
City of Mukilteo Fire Department 	 nan
COLUMBIA BASIN IMAGING, P.C 	 KADLEC MEDICAL CENTER
Columbia Valley Emergency Physicians 	 Sunnyside Community Hospital
Columbia Valley Emergency Physicians 	 Sunnyside Community Hospital
Cowiche Creek Emergency Physicians 	 Yakima Regional Medical & Heart Center
Cowiche Creek Emergency Physicians 	 Yakima Regional Medical & Heart Center
Direct Radiology 	 CASCADE MEDICAL
Direct Radiology 	 OCEAN BEACH HOSP
Discovery Coast Emergency Physicians 	 Ocean Beach Hospital
Discovery Coast Emergency Physicians 	 Ocean Beach Hospital
Eastside Emergency Physicians, PLLC 	 Swedish Medical Center
Eastside Emergency Physicians, PLLC 	 Swedish Medical Center Mill Creek
Eastside Emergency Physicians, PLLC 	 Swedish Medical Center Redmond
Emergency Physicians Services 	 Providence Holy Family Hospital
EVERETT RADIA LLC 	 * USE FOR UNKNOWN, UNLISTED OR MULTIPLE LOCATIONS *
EVERETT RADIA LLC 	 Ben Harmon MD
EVERETT RADIA LLC 	 Everett Radia Imaging Center
EVERETT RADIA LLC 	 Mark Mayhle MD
EVERGREEN RADIA LLC 	 * USE FOR UNKNOWN, UNLISTED OR MULTIPLE LOCATIONS *
EVERGREEN RADIA LLC 	 Evergreen Radia Imaging Center
Gage Inpatient Physicians 	 TriState Memorial Hospital
Gage Inpatient Physicians 	 TriState Memorial Hospital
Galen Inpatient Services 	 Capital Medical Center
Galen Inpatient Services 	 Capital Medical Center
GEPS PHYSICIAN GROUP OF PENNSYLVANIA PC 	 * USE FOR UNKNOWN, UNLISTED OR MULTIPLE LOCATIONS *
GEPS PHYSICIAN GROUP OF PENNSYLVANIA PC 	 Columbia Crest Center
GEPS PHYSICIAN GROUP OF PENNSYLVANIA PC 	 Everett Center
Highline Emergency Physicians 	 Highline Medical Center
HMC, DBA HIGHLINE IMAGING 	 HMC, DBA HIGHLINE IMAGING
INTEGRA IMAGING BUSINESS ASSOCIATES 	 * USE FOR UNKNOWN, UNLISTED OR MULTIPLE LOCATIONS *
INTEGRA IMAGING BUSINESS ASSOCIATES 	 Adventist Health Medical Group
INTEGRA IMAGING BUSINESS ASSOCIATES 	 Arthritis NW Rheumatology PLLC
INTEGRA IMAGING BUSINESS ASSOCIATES 	 Cancer Care Northwest
INTEGRA IMAGING BUSINESS ASSOCIATES 	 CHAS
INTEGRA IMAGING BUSINESS ASSOCIATES 	 Columbia Medical Associates North
INTEGRA IMAGING BUSINESS ASSOCIATES 	 Columbia Medical Associates South
INTEGRA IMAGING BUSINESS ASSOCIATES 	 Deaconess Medical Center
INTEGRA IMAGING BUSINESS ASSOCIATES 	 Deer Park Mobile MRI
INTEGRA IMAGING BUSINESS ASSOCIATES 	 East Adams Rural Hospital
INTEGRA IMAGING BUSINESS ASSOCIATES 	 Everett Clinic Gunderson Building
INTEGRA IMAGING BUSINESS ASSOCIATES 	 Everett Clinic Harbour Pointe
INTEGRA IMAGING BUSINESS ASSOCIATES 	 Everett Clinic Lake Stevens
INTEGRA IMAGING BUSINESS ASSOCIATES 	 Everett Clinic Main Clinic
INTEGRA IMAGING BUSINESS ASSOCIATES 	 Everett Clinic Marysville
INTEGRA IMAGING BUSINESS ASSOCIATES 	 Everett Clinic Mill Creek
INTEGRA IMAGING BUSINESS ASSOCIATES 	 Everett Clinic Silver Lake
INTEGRA IMAGING BUSINESS ASSOCIATES 	 Everett Clinic Smokey Point
INTEGRA IMAGING BUSINESS ASSOCIATES 	 Everett Clinic Snohomish
INTEGRA IMAGING BUSINESS ASSOCIATES 	 Everett Clinic Stanwood
INTEGRA IMAGING BUSINESS ASSOCIATES 	 Evergreen Hematology Oncology
INTEGRA IMAGING BUSINESS ASSOCIATES 	 Ferry County Hospital
INTEGRA IMAGING BUSINESS ASSOCIATES 	 First Hill Diagnostic Imaging
INTEGRA IMAGING BUSINESS ASSOCIATES 	 Holy Family Hospital
INTEGRA IMAGING BUSINESS ASSOCIATES 	 Inland at Deer Park
INTEGRA IMAGING BUSINESS ASSOCIATES 	 Inland at Holy Family
INTEGRA IMAGING BUSINESS ASSOCIATES 	 Inland At Holy Family
INTEGRA IMAGING BUSINESS ASSOCIATES 	 Inland at Liberty Lake
INTEGRA IMAGING BUSINESS ASSOCIATES 	 Inland at Northpoint
INTEGRA IMAGING BUSINESS ASSOCIATES 	 Inland at Providence Medical Park
INTEGRA IMAGING BUSINESS ASSOCIATES 	 Inland at Sacred Heart
INTEGRA IMAGING BUSINESS ASSOCIATES 	 Inland At Sacred Heart
INTEGRA IMAGING BUSINESS ASSOCIATES 	 Inland Imaging Manito Mammography
INTEGRA IMAGING BUSINESS ASSOCIATES 	 Lincoln County Hospital
INTEGRA IMAGING BUSINESS ASSOCIATES 	 Medical Oncology Associates
INTEGRA IMAGING BUSINESS ASSOCIATES 	 Minor And James
INTEGRA IMAGING BUSINESS ASSOCIATES 	 Minor and James Bellevue Commons
INTEGRA IMAGING BUSINESS ASSOCIATES 	 MT Carmel Hospital
INTEGRA IMAGING BUSINESS ASSOCIATES 	 NE Washington Medical Group
INTEGRA IMAGING BUSINESS ASSOCIATES 	 Newport Community Hospital
INTEGRA IMAGING BUSINESS ASSOCIATES 	 Northwest Orthopaedic Specialists
INTEGRA IMAGING BUSINESS ASSOCIATES 	 Odessa Memorial Hospital
INTEGRA IMAGING BUSINESS ASSOCIATES 	 Othello Community Hospital
INTEGRA IMAGING BUSINESS ASSOCIATES 	 Physicians Clinic Of Spokane
INTEGRA IMAGING BUSINESS ASSOCIATES 	 Pioneer Medical Building
INTEGRA IMAGING BUSINESS ASSOCIATES 	 Providence Family Medicine Hawthorn
INTEGRA IMAGING BUSINESS ASSOCIATES 	 Providence Health & Serv UrgentCare
INTEGRA IMAGING BUSINESS ASSOCIATES 	 Pullman Family Medicine
INTEGRA IMAGING BUSINESS ASSOCIATES 	 Pullman Regional Hospital
INTEGRA IMAGING BUSINESS ASSOCIATES 	 Sacred Heart Medical Center
INTEGRA IMAGING BUSINESS ASSOCIATES 	 Samaritan Hospital
INTEGRA IMAGING BUSINESS ASSOCIATES 	 South Center
INTEGRA IMAGING BUSINESS ASSOCIATES 	 Spokane Ear Nose Throat Clinic
INTEGRA IMAGING BUSINESS ASSOCIATES 	 St Josephs Hospital
INTEGRA IMAGING BUSINESS ASSOCIATES 	 Steck Medical Group
INTEGRA IMAGING BUSINESS ASSOCIATES 	 Swedish Medical Center Everett
INTEGRA IMAGING BUSINESS ASSOCIATES 	 Swedish Medical Center Redmond
INTEGRA IMAGING BUSINESS ASSOCIATES 	 Swedish Medical Center Seattle
INTEGRA IMAGING BUSINESS ASSOCIATES 	 Valley Center
INTEGRA IMAGING BUSINESS ASSOCIATES 	 Walla Walla General Hosptial
INTEGRA IMAGING BUSINESS ASSOCIATES 	 Walla Walla Medical Pavilion
KADLEC MEDICAL ASSOCIATES 	 KADLEC REGIONAL MEDICAL CENTER 
KENNEWICK RADIOLOGY GROUP PC 	 TRIOS SOUTHRIDGE HOSPITAL
Lake Tye Emergency Physicians 	 Valley General Hospital
Lake Tye Emergency Physicians 	 Valley General Hospital
Lewis County Emergency Physicians 	 Providence Hospital/Centralia
MEDICAL INSIGHTS DIAGNOSTIC CENTERS 	 KINDRED HOSPITAL
Monroe Inpatient Services , PLLC 	 Valley General Hospital
Monroe Inpatient Services , PLLC 	 Valley General Hospital
Mount Baker Imaging (MBI) 	 Washington Locations
Mt. Rainier Emergency Physicians, PLLC 	 Good Samaritan Hospital
North Sound Emergency Medicine 	 Providence Regional Medical Center
North Sound Emergency Medicine 	 Valley General Hospital
NORTHWEST EMERG PHYS 	 PROVIDENCE CENTRALIA HOSPITAL 
NORTHWEST EMERG PHYS 	 ST ANTHONY HOSPITAL 
NORTHWEST EMERG PHYS INC 	 CASCADE VALLEY HOSPITAL 
NORTHWEST EMERG PHYS INC 	 ISLAND HOSPITAL 
NORTHWEST EMERG PHYS INC 	 KADLEC EMERGENCY AT KENNEWICK 
NORTHWEST EMERG PHYS INC 	 KADLEC MEDICAL CENTER 
NORTHWEST EMERG PHYS INC 	 SAMARITAN HEALTHCARE 
NORTHWEST EMERG PHYS INC 	 ST ELIZABETH WA HOSPITAL 
NORTHWEST EMERGENCY PHYS 	 STEVENS HOSPITAL 
NORTHWEST EMERGENCY PHYSICIANS 	 ST CLARE HOSPITAL 
NORTHWEST EMERGENCY PHYSICIANS 	 ST FRANCIS WA COMMUNITY HOSPITAL 
NORTHWEST EMERGENCY PHYSICIANS 	 ST JOSEPH WA HOSPITAL 
NORTHWEST EMERGENCY PHYSICIANS 	 ST JOSEPH WA HOSPITAL - BELLINGHAM ED 
Northwest Pacific Emergency Physicians, LLP 	 Deaconess Medical Center
Northwest Radiologists (NWR) 	 BELLINGHAM AMBULATORY SURG CENTER
Northwest Radiologists (NWR) 	 CARE MEDICAL GROUP EXPRESS CARE
Northwest Radiologists (NWR) 	 LUMMI TRIBAL HEALTH CENTER
Northwest Radiologists (NWR) 	 NORTHWEST RADIOLOGISTS OVERREADS
Northwest Radiologists (NWR) 	 NORTHWEST RADIOLOGISTS PET/CT
Northwest Radiologists (NWR) 	 NORTHWEST RADIOLOGISTS VASCULAR
Northwest Radiologists (NWR) 	 ORCAS FAMILY HEALTH CENTER
Northwest Radiologists (NWR) 	 PH PEACE ISLAND MEDICAL CENTER
Northwest Radiologists (NWR) 	 PH ST JOSEPH MEDICAL CENTER
Northwest Radiologists (NWR) 	 RIVERSIDE PORTABLE X-RAY
Okanogan Emergency Physicians 	 Mid-Valley Hospital
Okanogan Emergency Physicians 	 Mid-Valley Hospital
OLYMPIC MEDICAL IMAGING CONSULTANTS 	 Bremerton Advanced Medical Imaging
OLYMPIC MEDICAL IMAGING CONSULTANTS 	 Harrison Medical Center Belfair Urgent Care
OLYMPIC MEDICAL IMAGING CONSULTANTS 	 Harrison Medical Center S Kitsap Urgent Care
OLYMPIC MEDICAL IMAGING CONSULTANTS 	 Poulsbo Advanced Medical Imaging
OLYMPIC MEDICAL IMAGING CONSULTANTS 	 Silverdale Advanced Medical Imaging
OLYMPIC MEDICAL IMAGING CONSULTANTS 	 South Kitsap Advanced Medical Imaging
Olympic Medical Imaging Consultants, PLLC 	 HARRISON MEDICAL CENTER - BREMERTON CAMPUS
Olympic Medical Imaging Consultants, PLLC 	 HARRISON MEDICAL CENTER - SILVERDALE CAMPUS
Olympic Medical Imaging Consultants, PLLC 	 HMC BAINBRIDGE ISLAND URGENT CARE
Olympic Medical Imaging Consultants, PLLC 	 HMC BELFAIR URGENT CARE
Olympic Medical Imaging Consultants, PLLC 	 HMC BREMERTON AMI
Olympic Medical Imaging Consultants, PLLC 	 HMC BREMERTON OR
Olympic Medical Imaging Consultants, PLLC 	 HMC POULSBO AMI
Olympic Medical Imaging Consultants, PLLC 	 HMC POULSBO OR
Olympic Medical Imaging Consultants, PLLC 	 HMC SILVERDALE AMI
Olympic Medical Imaging Consultants, PLLC 	 HMC SOUTH KITSAP AMI
Olympic Medical Imaging Consultants, PLLC 	 HMC SOUTH KITSAP URGENT CARE
Olympic Medical Imaging Consultants, PLLC 	 TDC URGENT CARE
Olympic Medical Imaging Consultants, PLLC 	 WSO POULSBO
OVERLAKE IMAGING ASSOCIATES 	 * USE FOR UNKNOWN, UNLISTED OR MULTIPLE LOCATIONS *
OVERLAKE IMAGING ASSOCIATES 	 ISSAQUAH URGENT CARE
OVERLAKE IMAGING ASSOCIATES 	 NEUROLOGICAL ASSOCIATES
OVERLAKE IMAGING ASSOCIATES 	 Overlake Hospital Imaging - Issaquah
OVERLAKE IMAGING ASSOCIATES 	 Overlake Hospital Imaging - NAW
OVERLAKE IMAGING ASSOCIATES 	 Overlake Hospital Imaging - Redmond
OVERLAKE IMAGING ASSOCIATES 	 Overlake Hospital Imaging - Tower
OVERLAKE IMAGING ASSOCIATES 	 Overlake Hospital Medical Center
OVERLAKE IMAGING ASSOCIATES 	 Overlake Imaging Issaquah
PATHOLOGIST REGIONAL LABORATORY 	 PATH REGIONAL LAB
Pend Oreille River Emergency Physicians, PLLC 	 Newport Hospital & Health Services
Pend Oreille River Emergency Physicians, PLLC 	 Newport Hospital & Health Services
Physiotherapy Associates 	 All Washington Locations
Plateau Emergency Physicians 	 Enumclaw Community Hospital
Plateau Emergency Physicians 	 Enumclaw Community Hospital
RADIA INC PS 	 * USE FOR UNKNOWN, UNLISTED OR MULTIPLE LOCATIONS *
RADIA INC PS 	 Alaska Neurology Center
RADIA INC PS 	 ANOVA WORKS
RADIA INC PS 	 Ben Harmon MD RADA
RADIA INC PS 	 BOEING
RADIA INC PS 	 Capital Medical Center
RADIA INC PS 	 Central WA Hospital
RADIA INC PS 	 Columbia Valley Community Hlth
RADIA INC PS 	 Coulee Community Hospital
RADIA INC PS 	 CWH Simplant
RADIA INC PS 	 Dawn Hastreiter MD RADA
RADIA INC PS 	 Deaconess Medical Center
RADIA INC PS 	 EDMONDS FAMILY MEDICINE
RADIA INC PS 	 EMG Duvall
RADIA INC PS 	 EMG Sammamish
RADIA INC PS 	 EMG Woodinville Family Practice
RADIA INC PS 	 Everett Bone & Joint
RADIA INC PS 	 Everett Bone & Joint Center
RADIA INC PS 	 Evergreen - Canyon Park
RADIA INC PS 	 Evergreen Hospital Medical Center
RADIA INC PS 	 Evergreen Professional Center
RADIA INC PS 	 Evergreen Radia Imaging Center-Redmond
RADIA INC PS 	 Inglewood Family Health
RADIA INC PS 	 Jefferson General Hospital
RADIA INC PS 	 Kadlec Medical Center
RADIA INC PS 	 Mid Valley Hospital
RADIA INC PS 	 Mid Valley Medical Group
RADIA INC PS 	 Mill Creek Family Practice
RADIA INC PS 	 North Idaho Acute Care Hospital
RADIA INC PS 	 North Valley Hospital CWH
RADIA INC PS 	 Obstetrix Seattle Ultrasound
RADIA INC PS 	 Olympic Downtown Ambulatory Clinic
RADIA INC PS 	 Olympic Medical Cancer Center
RADIA INC PS 	 Olympic Medical Imaging Center
RADIA INC PS 	 Olympic Medical Jamestown
RADIA INC PS 	 Olympic Medical Phys Primary Care
RADIA INC PS 	 Olympic Memorial Hospital
RADIA INC PS 	 Providence - Mill Creek
RADIA INC PS 	 Providence Harbor Pointe
RADIA INC PS 	 Providence Medical Bldg Monroe
RADIA INC PS 	 Providence Medical Group - Lynwood
RADIA INC PS 	 Providence Medical Group - Snohomish
RADIA INC PS 	 Providence Monroe
RADIA INC PS 	 Providence Physicians Group Interventional
RADIA INC PS 	 Providence Regional Medical Center Everett - Colby
RADIA INC PS 	 Providence Regional Medical Center Everett - Pacific
RADIA INC PS 	 ProvPG Marysville
RADIA INC PS 	 ProvPG Snohomish
RADIA INC PS 	 Radia Inc Teleradia Corp Office
RADIA INC PS 	 Radia Vascular & Interventional Phy
RADIA INC PS 	 Rockwood Airway Heights
RADIA INC PS 	 Rockwood Argonne Urgent Care
RADIA INC PS 	 Rockwood Breast Health Center
RADIA INC PS 	 Rockwood Cancer Treatment Center
RADIA INC PS 	 Rockwood Cheney Clinic
RADIA INC PS 	 Rockwood Clinic
RADIA INC PS 	 Rockwood Clinic
RADIA INC PS 	 Rockwood Deer Park
RADIA INC PS 	 Rockwood Liberty Lake Clinic
RADIA INC PS 	 Rockwood Liberty Lake Urgent Care
RADIA INC PS 	 Rockwood Main Clinic
RADIA INC PS 	 Rockwood Medical Lake Clinic
RADIA INC PS 	 Rockwood North
RADIA INC PS 	 Rockwood Northpointe Specialty Center
RADIA INC PS 	 Rockwood OB GYN Center
RADIA INC PS 	 Rockwood Orthopedics & Sports Med
RADIA INC PS 	 Rockwood Quail Run Clinic
RADIA INC PS 	 Rockwood South Hill Urgent Care
RADIA INC PS 	 Rockwood South Valley Clinic
RADIA INC PS 	 Rockwood Valley Clinic
RADIA INC PS 	 Rockwood Valley Specialty
RADIA INC PS 	 Seattle Nuclear Medicine
RADIA INC PS 	 Sequim Medical Services Building
RADIA INC PS 	 Snoqualmie Valley Hospital
RADIA INC PS 	 SPD Childrens Clinic
RADIA INC PS 	 SPD CLE ELUM
RADIA INC PS 	 SPD Downtown
RADIA INC PS 	 SPD Factoria
RADIA INC PS 	 SPD Greenlake
RADIA INC PS 	 SPD Magnolia
RADIA INC PS 	 SPD Pine Lake
RADIA INC PS 	 SPD Queen Anne
RADIA INC PS 	 SPD West Seattle
RADIA INC PS 	 Sunrise Clinic
RADIA INC PS 	 Swedish First Hill Campus
RADIA INC PS 	 Swedish Issaquah
RADIA INC PS 	 Swedish Medical Center - Ballard
RADIA INC PS 	 Swedish Medical Center - Cherry Hill
RADIA INC PS 	 Swedish Medical Center - Issaquah
RADIA INC PS 	 Swedish Mobile Mammography
RADIA INC PS 	 Swedish Mobile Mammography BCHP
RADIA INC PS 	 Swedish Seattle-RVIP
RADIA INC PS 	 Swedish/Edmonds Hospital
RADIA INC PS 	 Swedish/Edmonds Pavilion Imaging
RADIA INC PS 	 Swedish/Edmonds Pavilion Mill Creek
RADIA INC PS 	 TULALIP INDIAN TRIBE
RADIA INC PS 	 Valley General Hospital - Monroe
RADIA INC PS 	 Valley Hospital & Medical Center
RADIA INC PS 	 Wenatchee Valley Medical Center
RADIA INC PS 	 Western WA Medical Group
RADIA INC PS 	 WHIDBEY COMMUNITY PHYSICIANS
RADIA INC PS 	 Whidbey General - Oak Harbor
RADIA INC PS 	 Whidbey General - South Island
RADIA INC PS 	 Whidbey General Hospital
Rural/Metro of Greater Seattle, Inc. 	 nan
Scheuber Road Emergency Physicians 	 Providence Centralia Hospital
Scheuber Road Emergency Physicians 	 Providence Centralia Hospital
Seahawk Emergency Physicians 	 Toppenish Community Hospital
Seahawk Emergency Physicians 	 Toppenish Community Hospital
Seattle Emergency Physicians 	 Swedish Medical Center/Cherry Hill
Seattle Emergency Physicians 	 Swedish Medical Center/First Hill
Seattle Nuclear Medicine (SNM) 	 SEATTLE NUCLEAR MEDICINE
Seattle Nuclear Medicine (SNM) 	 SWEDISH MEDICAL CENTER-FIRST HILL
Seattle Nuclear Medicine (SNM) 	 nan
Sedro-Woolley Emergency Physicians 	 United General Hospital
Sedro-Woolley Emergency Physicians 	 United General Hospital
SOUTH SOUND RADIOLOGY 	  CHIROPRACTIC
SOUTH SOUND RADIOLOGY 	 * USE FOR UNKNOWN, UNLISTED OR MULTIPLE LOCATIONS *
SOUTH SOUND RADIOLOGY 	 CAPITAL IMAGING CENTER
SOUTH SOUND RADIOLOGY 	 CHEHALIS TRIBAL WELLNESS CENTER
SOUTH SOUND RADIOLOGY 	 GRAYS HARBOR CARDIOVASC IMAG
SOUTH SOUND RADIOLOGY 	 GRAYS HARBOR COMMUNITY HOSPITAL
SOUTH SOUND RADIOLOGY 	 GRAYS HARBOR IMAGING
SOUTH SOUND RADIOLOGY 	 MASON GENERAL HOSPITAL
SOUTH SOUND RADIOLOGY 	 MORTON GENERAL HOSPITAL
SOUTH SOUND RADIOLOGY 	 OLYMPIA MULTI SPECIALTY CLINIC
SOUTH SOUND RADIOLOGY 	 OLYMPIA OB AND GYN
SOUTH SOUND RADIOLOGY 	 OLYMPIA ORTHOPEDICS
SOUTH SOUND RADIOLOGY 	 PROVIDENCE CENTRALIA HOSPITAL
SOUTH SOUND RADIOLOGY 	 PROVIDENCE DIAG IMAGING CENTER
SOUTH SOUND RADIOLOGY 	 PROVIDENCE HAWKS PRAIRIE CENTER
SOUTH SOUND RADIOLOGY 	 PROVIDENCE REG CANCER CENTER
SOUTH SOUND RADIOLOGY 	 PROVIDENCE ST PETER HOSPITAL
SOUTH SOUND RADIOLOGY 	 PROVIDENCE WEST OLYMPIA CLINIC
SOUTH SOUND RADIOLOGY 	 RIFFE MEDICAL CENTER
SOUTH SOUND RADIOLOGY 	 SOUTH SOUND RADIOLOGISTS INC PS
SOUTH SOUND RADIOLOGY 	 SOUTH SOUND SURGERY CENTER
SOUTH SOUND RADIOLOGY 	 SUMMIT PACIFIC MEDICAL CENTER
SOUTH SOUND RADIOLOGY 	 TUMWATER FAMILY PRACTICE
SOUTH SOUND RADIOLOGY 	 WASHINGTON PARK MEDICAL CENTER
SOUTH SOUND RADIOLOGY 	 WESTCARE CLINIC
SOUTH SOUND RADIOLOGY 	 YELM FAMILY MEDICINE
Southland Hospitalist 	 St Joseph Hospital WA
Spokane Emergency Physicians 	 Sacred Heart Medical Center
Spokane Tribal Emergency Response 	 nan
Stewards Inpatient Services 	 Auburn Regional Medical Center
Stewards Inpatient Services 	 Auburn Regional Medical Center
SWEDISH RADIA EDMONDS 	 * USE FOR UNKNOWN, UNLISTED OR MULTIPLE LOCATIONS *
SWEDISH RADIA EDMONDS 	 Mill Creek Family Practice
SWEDISH RADIA EDMONDS 	 Swedish Edmonds Imaging Center
SWEDISH RADIA EDMONDS 	 Swedish Medical Center Edmonds
Tacoma Emergency Care Physicians, Inc., P.S. 	 Allenmore Hospital and Medical Center
Tacoma Emergency Care Physicians, Inc., P.S. 	 Multicare Covington Medical Center
Tacoma Emergency Care Physicians, Inc., P.S. 	 Tacoma General Hospital
Thurston ER Group 	 Capital Medical Center
TRI-CITY RADIOLOGY, INC 	 TRI-CITY RADIOLOGY, INC
Tri-State Hospitalist Group 	 Tri-State Memorial Hospital
Tri-State Hospitalist Group 	 Tri-State Memorial Hospital
West Sound Emergency Physicians 	 Harrison Medical Center Bremerton
West Sound Emergency Physicians 	 Harrison Medical Center Silverdale
Yakima Emergency Group 	 Yakima Regional Med & Cardiac Center
>>> 
KeyboardInterrupt
>>> import namedtuple
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    import namedtuple
ImportError: No module named 'namedtuple'
>>> from collections import namedtuple
>>> A = namedtuple('A', 'Phys Facility')
>>> for i in df.index:
	if df['Account Site'][i] == 'Washington':
		return A(f['Account Name'][i],  df['Attention'][i])
		#print(df['Account Name'][i], '\t',  df['Attention'][i])
	
SyntaxError: 'return' outside function
>>> def t():
	for i in df.index:
		f df['Account Site'][i] == 'Washington':
			
SyntaxError: invalid syntax
>>> def t():
	for i in df.index:
		fd['Account Site'][i] == 'Washington':
			
SyntaxError: invalid syntax
>>> def t():
	for i in df.index:
		if fd['Account Site'][i] == 'Washington':
			return A(f['Account Name'][i],  df['Attention'][i])

		
>>> tup = t()
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    tup = t()
  File "<pyshell#74>", line 3, in t
    if fd['Account Site'][i] == 'Washington':
NameError: name 'fd' is not defined
>>> def t():
	for i in df.index:
		if df['Account Site'][i] == 'Washington':
			return A(f['Account Name'][i],  df['Attention'][i])

		
>>> tup = t()
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    tup = t()
  File "<pyshell#77>", line 4, in t
    return A(f['Account Name'][i],  df['Attention'][i])
NameError: name 'f' is not defined
>>> def t():
	for i in df.index:
		if df['Account Site'][i] == 'Washington':
			return A(df['Account Name'][i],  df['Attention'][i])

		
>>> tup = t()
>>> tup[0]
'ADVANCED OPEN IMAGING'
>>> tup[1]
'* USE FOR UNKNOWN, UNLISTED OR MULTIPLE LOCATIONS *'
>>> tup
A(Phys='ADVANCED OPEN IMAGING', Facility='* USE FOR UNKNOWN, UNLISTED OR MULTIPLE LOCATIONS *')
>>> def t():
	t = set()
	for i in df.index:
		if df['Account Site'][i] == 'Washington':
			t.add(A(df['Account Name'][i],  df['Attention'][i]))

			
>>> def t():
	t = set()
	for i in df.index:
		if df['Account Site'][i] == 'Washington':
			t.add(A(df['Account Name'][i],  df['Attention'][i]))
	return t

>>> tup = t()
>>> tup
{A(Phys='RADIA INC PS', Facility='EMG Duvall'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='Everett Clinic Stanwood'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='Inland at Liberty Lake'), A(Phys='HMC, DBA HIGHLINE IMAGING', Facility='HMC, DBA HIGHLINE IMAGING'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='* USE FOR UNKNOWN, UNLISTED OR MULTIPLE LOCATIONS *'), A(Phys='SOUTH SOUND RADIOLOGY', Facility='YELM FAMILY MEDICINE'), A(Phys='Physiotherapy Associates', Facility='All Washington Locations'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='Everett Clinic Gunderson Building'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='East Adams Rural Hospital'), A(Phys='RADIA INC PS', Facility='Jefferson General Hospital'), A(Phys='RADIA INC PS', Facility='Evergreen Professional Center'), A(Phys='RADIA INC PS', Facility='Sunrise Clinic'), A(Phys='OLYMPIC MEDICAL IMAGING CONSULTANTS', Facility='Harrison Medical Center S Kitsap Urgent Care'), A(Phys='Olympic Medical Imaging Consultants, PLLC', Facility='HMC BREMERTON AMI'), A(Phys='NORTHWEST EMERGENCY PHYS', Facility='STEVENS HOSPITAL '), A(Phys='RADIA INC PS', Facility='Olympic Medical Jamestown'), A(Phys='SWEDISH RADIA EDMONDS', Facility='* USE FOR UNKNOWN, UNLISTED OR MULTIPLE LOCATIONS *'), A(Phys='RADIA INC PS', Facility='EMG Woodinville Family Practice'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='Pullman Family Medicine'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='Pioneer Medical Building'), A(Phys='RADIA INC PS', Facility='North Valley Hospital CWH'), A(Phys='RADIA INC PS', Facility='ProvPG Marysville'), A(Phys='RADIA INC PS', Facility='Everett Bone & Joint Center'), A(Phys='Northwest Radiologists (NWR)', Facility='NORTHWEST RADIOLOGISTS OVERREADS'), A(Phys='Stewards Inpatient Services', Facility='Auburn Regional Medical Center'), A(Phys='North Sound Emergency Medicine', Facility='Valley General Hospital'), A(Phys='NORTHWEST EMERG PHYS INC', Facility='CASCADE VALLEY HOSPITAL '), A(Phys='RADIA INC PS', Facility='Deaconess Medical Center'), A(Phys='SOUTH SOUND RADIOLOGY', Facility='OLYMPIA OB AND GYN'), A(Phys='Lewis County Emergency Physicians', Facility='Providence Hospital/Centralia'), A(Phys='RADIA INC PS', Facility='Ben Harmon MD RADA'), A(Phys='SOUTH SOUND RADIOLOGY', Facility='* USE FOR UNKNOWN, UNLISTED OR MULTIPLE LOCATIONS *'), A(Phys='Plateau Emergency Physicians', Facility='Enumclaw Community Hospital'), A(Phys='OVERLAKE IMAGING ASSOCIATES', Facility='Overlake Hospital Imaging - NAW'), A(Phys='SOUTH SOUND RADIOLOGY', Facility='CAPITAL IMAGING CENTER'), A(Phys='RADIA INC PS', Facility='SPD Magnolia'), A(Phys='RADIA INC PS', Facility='Everett Bone & Joint'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='Everett Clinic Main Clinic'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='Holy Family Hospital'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='Valley Center'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='Everett Clinic Harbour Pointe'), A(Phys='GEPS PHYSICIAN GROUP OF PENNSYLVANIA PC', Facility='Columbia Crest Center'), A(Phys='Monroe Inpatient Services , PLLC', Facility='Valley General Hospital'), A(Phys='SOUTH SOUND RADIOLOGY', Facility='TUMWATER FAMILY PRACTICE'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='Adventist Health Medical Group'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='Ferry County Hospital'), A(Phys='Olympic Medical Imaging Consultants, PLLC', Facility='WSO POULSBO'), A(Phys='OVERLAKE IMAGING ASSOCIATES', Facility='Overlake Hospital Imaging - Issaquah'), A(Phys='Northwest Radiologists (NWR)', Facility='NORTHWEST RADIOLOGISTS VASCULAR'), A(Phys='SOUTH SOUND RADIOLOGY', Facility='PROVIDENCE HAWKS PRAIRIE CENTER'), A(Phys='RADIA INC PS', Facility='Providence Regional Medical Center Everett - Colby'), A(Phys='Highline Emergency Physicians', Facility='Highline Medical Center'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='Inland at Northpoint'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='Newport Community Hospital'), A(Phys='RADIA INC PS', Facility='Inglewood Family Health'), A(Phys='RADIA INC PS', Facility='Radia Vascular & Interventional Phy'), A(Phys='North Sound Emergency Medicine', Facility='Providence Regional Medical Center'), A(Phys='GEPS PHYSICIAN GROUP OF PENNSYLVANIA PC', Facility='Everett Center'), A(Phys='RADIA INC PS', Facility='Swedish Medical Center - Ballard'), A(Phys='RADIA INC PS', Facility='Rockwood Airway Heights'), A(Phys='Olympic Medical Imaging Consultants, PLLC', Facility='HMC POULSBO OR'), A(Phys='RADIA INC PS', Facility='ANOVA WORKS'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='Everett Clinic Mill Creek'), A(Phys='RADIA INC PS', Facility='Rockwood Cancer Treatment Center'), A(Phys='RADIA INC PS', Facility='Valley General Hospital - Monroe'), A(Phys='SOUTH SOUND RADIOLOGY', Facility='PROVIDENCE REG CANCER CENTER'), A(Phys='EVERGREEN RADIA LLC', Facility='Evergreen Radia Imaging Center'), A(Phys='SOUTH SOUND RADIOLOGY', Facility='SOUTH SOUND RADIOLOGISTS INC PS'), A(Phys='RADIA INC PS', Facility='Rockwood Liberty Lake Urgent Care'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='South Center'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='Walla Walla General Hosptial'), A(Phys='Olympic Medical Imaging Consultants, PLLC', Facility='HMC BELFAIR URGENT CARE'), A(Phys='Ballard Emergency Physicians PS', Facility='Swedish Medical Center'), A(Phys='Olympic Medical Imaging Consultants, PLLC', Facility='HMC SOUTH KITSAP URGENT CARE'), A(Phys='ADVANCED OPEN IMAGING', Facility='ADVANCED IMAGING SVC'), A(Phys='MEDICAL INSIGHTS DIAGNOSTIC CENTERS', Facility='KINDRED HOSPITAL'), A(Phys='RADIA INC PS', Facility='Seattle Nuclear Medicine'), A(Phys='Seattle Nuclear Medicine (SNM)', Facility='SWEDISH MEDICAL CENTER-FIRST HILL'), A(Phys='RADIA INC PS', Facility='Rockwood Deer Park'), A(Phys='RADIA INC PS', Facility='Rockwood OB GYN Center'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='Everett Clinic Silver Lake'), A(Phys='Spokane Emergency Physicians', Facility='Sacred Heart Medical Center'), A(Phys='RADIA INC PS', Facility='Providence - Mill Creek'), A(Phys='EVERGREEN RADIA LLC', Facility='* USE FOR UNKNOWN, UNLISTED OR MULTIPLE LOCATIONS *'), A(Phys='SOUTH SOUND RADIOLOGY', Facility='GRAYS HARBOR COMMUNITY HOSPITAL'), A(Phys='Direct Radiology', Facility='OCEAN BEACH HOSP'), A(Phys='Eastside Emergency Physicians, PLLC', Facility='Swedish Medical Center Mill Creek'), A(Phys='Seattle Nuclear Medicine (SNM)', Facility=nan), A(Phys='RADIA INC PS', Facility='CWH Simplant'), A(Phys='Olympic Medical Imaging Consultants, PLLC', Facility='HMC BREMERTON OR'), A(Phys='RADIA INC PS', Facility='Providence Medical Group - Lynwood'), A(Phys='CEP AMERICA LLC', Facility='Swedish Edmonds'), A(Phys='EVERETT RADIA LLC', Facility='Ben Harmon MD'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='Swedish Medical Center Everett'), A(Phys='Black Hill Emergency Physiicans', Facility='Capital Medical Center'), A(Phys='RADIA INC PS', Facility='SPD Downtown'), A(Phys='NORTHWEST EMERGENCY PHYSICIANS', Facility='ST FRANCIS WA COMMUNITY HOSPITAL '), A(Phys='NORTHWEST EMERGENCY PHYSICIANS', Facility='ST JOSEPH WA HOSPITAL - BELLINGHAM ED '), A(Phys='Northwest Radiologists (NWR)', Facility='PH ST JOSEPH MEDICAL CENTER'), A(Phys='Okanogan Emergency Physicians', Facility='Mid-Valley Hospital'), A(Phys='RADIA INC PS', Facility='Radia Inc Teleradia Corp Office'), A(Phys='RADIA INC PS', Facility='Rockwood Northpointe Specialty Center'), A(Phys='RADIA INC PS', Facility='TULALIP INDIAN TRIBE'), A(Phys='RADIA INC PS', Facility='Providence Regional Medical Center Everett - Pacific'), A(Phys='RADIA INC PS', Facility='* USE FOR UNKNOWN, UNLISTED OR MULTIPLE LOCATIONS *'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='Inland At Holy Family'), A(Phys='RADIA INC PS', Facility='Rockwood Breast Health Center'), A(Phys='Cascade Emergency Physicians', Facility='Auburn Regional Medical Center'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='Columbia Medical Associates South'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='MT Carmel Hospital'), A(Phys='SOUTH SOUND RADIOLOGY', Facility=' CHIROPRACTIC'), A(Phys='ADVANCED OPEN IMAGING', Facility='AOI GRP HEALTH'), A(Phys='RADIA INC PS', Facility='ProvPG Snohomish'), A(Phys='OLYMPIC MEDICAL IMAGING CONSULTANTS', Facility='Harrison Medical Center Belfair Urgent Care'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='Everett Clinic Snohomish'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='Minor and James Bellevue Commons'), A(Phys='NORTHWEST EMERGENCY PHYSICIANS', Facility='ST CLARE HOSPITAL '), A(Phys='Olympic Medical Imaging Consultants, PLLC', Facility='HMC POULSBO AMI'), A(Phys='RADIA INC PS', Facility='Coulee Community Hospital'), A(Phys='Cascade Radiology Consultants', Facility='Granite Falls Clinic'), A(Phys='Northwest Radiologists (NWR)', Facility='NORTHWEST RADIOLOGISTS PET/CT'), A(Phys='Cowiche Creek Emergency Physicians', Facility='Yakima Regional Medical & Heart Center'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='Columbia Medical Associates North'), A(Phys='RADIA INC PS', Facility='Valley Hospital & Medical Center'), A(Phys='SOUTH SOUND RADIOLOGY', Facility='CHEHALIS TRIBAL WELLNESS CENTER'), A(Phys='KENNEWICK RADIOLOGY GROUP PC', Facility='TRIOS SOUTHRIDGE HOSPITAL'), A(Phys='RADIA INC PS', Facility='SPD Childrens Clinic'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='Inland at Providence Medical Park'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='Samaritan Hospital'), A(Phys='KADLEC MEDICAL ASSOCIATES', Facility='KADLEC REGIONAL MEDICAL CENTER '), A(Phys='Northwest Radiologists (NWR)', Facility='RIVERSIDE PORTABLE X-RAY'), A(Phys='RADIA INC PS', Facility='Capital Medical Center'), A(Phys='Northwest Pacific Emergency Physicians, LLP', Facility='Deaconess Medical Center'), A(Phys='SOUTH SOUND RADIOLOGY', Facility='OLYMPIA ORTHOPEDICS'), A(Phys='RADIA INC PS', Facility='Central WA Hospital'), A(Phys='Seattle Emergency Physicians', Facility='Swedish Medical Center/Cherry Hill'), A(Phys='City of Mukilteo Fire Department', Facility=nan), A(Phys='Northwest Radiologists (NWR)', Facility='LUMMI TRIBAL HEALTH CENTER'), A(Phys='RADIA INC PS', Facility='Rockwood Main Clinic'), A(Phys='Cedra Emergency Physicians', Facility='United General Hospital'), A(Phys='RADIA INC PS', Facility='Olympic Medical Cancer Center'), A(Phys='SOUTH SOUND RADIOLOGY', Facility='PROVIDENCE CENTRALIA HOSPITAL'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='First Hill Diagnostic Imaging'), A(Phys='RADIA INC PS', Facility='SPD Pine Lake'), A(Phys='SWEDISH RADIA EDMONDS', Facility='Swedish Edmonds Imaging Center'), A(Phys='Bridgeport Ambulance', Facility=nan), A(Phys='NORTHWEST EMERG PHYS', Facility='PROVIDENCE CENTRALIA HOSPITAL '), A(Phys='RADIA INC PS', Facility='Olympic Downtown Ambulatory Clinic'), A(Phys='Gage Inpatient Physicians', Facility='TriState Memorial Hospital'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='Physicians Clinic Of Spokane'), A(Phys='Pend Oreille River Emergency Physicians, PLLC', Facility='Newport Hospital & Health Services'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='Everett Clinic Lake Stevens'), A(Phys='Northwest Radiologists (NWR)', Facility='ORCAS FAMILY HEALTH CENTER'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='Medical Oncology Associates'), A(Phys='Ballard Emergency Physicians', Facility='Swedish Medical Center/Ballard'), A(Phys='RADIA INC PS', Facility='Swedish Issaquah'), A(Phys='SOUTH SOUND RADIOLOGY', Facility='PROVIDENCE ST PETER HOSPITAL'), A(Phys='Eastside Emergency Physicians, PLLC', Facility='Swedish Medical Center Redmond'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='Odessa Memorial Hospital'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='Spokane Ear Nose Throat Clinic'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='CHAS'), A(Phys='NORTHWEST EMERG PHYS INC', Facility='SAMARITAN HEALTHCARE '), A(Phys='RADIA INC PS', Facility='EDMONDS FAMILY MEDICINE'), A(Phys='OVERLAKE IMAGING ASSOCIATES', Facility='Overlake Hospital Medical Center'), A(Phys='RADIA INC PS', Facility='Western WA Medical Group'), A(Phys='ADVANCED OPEN IMAGING', Facility='ADVANCED EN IMAG'), A(Phys='SOUTH SOUND RADIOLOGY', Facility='GRAYS HARBOR IMAGING'), A(Phys='EVERETT RADIA LLC', Facility='* USE FOR UNKNOWN, UNLISTED OR MULTIPLE LOCATIONS *'), A(Phys='SWEDISH RADIA EDMONDS', Facility='Swedish Medical Center Edmonds'), A(Phys='RADIA INC PS', Facility='SPD CLE ELUM'), A(Phys='RADIA INC PS', Facility='North Idaho Acute Care Hospital'), A(Phys='RADIA INC PS', Facility='Evergreen Hospital Medical Center'), A(Phys='RADIA INC PS', Facility='Mid Valley Medical Group'), A(Phys='RADIA INC PS', Facility='Rockwood Quail Run Clinic'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='Inland at Deer Park'), A(Phys='RADIA INC PS', Facility='Rockwood Clinic'), A(Phys='RADIA INC PS', Facility='Swedish/Edmonds Hospital'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='Inland at Sacred Heart'), A(Phys='RADIA INC PS', Facility='Mid Valley Hospital'), A(Phys='West Sound Emergency Physicians', Facility='Harrison Medical Center Bremerton'), A(Phys='Cascade Radiology Consultants', Facility='Smokey Point Clinic'), A(Phys='RADIA INC PS', Facility='Swedish Medical Center - Cherry Hill'), A(Phys='Seattle Nuclear Medicine (SNM)', Facility='SEATTLE NUCLEAR MEDICINE'), A(Phys='RADIA INC PS', Facility='Rockwood Valley Clinic'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='Providence Health & Serv UrgentCare'), A(Phys='RADIA INC PS', Facility='Sequim Medical Services Building'), A(Phys='OVERLAKE IMAGING ASSOCIATES', Facility='Overlake Hospital Imaging - Tower'), A(Phys='Southland Hospitalist', Facility='St Joseph Hospital WA'), A(Phys='OLYMPIC MEDICAL IMAGING CONSULTANTS', Facility='South Kitsap Advanced Medical Imaging'), A(Phys='RADIA INC PS', Facility='Alaska Neurology Center'), A(Phys='RADIA INC PS', Facility='Rockwood Orthopedics & Sports Med'), A(Phys='COLUMBIA BASIN IMAGING, P.C', Facility='KADLEC MEDICAL CENTER'), A(Phys='NORTHWEST EMERG PHYS INC', Facility='ISLAND HOSPITAL '), A(Phys='SOUTH SOUND RADIOLOGY', Facility='PROVIDENCE DIAG IMAGING CENTER'), A(Phys='TRI-CITY RADIOLOGY, INC', Facility='TRI-CITY RADIOLOGY, INC'), A(Phys='SOUTH SOUND RADIOLOGY', Facility='SOUTH SOUND SURGERY CENTER'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='Swedish Medical Center Seattle'), A(Phys='OLYMPIC MEDICAL IMAGING CONSULTANTS', Facility='Bremerton Advanced Medical Imaging'), A(Phys='Cascade Radiology Consultants', Facility='Cascade Valley Hospital'), A(Phys='RADIA INC PS', Facility='Rockwood Cheney Clinic'), A(Phys='Tri-State Hospitalist Group', Facility='Tri-State Memorial Hospital'), A(Phys='SOUTH SOUND RADIOLOGY', Facility='GRAYS HARBOR CARDIOVASC IMAG'), A(Phys='Sedro-Woolley Emergency Physicians', Facility='United General Hospital'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='Cancer Care Northwest'), A(Phys='RADIA INC PS', Facility='Providence Harbor Pointe'), A(Phys='Discovery Coast Emergency Physicians', Facility='Ocean Beach Hospital'), A(Phys='RADIA INC PS', Facility='Providence Physicians Group Interventional'), A(Phys='RADIA INC PS', Facility='Swedish First Hill Campus'), A(Phys='RADIA INC PS', Facility='Dawn Hastreiter MD RADA'), A(Phys='RADIA INC PS', Facility='Evergreen Radia Imaging Center-Redmond'), A(Phys='Tacoma Emergency Care Physicians, Inc., P.S.', Facility='Allenmore Hospital and Medical Center'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='Arthritis NW Rheumatology PLLC'), A(Phys='PATHOLOGIST REGIONAL LABORATORY', Facility='PATH REGIONAL LAB'), A(Phys='RADIA INC PS', Facility='Snoqualmie Valley Hospital'), A(Phys='OVERLAKE IMAGING ASSOCIATES', Facility='Overlake Imaging Issaquah'), A(Phys='SOUTH SOUND RADIOLOGY', Facility='OLYMPIA MULTI SPECIALTY CLINIC'), A(Phys='Galen Inpatient Services', Facility='Capital Medical Center'), A(Phys='West Sound Emergency Physicians', Facility='Harrison Medical Center Silverdale'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='Swedish Medical Center Redmond'), A(Phys='GEPS PHYSICIAN GROUP OF PENNSYLVANIA PC', Facility='* USE FOR UNKNOWN, UNLISTED OR MULTIPLE LOCATIONS *'), A(Phys='RADIA INC PS', Facility='Providence Monroe'), A(Phys='OVERLAKE IMAGING ASSOCIATES', Facility='NEUROLOGICAL ASSOCIATES'), A(Phys='Cascade Radiology Consultants', Facility='Skagit Valley Clinic'), A(Phys='RADIA INC PS', Facility='EMG Sammamish'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='Inland at Holy Family'), A(Phys='OLYMPIC MEDICAL IMAGING CONSULTANTS', Facility='Silverdale Advanced Medical Imaging'), A(Phys='Columbia Valley Emergency Physicians', Facility='Sunnyside Community Hospital'), A(Phys='Olympic Medical Imaging Consultants, PLLC', Facility='HMC SOUTH KITSAP AMI'), A(Phys='Rural/Metro of Greater Seattle, Inc.', Facility=nan), A(Phys='SOUTH SOUND RADIOLOGY', Facility='WASHINGTON PARK MEDICAL CENTER'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='St Josephs Hospital'), A(Phys='RADIA INC PS', Facility='Mill Creek Family Practice'), A(Phys='RADIA INC PS', Facility='Whidbey General - South Island'), A(Phys='RADIA INC PS', Facility='Rockwood Medical Lake Clinic'), A(Phys='Scheuber Road Emergency Physicians', Facility='Providence Centralia Hospital'), A(Phys='Cascade Radiology Consultants', Facility='Darrington Clinic'), A(Phys='Eastside Emergency Physicians, PLLC', Facility='Swedish Medical Center'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='Evergreen Hematology Oncology'), A(Phys='SOUTH SOUND RADIOLOGY', Facility='MASON GENERAL HOSPITAL'), A(Phys='OVERLAKE IMAGING ASSOCIATES', Facility='* USE FOR UNKNOWN, UNLISTED OR MULTIPLE LOCATIONS *'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='Inland At Sacred Heart'), A(Phys='RADIA INC PS', Facility='Kadlec Medical Center'), A(Phys='RADIA INC PS', Facility='Rockwood South Valley Clinic'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='Pullman Regional Hospital'), A(Phys='RADIA INC PS', Facility='WHIDBEY COMMUNITY PHYSICIANS'), A(Phys='RADIA INC PS', Facility='Rockwood Argonne Urgent Care'), A(Phys='SOUTH SOUND RADIOLOGY', Facility='SUMMIT PACIFIC MEDICAL CENTER'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='Everett Clinic Smokey Point'), A(Phys='RADIA INC PS', Facility='BOEING'), A(Phys='Tacoma Emergency Care Physicians, Inc., P.S.', Facility='Multicare Covington Medical Center'), A(Phys='RADIA INC PS', Facility='Whidbey General - Oak Harbor'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='Providence Family Medicine Hawthorn'), A(Phys='SOUTH SOUND RADIOLOGY', Facility='WESTCARE CLINIC'), A(Phys='NORTHWEST EMERG PHYS INC', Facility='ST ELIZABETH WA HOSPITAL '), A(Phys='RADIA INC PS', Facility='Swedish Seattle-RVIP'), A(Phys='Seattle Emergency Physicians', Facility='Swedish Medical Center/First Hill'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='Everett Clinic Marysville'), A(Phys='OLYMPIC MEDICAL IMAGING CONSULTANTS', Facility='Poulsbo Advanced Medical Imaging'), A(Phys='Northwest Radiologists (NWR)', Facility='BELLINGHAM AMBULATORY SURG CENTER'), A(Phys='RADIA INC PS', Facility='Swedish Mobile Mammography BCHP'), A(Phys='RADIA INC PS', Facility='Swedish/Edmonds Pavilion Imaging'), A(Phys='RADIA INC PS', Facility='Columbia Valley Community Hlth'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='NE Washington Medical Group'), A(Phys='SWEDISH RADIA EDMONDS', Facility='Mill Creek Family Practice'), A(Phys='EVERETT RADIA LLC', Facility='Mark Mayhle MD'), A(Phys='ADVANCED OPEN IMAGING', Facility='* USE FOR UNKNOWN, UNLISTED OR MULTIPLE LOCATIONS *'), A(Phys='NORTHWEST EMERGENCY PHYSICIANS', Facility='ST JOSEPH WA HOSPITAL '), A(Phys='RADIA INC PS', Facility='Olympic Medical Phys Primary Care'), A(Phys='Northwest Radiologists (NWR)', Facility='CARE MEDICAL GROUP EXPRESS CARE'), A(Phys='RADIA INC PS', Facility='Swedish Medical Center - Issaquah'), A(Phys='RADIA INC PS', Facility='Evergreen - Canyon Park'), A(Phys='RADIA INC PS', Facility='Rockwood Liberty Lake Clinic'), A(Phys='NORTHWEST EMERG PHYS INC', Facility='KADLEC MEDICAL CENTER '), A(Phys='Beezley Springs Inpatient Services', Facility='Columbia Basin Hospital'), A(Phys='Olympic Medical Imaging Consultants, PLLC', Facility='HARRISON MEDICAL CENTER - SILVERDALE CAMPUS'), A(Phys='Mt. Rainier Emergency Physicians, PLLC', Facility='Good Samaritan Hospital'), A(Phys='RADIA INC PS', Facility='Obstetrix Seattle Ultrasound'), A(Phys='RADIA INC PS', Facility='Providence Medical Bldg Monroe'), A(Phys='Seahawk Emergency Physicians', Facility='Toppenish Community Hospital'), A(Phys='RADIA INC PS', Facility='SPD Factoria'), A(Phys='NORTHWEST EMERG PHYS INC', Facility='KADLEC EMERGENCY AT KENNEWICK '), A(Phys='Tacoma Emergency Care Physicians, Inc., P.S.', Facility='Tacoma General Hospital'), A(Phys='SOUTH SOUND RADIOLOGY', Facility='PROVIDENCE WEST OLYMPIA CLINIC'), A(Phys='Spokane Tribal Emergency Response', Facility=nan), A(Phys='Direct Radiology', Facility='CASCADE MEDICAL'), A(Phys='NORTHWEST EMERG PHYS', Facility='ST ANTHONY HOSPITAL '), A(Phys='RADIA INC PS', Facility='Rockwood Valley Specialty'), A(Phys='EVERETT RADIA LLC', Facility='Everett Radia Imaging Center'), A(Phys='RADIA INC PS', Facility='Swedish/Edmonds Pavilion Mill Creek'), A(Phys='RADIA INC PS', Facility='Wenatchee Valley Medical Center'), A(Phys='Yakima Emergency Group', Facility='Yakima Regional Med & Cardiac Center'), A(Phys='RADIA INC PS', Facility='Olympic Memorial Hospital'), A(Phys='SOUTH SOUND RADIOLOGY', Facility='RIFFE MEDICAL CENTER'), A(Phys='Emergency Physicians Services', Facility='Providence Holy Family Hospital'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='Inland Imaging Manito Mammography'), A(Phys='RADIA INC PS', Facility='Olympic Medical Imaging Center'), A(Phys='RADIA INC PS', Facility='Rockwood South Hill Urgent Care'), A(Phys='RADIA INC PS', Facility='Whidbey General Hospital'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='Deaconess Medical Center'), A(Phys='OVERLAKE IMAGING ASSOCIATES', Facility='ISSAQUAH URGENT CARE'), A(Phys='RADIA INC PS', Facility='Swedish Mobile Mammography'), A(Phys='Olympic Medical Imaging Consultants, PLLC', Facility='HMC SILVERDALE AMI'), A(Phys='Northwest Radiologists (NWR)', Facility='PH PEACE ISLAND MEDICAL CENTER'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='Sacred Heart Medical Center'), A(Phys='RADIA INC PS', Facility='Providence Medical Group - Snohomish'), A(Phys='RADIA INC PS', Facility='Rockwood North'), A(Phys='RADIA INC PS', Facility='SPD Greenlake'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='Northwest Orthopaedic Specialists'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='Minor And James'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='Deer Park Mobile MRI'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='Lincoln County Hospital'), A(Phys='Olympic Medical Imaging Consultants, PLLC', Facility='HARRISON MEDICAL CENTER - BREMERTON CAMPUS'), A(Phys='Thurston ER Group', Facility='Capital Medical Center'), A(Phys='Olympic Medical Imaging Consultants, PLLC', Facility='TDC URGENT CARE'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='Walla Walla Medical Pavilion'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='Steck Medical Group'), A(Phys='INTEGRA IMAGING BUSINESS ASSOCIATES', Facility='Othello Community Hospital'), A(Phys='Mount Baker Imaging (MBI)', Facility='Washington Locations'), A(Phys='Olympic Medical Imaging Consultants, PLLC', Facility='HMC BAINBRIDGE ISLAND URGENT CARE'), A(Phys='OVERLAKE IMAGING ASSOCIATES', Facility='Overlake Hospital Imaging - Redmond'), A(Phys='SOUTH SOUND RADIOLOGY', Facility='MORTON GENERAL HOSPITAL'), A(Phys='RADIA INC PS', Facility='SPD Queen Anne'), A(Phys='RADIA INC PS', Facility='SPD West Seattle'), A(Phys='AMERICAN MEDICAL RESPONSE', Facility=nan), A(Phys='Lake Tye Emergency Physicians', Facility='Valley General Hospital')}Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    tup
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/idlelib/rpc.py", line 613, in displayhook
    sys.stdout.write(text)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/idlelib/PyShell.py", line 1344, in write
    return self.shell.write(s, self.tags)
KeyboardInterrupt
>>> 
>>> 
>>> 
>>> 
