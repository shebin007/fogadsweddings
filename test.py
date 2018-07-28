list = [12,24,35,24,24,88,120,155,88,120,155]
range  = []
for i in list[::-1]:
  flag = 0
  for j in range :
    if i == j:
      flag = 1
  if flag == 1 :
    continue
  else :
    range.append(i)
	
print range
