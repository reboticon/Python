def lucky_sum(a, b, c):
  sum1 = a + b + c
  if a == 13 or b == 13 or c == 13:
    sum1 = sum1 - 13
    print sum1
  if a == 13: sum1 - b
  print sum1
  if b == 13: sum1 - c
  print sum1
  return sum1


lucky_sum(1, 13, 3)

-2 - -20 (18) ok
abs(-2) - abs(-20) (-18) WRONG
abs (-2) - -20 (18) ok
-2 - abs(-20) -22 WRONG

-2 + -20 (-22) WRONG
abs(-2) + -20 (-18) WRONG
abs(-2) + abs(-20) (22) WRONG
-2 + abs(20) 18 ok


abs(-2 --20)
  

a_b, a_c, b_c = abs(a-b), abs(a-c), abs(b-c)
  if (a_b < 2 or a_c < 2 or b_c < 2) and (a_b >=2 or a_c >=2 or b_c >=2):
    return True
  return False

sort()
