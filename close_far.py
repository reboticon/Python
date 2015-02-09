def close_far(a, b, c):
  list1 = [a,b,c]
  list1.sort()
  a,b,c = list1[0],list1[1],list1[2]
  if abs(a-b) < 2 and abs(a-c) <= 2: return False
  return True  
 
  
  
