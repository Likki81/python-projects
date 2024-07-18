import time
def time_countdown(seconds):
    while True:
      mins,secs=divmod(seconds,60)
      timer='{:02d}:{:02d}'.format(mins,secs)
      print(timer,end='\r')
      time.sleep(1)
      seconds-=1
    print("time out")  
try:
    seconds=int(input('enter a secods'))   
    time_countdown(seconds) 
except valueError:
    print("Invalid input please enter time in seconds")   
    
