#!/usr/bin/env python
# coding: utf-8

'''
UNIT TEST for Python's multiprocessing module.

this unit test first runs a base-function sequentially, before running in parallel.
the base function is simply a sleep time of 1s.

the sequential portion runs the base-function 60 times, which should result in a wait time of 60 seconds.

if working correctly, the multiprocessing portion will run the 60 base-function iterations in parallel, which should result in a wait time significantly less than 60 seconds (~approx 1s). 
'''

#setup
import time
from multiprocessing import Process

n=60

#base-function
def t():
    time.sleep(1)

#test
if __name__ == '__main__':

  #sequential
  start_time = time.time()
  for _ in range(n):
      t()
  print("Sequential run time: %.2f seconds" % (time.time() - start_time))

  #parallel
  start_time = time.time()
  processes = []
  for _ in range(n):
    p = Process(target=t)
    processes.append(p)
    p.start()

  for process in processes:
    process.join()

  print("Parallel run time: %.2f seconds" % (time.time() - start_time))