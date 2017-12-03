import time
from threading import Thread
import sys

def wordcounter(filename):
    print("Counting words in: %s " % filename)
    time.sleep(5)
    print("There are %d words in %s." % (len(open(filename, "r+").read().split()), filename))


if __name__ == "__main__":
    for i in range(1, len(sys.argv)):
        # wordcounter(sys.argv[i])
        t = Thread(target=wordcounter, args=(sys.argv[i],))
        t.start()
