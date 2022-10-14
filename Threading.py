import threading
import time

start=time.perf_counter()

def do_something(seconds):
    print(f"Sleep for {seconds} seconds")
    time.sleep(seconds)
    print("function got executed properly")

threads=[]
for _ in range(10):
    t=threading.Thread(target=do_something,args=(2,))
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish=time.perf_counter()
print(f"Program finished in {round(finish-start,2)} seconds")


*************************************************************************************
import concurrent.futures
import time

start=time.perf_counter()

def do_something(seconds):
    print(f"Sleep for {seconds} seconds")
    time.sleep(seconds)
    return "function got executed properly"

def do_something1(seconds):
    print(f"Sleep for {seconds} seconds")
    time.sleep(seconds)
    return f"finished at {seconds} seconds"

with concurrent.futures.ThreadPoolExecutor() as thread:
    #submit executes the target object and provide result based on completion status
    threads=[thread.submit(do_something,1) for _ in range(10)]
    for data in concurrent.futures.as_completed(threads):
        print(data.result())

    #Map exceutes and returns result of target object sequentially
    secs = [5, 4, 3, 2, 1]
    thread1=thread.map(do_something1,secs)
    for r in thread1:
        print(r)

finish=time.perf_counter()
print(f"Program finished in {round(finish-start,2)} seconds")