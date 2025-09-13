s1 = input("String1: ")
s2 = input("String2: ")
matches = [ ]
s1_len = len(s1)
s2_len = len(s2)
for i in range(s1_len):
 if (s1[i:i+s2_len]) == s2:
  matches.append(i+1)
print(*matches)
