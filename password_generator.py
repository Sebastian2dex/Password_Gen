import random

lc="abcdefghijklmnopqrstuvwxyz"
uc="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sym="'*:/!?+=%)(-_&$#@[]£€¥¢^><|~¿"
num="1234567890"

l=8

j=lc+uc+sym+num

password="".join(random.sample(j,l))

print("Generated password:",password)