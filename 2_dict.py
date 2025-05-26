marks = {
    "Ram": 100,
    "Rohan": 90,
    "Arpit": 80,
    0: "Happy"
} 
print(marks.items()) #it print in form of list inside that it's like tuple form
print(marks.keys()) #it print key of the marks like Ram ,Arpit,0 etc.
print(marks.values()) #it print value of the marks like 90 ,100,happy etc.


marks.update({"Arpit": 89}) # that show dictionary is mutable
print(marks) 