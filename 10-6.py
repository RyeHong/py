import multiprocessing
import time
from random import randint

def loopy():
    for num in range(0,3):
        now = time.time()
        print(time.ctime(now))

        time.sleep(randint(1, 5))
if __name__ == "__main__":
    loopy()
    p = multiprocessing.Process(target=loopy)
    p.start()
    p.terminate()
