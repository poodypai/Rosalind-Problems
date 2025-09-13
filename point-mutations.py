str1 = list(input("Strand 1: ").strip())
str2 = list(input("Strand 2: ").strip())
count = 0

for i in range(len(str1)):
  if str1[i] == str2[i]:
    pass
  else:
   count += 1

print(count)
