#O(n)
num_list = []
def positive_sum(arr):
    for n in arr:# O(n)
        if n >= 1: # O(1)
            num_list.append(n)# O(1)
            answer = sum(num_list)# O(1)
            print(answer)# O(1)
            
positive_sum([1,-4,7,12])