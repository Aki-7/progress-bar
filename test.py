#! python3

from time import sleep

N = 100
for i in range(N+1):
    print("#P {}/{}".format(i, N), flush=True)
    print("log: {}".format(i))
    sleep(0.1)

print("#P exit")
