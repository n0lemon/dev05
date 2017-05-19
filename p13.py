import numpy as np
#import pandas as pd

NU = 100 #neuron
TD=np.empty((4,NU)) #stoned data

A = 10.0
KF = 0.2
KR = 0.9
AI = 2.0
EXP = 0.015

H = np.empty(NU)
_H = np.empty(NU)
Z = np.empty(NU)
_Z = np.empty(NU)
X = np.empty(NU)
_X = np.empty(NU)

W = np.zeros((NU,NU)) 
#OUT_X = np.zeros((10,10)) #for output

#teacher data
TD = np.array([[1, 1, 0, 0, 0, 0, 0 ,0, 1, 1, 
                1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 
                0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 
                0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 
                0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 
                0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 
                0, 0, 1, 1, 1, 1, 1, 1, 0, 0,
                0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 
                1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 
                1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
               
      	       [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 
	        0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 
	        0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 
	        0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 
	        0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 
	        0, 0, 1, 1, 1, 0, 1, 1, 1, 0,
	        0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 
	        0, 1, 1, 1, 0, 0, 0, 1, 1, 1,
	        0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
	        0, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],

	       [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 
	        0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
	        1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 
	        1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 
	        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
	        0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 
	        0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 
	        1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
	        1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 
	        0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

	       [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 
	        0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 
	        0, 0, 1, 1, 1, 1, 1, 1, 0, 0,
	        0, 0, 1, 1, 1, 1, 1, 1, 0, 0,
	        0, 0, 1, 1, 1, 1, 1, 1, 0, 0,
	        0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 
	        1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
	        0, 0, 0, 1, 1, 1, 1, 0, 0, 0,
	        0, 0, 0, 0, 1, 1, 0, 0, 0, 0,
	        0, 0, 0, 0, 0, 1, 0, 0, 0, 0 ]])


def sig(y):#array
  global EXP 
  return 1/(1+np.exp(-y/EXP))
  
def __init__():
  global X, H, Z
  X[:] = 0.0
  H[:] = 1.0
  Z[:] = 1.0

  
def GenerateW():
  global W, TD
  # array @ array /// @ = *
  # scalar * array 
  W = ((2 * TD.T - 1) @ (2 * TD - 1)) /4

    
def Run(OT):
  global X, _X
  global Z, _Z
  global H, _H
  global W, KF, KR, AI
  
  SUM = np.zeros(NU)
  
  for t in range(OT):
    print("time is " + str(t))
    SUM[:] = 0.0

    SUM = W @ X 
      
    _H = KF * H + SUM 
    _Z = KR * Z - A * X + AI 
    _X = sig(_H + _Z)

    #finished calculate
    #output
    
    for j in range(NU):
      if X[j] >= 0.5:
        print ("@", end=' ')
      else:
        print (".", end=' ')
        
      if (j+1) % 10 == 0:
        print("\n")
        
    X = _X.copy()
    H = _H.copy()
    Z = _Z.copy()
    
    print("\n")

  #printAr()  

'''  10 * 10 ver output
def printAr():
  global X
  for k in range(NU):
    if X[k] >= 0.5:
      i = k - int(k / 10) * 10#x
      j = 9 - int(k / 10)#y sita ga 0 - 10
      print(int(i+1), end=" ")
      print(int(j+1))
'''
    
def main():
  OT = int(input('time is :'))
  __init__()
  GenerateW()
  Run(OT)

if __name__ == '__main__':
  main()

