def fizzBuzz(n):
  if n == 42:
    return "The meaning of life"
  if n % 3 == 0 and n % 5 == 0:
    return "FizzBuzz"
  if n % 3 == 0:
    return "Fizz"
  if n % 5 == 0:
    return "Buzz"
  return str(n)

# PASTE YOUR TESTS BELOW HERE:
