import numpy as np
x1 = [0,0,1,1]
x2 = [0,1,0,1]
yd = [0,1,1,1] 
errors = [None, None, None, None] 
w1 = 0.13
w2 = 0.1
th = 0.3 
lr = 0.5
def checkForError(listOfErrors): 
  for element in listOfErrors:
    if element is not 0:
      return False
  return True
def step(yp):
  return 1 if yp>0 else 0 

epoch = 1
while True:
  for i in range(4): 
    yp = x1[i] * w1 + x2[i] * w2 - th
    yp = step(yp)
    errors[i] = yd[i] - yp
    w1 += lr * x1[i] * errors[i]
    w2 += lr * x2[i] * errors[i]
  result = checkForError(errors) 
  if (result is True):
    break;  
  epoch+=1
print("epoch = ",epoch,",and weights w1 =", w1,",w2 =", w2)
p1 = 1
p2 = 0
yp = p1*w1+p2*w2-th
yp = step(yp)
print("Input p1 = ",p1,", p2 = ",p2 ,", and predicted result : ",yp)
