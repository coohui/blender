names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
def test(n):
  print(n)
  if n == 'Bob':
    return '我是第一名Bob'
  elif n == 'Tom':
    return '我是第二名Bob'
  else:
    return n

new_names = [test(name) for name in names if len(name)>0]
print(new_names)