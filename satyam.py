import requests
import json
import os
from os import path
exist=path.exists("courses.json")
if exist:
    with open("courses.json","r+") as f:
        var=json.load(f)
        # print (var)
else:
    r=requests.get("http://saral.navgurukul.org/api/courses")
    # print (r.text)
    with open("courses.json","w") as f:
        f.write(r.text)
    with open("courses.json","r+") as f:
        var=json.load(f)


j=0
available_courses=var["availableCourses"]
for i in available_courses:
    name=i["name"]
    print (j,name)
    j+=1


user=int(input("Enter your course-index"))
# a=0
# for i in available_courses:
#     if user==a:
#         print (i["name"])
#     a+=1


id=var["availableCourses"][user]["id"]
id=str(id)
print (id)
a=requests.get("http://saral.navgurukul.org/api/courses/"+id+"/exercises").text
b=json.loads(a)
print (b)

# for i in b["data"]:
#     slug=i["slug"]
#     childExercise=i["childExercises"]
#     print (slug)
#     print ("                      ",childExercise)



files=path.exists("exercises"+id+".json")
if files:
    with open("exercises"+id+".json","r+") as f:
        var=json.load(f)
        data=var["data"]
        for i in data:
            slug=i["slug"]
            childExercise=i["childExercises"]
            print (slug)
            print ("                      ",childExercise)
else:
    a=requests.get("http://saral.navgurukul.org/api/courses/"+id+"/exercises")
    ExerciseName=a.text
    # print (type(var))
    # data=var["data"]
    with open("exercises"+id+".json","w") as f:
        f.write(ExerciseName)
    with open("exercises"+id+".json","r") as f:
        var=json.laod(f)
        data=var["data"]
    for i in data:
        slug=i["slug"]
        childExercise=i["childExercises"]
        print (slug)
        print ("                      ",childExercise)