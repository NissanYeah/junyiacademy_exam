#Q1-A (A)請寫一個程式把裡面的字串反過來。
def reverse(txt):
  return txt[::-1]

print(reverse("junyiacademy"))

#Q1-B (B)請寫一個程式把裡面的字串,每個單字本身做反轉,但是單字的順序不變。
def reverseWord(txt):
  word_list = txt.split()
  result = ''
  for word in word_list:
    result += reverse(word) + ' '
  return result

print(reverseWord("flipped class room is important"))