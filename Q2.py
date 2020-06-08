#Q2
#請寫一個程式,Input 是一個數字,Output 是從 1 到這個數字,扣除掉所有 3 的
#倍數以及 5 的倍數,但是需要保留同時是 3 和 5 的倍數的總數字數。

def remove(num):
  num3 = num//3 
  num5 = num//5 
  num15 = num//15 
  return num - num3 - num5 + 2*(num15)
  
print(remove(30))