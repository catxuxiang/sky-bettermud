'''
Created on 2012-4-14

@author: Sky
'''
a = {}
a["111"] = "222"
a["333"] = "4444"
i = 0
for i in a:
    if i == "111":
        print("xxx")
        break
i = "False"
print(str(i.find("Fal")))
print(str(i))
print(type(i) == str)