
li=[]

total_marks=100

for i in range(5):
    name=input("Enter student's name : ")
    print("Enter grade out of in mditerm ",total_marks,": ",end=' ')
    midterm=float(input())
    print("Enter grade out of in project",total_marks,": ",end=' ')
    project=float(input())
    print("Enter grade out of in final ",total_marks,": ",end=' ')
    final=float(input()) 
    li.append({'name':name,'grade':((midterm*0.3)+(project*0.3)+(final*0.4))})
li.sort(key=lambda a:(-a['grade']))
for i in li:
    print(i['name'],": ",i['grade'])