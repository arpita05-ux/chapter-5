marks = {
    "Ram": 100,
    "Rohan": 90,
    "Arpit": 80,
    0: "Happy"
} 
print(marks.items()) #it print in form of list inside that it's like tuple form
print(marks.keys()) #it print key of the marks like Ram ,Arpit,0 etc.
print(marks.values()) #it print value of the marks like 90 ,100,happy etc.


marks.update({"Arpit": 89 , "sika": 8}) # that show dictionary is mutable, we can add anything and it will change in main dict. 
print(marks) 


print(marks.get("Ram2")) #print none
print(marks.get["Ram2"])  # returns  an error both are not same 

#both give same results when "Ram" and print 100 so for checking there is difference b/w them we do error and wrote "Ram2" for different result.