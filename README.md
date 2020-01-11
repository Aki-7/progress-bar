# Progress Bar

This works with python3

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

![sample](https://gyazo.com/863a9017c1e4f5ee759046169a0aa733/raw)

Progress state format should be like this: `#P 2/100\n`
