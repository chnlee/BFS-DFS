def recursive_function():
  print('재귀 함수를 호출합니다.')
  recursive_function()

def recursive_function(i):
  if i == 100:
    return
  print(i, '번째 함수에서', i+1, '번째 재귀 함수를 호출한다.')
  recursive_function(i+1)
  print(i,'번째 재귀 삼수를 종료합니다.')

recursive_function(1)

#반복적으로 구현한 n!
def factorial_iterative(n):
  result = 1
  # 1부터 n까지의 수를 차례대로 곱하기
  for i in range(1,n+1):
    result *= i
  return result

#재귀함수를 이용해 구현한 n!
def factorial_recursive(n):
  if n <= 1:
    return 1
  #n! = n * (n-1)!를 그대로 코드로 작성하면 된다.
  return n * factorial_recursive(n-1)

print(factorial_iterative(5))
print(factorial_recursive(5))