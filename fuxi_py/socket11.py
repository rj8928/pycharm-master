from socket import *


s = socket(AF_INET, SOCK_STREAM)
a = []
a.append(s)
s = socket(AF_INET, SOCK_STREAM)
a.append(s)

for s in a:
    print(s)