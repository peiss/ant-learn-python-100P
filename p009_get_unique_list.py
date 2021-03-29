def get_unique_list(lista):
  result = []
  for item in lista:
    if item not in result:
      result.append(item)
  return result


lista = [10, 20, 30, 10, 20]
print(f"source list {lista}, unique list:", get_unique_list(lista))

print(f"source list {lista}, unique list:", list(set(lista)))