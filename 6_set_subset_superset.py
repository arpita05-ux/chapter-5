s1 = {1,2,3}   # eg of subset in s1 should be {1,2} or{2,3} etc
s2 = {1,2,3,4,5}

print(s1.issubset(s2))  # here s1 is part of s2 so , s1 is subset of s2
print(s2.issuperset(s1)) #here s2 is superset because all element in s1 present in s2 