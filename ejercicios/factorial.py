def calcularFactorialRecursivo(factorial: int)-> int:
  if factorial == 0 or factorial == 1:
    return 1
  else:
    return factorial * calcularFactorialRecursivo(factorial - 1)