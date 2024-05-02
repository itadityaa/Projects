# Description: This program reads a file called coding_qual_input.txt and generates a sentence based on the triangular numbers in the file.

def generate_triangular_numbers(limit):
  """Generates triangular numbers up to a limit.

  Args:
      limit (_type_): Upper limit for the triangular numbers.

  Yields:
      _type_: The next triangular number in the sequence.
  """  
  n = 1
  while True:
      triangular_num = n * (n + 1) // 2
      if triangular_num <= limit:
          yield triangular_num
          n += 1
      else:
            break

def sentence_formation():
  """Generates a sentence based on the triangular numbers in the file.

  Returns:
      str : The sentence formed from the triangular numbers in the file.
  """  
  hashmap = {}
  with open ('coding_qual_input.txt', 'r') as file:
    data = file.readlines()
    for dataa in data:
      hashmap[int(dataa.split()[0])] = dataa.split()[1]

  max_hash = max(hashmap)

  triangular_numbers = list(generate_triangular_numbers(max_hash))

  final_output = []
  for num in triangular_numbers:
    if num in hashmap:
      final_output.append(hashmap[num])

  return ' '.join(final_output)

print(sentence_formation())