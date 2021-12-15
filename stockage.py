import shutil
from progress.bar import Bar
total, used, free = shutil.disk_usage("/")
from math import ceil
import os

os.system("clear")
print("=============== Disk space ===============")
print(" ")
d = used / total
eamount = ceil(100 * d)
bar = Bar('\033[1mDisk size\033[m', max=100)
for i in range(eamount):
    bar.next()
bar.finish()
print("\033[1mTotal :\033[m %d Go" % (total // (2**30)))
print("\033[1mUsed :\033[m %d Go" % (used // (2**30)))
print("\033[1mRemaining :\033[m %d Go" % (free // (2**30)))
print(" ")
print("===========================================")