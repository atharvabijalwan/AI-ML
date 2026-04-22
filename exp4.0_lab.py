import pandas as pd
2 import numpy as np
3
4 df = pd . read_csv ( " data_summary . csv " )
5
6 print ( df )
7 print ( " df done --------------- " )
8 print ( df . shape )
9 print ( " shape line done -------------- " )
10 print ( df . columns )
11 print ( " column ------------ " )
12 print ( df . head (2) )
13 print ( df . tail (2) )
14 print ( " head and tail done --- ------ ------ --- " )
15 print ( df . isnull () . sum () )
16 print ( df . isnull () . sum () / len ( df ) *100)