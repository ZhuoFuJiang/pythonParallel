import threading
from threading import Thread
from threading import BoundedSemaphore


def function(i):
    print("function called by thread %i" % i)
    return


threads = []

for i in range(5):
    t = Thread(target=function, args=(i, ))
    threads.append(t)
    t.start()


# alive_nums = len(threads)
# while alive_nums != 0:
#     for t in threads:
#         if not t.is_alive():
#             # print("完成线程", t.getName())
#             alive_nums -= 1
#     if alive_nums == 0:
#         break
#     alive_nums = len(threads)


# while True:
    # print(threading.activeCount())
    # if threading.activeCount() == 1:
    #     break

while True:
    if len(threading.enumerate()) == 1:
        break
print("所有线程结束")
