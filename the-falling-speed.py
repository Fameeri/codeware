#https://www.codewars.com/kata/5a0be7ea8ba914fc9c00006b/train/python

def sakura_fall(v):
    # your code here
    height = 5 * 80
    
    if v <= 0:
        return 0
    
    return height / v
