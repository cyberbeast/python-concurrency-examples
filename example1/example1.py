import time
from threading import Thread

def myfunc(i, param):
    print("sleeping 5 sec from thread %d" % i)
    time.sleep(5)
    print( "finished sleeping from thread %d: %s" % (i, param))

param = "hello"
for i in range(10):
	param = "hello" if param == "goodbye" else "goodbye"
	# myfunc(i, param)
	t = Thread(target=myfunc, args=(i,param,))
	t.start()