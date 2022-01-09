def pairListFibonacci(limit):
  currentInt = 8
  fibList = [1,2,8]
  while currentInt<limit:
    currentInt += fibList[len(fibList)-2]
    if currentInt%2:
      fibList.append(currentInt)
    
  return fibList

def sumListElements(list):
  total = 0
  for i in list:
    total += i
  return total
print(pairListFibonacci(4000000))
#print(pairListFibonacci(4000000)) 
#print(sumListElements(pairListFibonacci(4000000)))
