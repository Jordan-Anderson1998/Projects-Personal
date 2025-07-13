def factorial(x)
  total = 1
  for number in (1..x).to_a do
    total *= number
  end
  return total
end
