strand = input("Enter Strand: ")
count_A, count_C, count_G, count_T = 0, 0, 0, 0

for i in range(len(strand)):
 if strand[i] == 'A':
  count_A += 1
 elif strand[i] == 'C':
  count_C += 1
 elif strand[i] == 'G':
  count_G += 1
 else:
  count_T += 1

print(f"{count_A} {count_C} {count_G} {count_T}")
