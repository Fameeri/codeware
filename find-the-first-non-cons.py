#https://www.codewars.com/kata/58f8a3a27a5c28d92e000144/train/python

def first_non_consecutive(arr):
    if len(arr) < 2:
        return None
    
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]+ 1:
            return arr[i]
        
    return None