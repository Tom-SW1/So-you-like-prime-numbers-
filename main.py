import time
import datetime
import multiprocessing
from colorama import Fore
from colorama import Style
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
file = open("primes.txt", "r")
lists = file.read()
file.close()
x3 = lists.split()
x1 = int(lists[0])
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
        place = "{:,}".format(totalprime)
        print(f"Running Since: {Fore.YELLOW}{dates} @ {originalsechou}:{originalsecmin} UTC{Style.RESET_ALL} \|/ Total Prime Numbers Counted: {Fore.YELLOW}{place}{Style.RESET_ALL}")
        file = open("primes.txt", "r")
        data = file.read()
        file.close()
        file = open("primes.txt", "w")
        filew = file.write(f"{x1} {data}")
        file.close()
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
        print(f"Time Taken: {Fore.GREEN}{seconds}{Style.RESET_ALL} seconds {Fore.GREEN}{mila}{Style.RESET_ALL} ms       Prime Number: {Fore.GREEN}{placex}{Style.RESET_ALL}\n")
        x3.append(x1)
      x1 = x1 + 2
    except:
      print(f"{Fore.RED}THERE WAS AN ERROR{Style.RESET_ALL}") 