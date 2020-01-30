
def binarySearch(array,k,end):

	first = 0;
	
	while (first < end) :
		mid = (first + end)/2;
		if k == array[mid] :
			return 1;
		elif k > array[mid] :
			first = mid + 1;
		else :
			end = mid -1;
	
	return -1;

cases = input()
for i in range(cases):	
	arr = []	
	n = int(input())
	k = int(input())
	for i in range(n):
		a = int(input())
		arr.append(a);
	print(binarySearch(arr,k,n-1));


		
	 	
	
