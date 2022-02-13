def fizzBuzz(n):
  fb = " ".join([
    "Fizz" if n % 3 == 0 else "", 
    "Buzz" if n % 5 == 0 else "",
  ])

  if (fb == ""):
    return n

  return fb

# PASTE YOUR TESTS BELOW HERE:
