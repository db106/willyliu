import datetime
from datetime import timedelta



t1 = datetime.datetime(2020, 5, 23, 11, 00) ; print(t1)
t_s = datetime.datetime(2020, 5, 23, 11, 2) ; print(t_s)
nn = t_s - t1
print('nn:', type(nn), nn)
print(nn > timedelta(minutes=0))
