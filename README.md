# Progress Bar

This only works with python3

Use this script like this.

```
$ ./test.py | ./main.py
```

```py
# test.py
N = 100
for i in range(N):
  # Don't forget to flush
  print("#P {}/{}".format(i,N), flush=True) # write progress state to stdout
  print("log: {}".format(i)) # you can write other log output
  sleep(1)
```

Progress state format should be like this: `#P 2/100\n`
