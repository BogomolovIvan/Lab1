import time

name = 'Ivan'
start_time = time.time()

while 1:
    time.sleep(5)
    print('My name is: ' + name)
    summary_time = time.time() - start_time
    print('Summary time: ' + str(summary_time))
