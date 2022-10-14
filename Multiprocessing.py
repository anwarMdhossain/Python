#import multiprocessing
import concurrent.futures
import time

start=time.perf_counter()

def do_something(seconds):
    print(f"Sleep for {seconds} seconds")
    time.sleep(seconds)
    return "function got executed properly"


'''if __name__ == '__main__':
    multiprocessing.freeze_support()
    processes=[]
    for _ in range(10):
        p=multiprocessing.Process(target=do_something,args=(1,))
        p.start()
        processes.append(p)
    
    for process in processes:
        process.join()'''

if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executer:
        process=[executer.submit(do_something,2) for _ in range(10)]
        
        for pr in concurrent.futures.as_completed(process):
            print(pr.result())
  
    finish=time.perf_counter()
    print(f"Program finished in {round(finish-start,2)} seconds")