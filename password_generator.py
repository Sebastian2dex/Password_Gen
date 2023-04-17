import random
import string

wd = string.ascii_letters
sym="'*:/!?+=%)(-_&$#@[]£€¥¢^><|~¿"
num=string.digits

l=8

j=wd+sym+num

password="".join(random.sample(j,l))

print("Generated password:",password)
