import time
for i in range(1, 6):
    print("  ", i, end="\r")
    time.sleep(1)
    if i =="5":
        print("Loading end")