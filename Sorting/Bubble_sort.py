def bubbleSort(nlist):
	for passnum in range(len(nlist)-1,0,-1):
		for i in range(passnum):
			if nlist[i]>nlist[i+1]:
				temp = nlist[i]
				nlist[i] = nlist[i+1]
				nlist[i+1] = temp
	return nlist

nlist = [14,46,43,27,57,41,45,21,70]
print("Source list:", nlist)

sorted_list = bubbleSort(nlist)
print("Sorted list:", sorted_list)
