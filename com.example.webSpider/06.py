__author__ = 'summer'

import re


IP = r"((1{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}\2"



print re.findall(IP, "192.168.1.1")

print(re.search(r'FishC', 'I love FishC.com'))

print re.findall('\w', 'hello !!!')

print re.findall('\W', 'hello !!!')

p = re.compile(IP)

P_2 = re.compile(r"""
   (?:(?:1?[1-9]?\d   #1-199
   |2[0-4]\d          #200-249
   |25[0-5])          #250-255
   \.){3}
   (?:1?[1-9]?\d
   |2[0-4]\d
   |25[0-5])          #get group 2
""", re.VERBOSE)

ret = p.search("192.168.1.2ss.add.156.123.2.2").group()
ret_2 = P_2.findall("192.168.1.2ss.add.156.123.2.2")
print(ret_2)
print(ret+ " here!")
print(p.findall("156.123.2.2"))

