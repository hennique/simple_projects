# 0 to 9 will return 10; 10 to 19 will return 20; and so on
def to_next_multiple_of_ten(n):
  return n + (10 - int(str(n)[-1]))
