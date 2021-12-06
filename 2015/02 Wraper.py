# -*- coding: UTF8 -*-

s = 0
r = 0
file = open('.data/02.input.txt', 'r') 
for line in file: 
  ls, ws, hs = line.split('x')
  dim = [int(ls), int(ws), int(hs)]
  dim.sort()

  s = s + (2*dim[0]*dim[1] + 2*dim[1]*dim[2] + 2*dim[0]*dim[2] + dim[0]*dim[1])
  r = r + 2*dim[0] + 2*dim[1] + dim[0]*dim[1]*dim[2]

print (s, r)

