#filename: _1259_2.py
while True:
  number = str(input())
  if number == '0':
    break
  flag = "no"
  if number == number[::-1]:
    flag = "yes"
  print(flag)
  
  