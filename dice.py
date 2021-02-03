#!/usr/bin/env python3
from sys import argv
from random import seed
from random import random
from random import randint

#seed(1)

arg = int(argv[1])
num = int(argv[2])

for _ in range(num):
	res = randint(0, arg)
	print(res)
