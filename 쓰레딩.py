import threading
import time
telnet_IP = ['10','11','12','13','14','15']

import threading
sem = threading.Semaphore(5)

def telnet_ftth(IP):
    sem.acquire()
    print (IP)
    time.sleep(2)
    sem.release()


threads = []
for x in telnet_IP :
    th = threading.Thread(target=telnet_ftth, args=(x,),daemon=True)
    threads.append(th)
    th.start()         # 종료대기
for i, thread in enumerate(threads) :
    thread.join()
print('Finished')

