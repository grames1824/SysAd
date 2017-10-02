# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 16:01:42 2017

@author: Hular
"""

class Des(object):

  table={}
  table[1] = ( 57,49,41,33,25,17,9,
               1,58,50,42,34,26,18,
              10,2,59,51,43,35,27,
              19,11,3,60,52,44,36,
              63,55,47,39,31,23,15,
               7,62,54,46,38,30,22,
              14,6,61,53,45,37,29,
              21,13,5,28,20,12,4)
  
   
  table[2] = 1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1
  table[3] = (14,17,11,24,1,5,
       3,28,15,6,21,10,
       23,19,12,4,26,8,
       16,7,27,20,13,2,
       41,52,31,37,47,55,
       30,40,51,45,33,48,
       44,49,39,56,34,53,
       46,42,50,36,29,32)
  table[4] = (58,50,42,34,26,18,10,2,
	60,52,44,36,28,20,12,4,
	62,54,46,38,30,22,14,6,
	64,56,48,40,32,24,16,8,
	57,51,41,33,25,17,9,1,
	59,53,43,35,27,19,11,3,
	61,55,45,37,29,21,13,5,
	63,57,47,39,31,23,15,7)
  
  table[5]= ( 32,1,2,3,4,5,
               4,5,6,7,8,9,
               8,9,10,11,12,13,
               12,13,14,15,16,17,
               16,17,18,19,20,21,
               20,21,22,23,24,25,
               24,25,26,27,28,29,
               28,29,30,31,32,1)

  s={}

  s[1] = (14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7,
	0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8,
	4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0,
	15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13)
  s[2] = (15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10,
	3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5,
	0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15,
	13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9)

  table[7] = (16,7,20,21,
	29,12,28,17,
	1,15,23,2,6,
	5,18,31,10,
	2,8,24,14,
	32,27,3,9,
	19,13,30,6,
	22,11,4,25)

  #key = key[:8]
  #message = message[:8]
  key = "133457799BBCDFF1"
  message = "0123456789ABCDEF"

  def getBits(self, ch):
    #convert char to ascii value, then to binary
    return ('00000000' +bin(ord(ch))[2:])[-8:]

  def getBitsFromHex(self, ch):
    #must return exactly 4 bits
    return ('0000' +bin(int(ch,16))[2:])[-4:]

  def getBinary(self, msg):
    #convert message/key to binary
    mk = ""
    for ch in msg:
      mk += self.getBitsFromHex(ch)
    return mk

  def permute(self, table, msg):
      #permutation
    p = ""
    for x in self.table[table]:
      p += msg[x-1:x]
    return p 

  def shift(self, msg, round):
    shift_ctr=0
    m=msg
    while shift_ctr < self.table[2][round-1]:
      m=m[1:]+m[0]
      shift_ctr += 1
      return m

  def getHex(self, msg):
    i=0
    h=""
    while i<len(msg):
      b4 = msg[i:i+4]
      h += hex(int(b4,2))[2:]
      i += 4
    return h
 
  def displayHex(self, msg):
    i=0
    while i<len(msg):
      b4 = msg[i:i+4]
      print (hex(int(b4,2))[2:])
      i += 4
    return

def main():

  e = Des()

  messageb = e.getBinary(e.message)
  keyb = e.getBinary(e.key)
  print (keyb)
#first step
  rounds=16
  r=0
  while r<=rounds:
    if (r==0):
      table=1
      p=e.permute(table, keyb)
      c=p[:28]
      d=p[28:]
      k=keyb
      print ("c " + c)
      print ("d " + d)
      
    else:
      c=e.shift(c,r)
      d=e.shift(d,r)
      k=e.permute(3,c+d)
          
    print ("Round: ")
    print (r)
    print ("c " + c)
    print ("d " + d)
    print ("k " + k)
    
    r += 1
    
  table=4
  p=e.permute(table, messageb)
  ip=p[:64]
  
  #second step
  m=messageb
  print ("Message in binary: " + m)
  print ("Encrypted message: " + ip)
  
  r=ip[32:]
  l=ip[:32]
  print ("Left: " + l)
  print ("Right: " + r)
  
  IProunds=16
  IPr = 0
  while IPr<=IProunds:
    if (IPr==0):
      table=1
      p=e.permute(table, keyb)
      c=p[:28]
      d=p[28:]
      k=keyb
      
      
      print ("c " + c)
      print ("d " + d)
      
    else:
      c=e.shift(c,r)
      d=e.shift(d,r)
      k=e.permute(3,c+d)
          
    print ("Round: ")
    print (r)
    print ("c " + c)
    print ("d " + d)
    print ("k " + k)
    
    r += 1
    
  
  

  
  

main()

