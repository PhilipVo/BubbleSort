from random import randint

def bubbleSort(li):
	# for i in range (0, len(li)-1):
	# 	for j in range (i+1, len(li)):
	# 		if li[i] > li[j]:
	# 			temp = li[i]
	# 			li[i] = li[j]
	# 			li[j] = temp
	i = 0
	end = len(li)-1
	while i < end:
		j = i + 1
		if li[i] > li[j]:
			temp = li[i]
			li[i] = li[j]
			li[j] = temp
		if i == end - 1:
			i = 0
			end -= 1
			continue
		i += 1




# li = [5,7,2,6,86,34,8,23]
li = []
for i in range (0, 100):
	li.append(randint(0, 10000))
print 'Unsorted:'
print li
print
bubbleSort(li)
print 'Sorted:'
print li
