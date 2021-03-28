
def get_even_numbers(begin, end):
  result = []
  for item in range(begin, end):
    if item % 2 == 0:
      result.append(item)
  return result

begin = 4
end = 15
print(f"begin={begin}, end={end}, even numbers: ", get_even_numbers(begin, end))

data = [item for item in range(begin, end) if item % 2 == 0]
print(f"begin={begin}, end={end}, even numbers: ", data)