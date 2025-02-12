""""""

import json
import datetime
from datetime import datetime as dt
# from datetime import *
import time

start_dt = dt.now()
# time.sleep(5)


print(datetime.datetime.now())

print(dt.now() - start_dt)

my_dict: dict = {
    'name': 'Maks',
    'age': 27,
    't': None
}



with open('/Users/mvstrometskiy/home_programs/hubble_course/group/lessons/my_t.json', 'w') as f:
   json.dump(my_dict, f)

with open('/Users/mvstrometskiy/home_programs/hubble_course/group/lessons/my_t.json', 'r') as f:
    m = json.load(f)

with open('/Users/mvstrometskiy/home_programs/hubble_course/group/lessons/my_txt.txt', 'w') as f:
    f.write('jhsvdfjshvhdkshvhdsj')


my_txt = open('/Users/mvstrometskiy/home_programs/hubble_course/group/lessons/my_txt.txt', 'r')
print(my_txt.readlines())
my_txt.close()

