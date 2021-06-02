import time
import datetime
from colorama import Fore
from colorama import Style
print("So you like prime numbers? Name every prime number")
time.sleep(4)
times = datetime.datetime.now()
times = str(times)
times = times.split()
dates = times[0]
times = times[1]
times = times.replace(":", " ")
times = times.replace(".", " ")
times = times.split()
originalsec = int(times[2])
originalsecmin = int(times[1])
originalsechou = int(times[0])
totalprime = 0
primecheck = 0
x3 = [3]
print("2\n3")
x1 = 5
while True:
    try:
      start = time.time()
      x2 = 0
      for (COUNT) in range(len(x3)):
          if x1 % x3[COUNT] == 0:
              x2 = 1
              break
              #Half check
          elif x3[COUNT] > x1/2:
            break
            #Half check end
      if x2 == 0:
        totalprime = totalprime + 1
        primecheck = primecheck + 1
        if primecheck == 1:
          primecheck = 0
          place = "{:,}".format(totalprime)
          print(f"Running Since: {Fore.YELLOW}{dates} @ {originalsechou}:{originalsecmin} UTC{Style.RESET_ALL} \|/ Total Prime Numbers Counted: {Fore.YELLOW}{place}{Style.RESET_ALL}")
        end = time.time()
        total = end - start
        total = float(total)
        total = "{:,.3f}".format(total)
        total = total.replace(",", "")
        total = total.replace(".", " ")
        total = total.split()
        mila = int(total[1])
        mila = "{:,}".format(mila)
        placex = "{:,}".format(x1)
        mila = mila.replace("-", "")
        seconds = total[0]
        seconds = str(seconds)
        if "-" in seconds:
          seconds = 0
        print(f"Time Taken: {Fore.GREEN}{seconds}{Style.RESET_ALL} seconds {Fore.GREEN}{mila}{Style.RESET_ALL} ms       Prime Number: {Fore.GREEN}{placex}{Style.RESET_ALL}\n")
        x3.append(x1)
      x1 = x1 + 2
    except:
      print(f"{Fore.RED}THERE WAS AN ERROR{Style.RESET_ALL} ")