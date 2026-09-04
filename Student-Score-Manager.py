students={}
scores=[]
sum_scores=0
pass_count=0
fail_count=0
above_average={}
while True:
       try:
           number=int(input('please enter number of students:\n')) 
       except ValueError:
              print('invalid number of students')
              print('----------------------------')
              continue
       if number<1 or number>30:
                               print('you must choose a integer of [1,30]')
                               print('----------------------------------')
                               continue
       break          


for _ in range(number):
    while True:
          student=input('please enter name & score:\n')
          print('----------------------------------')
          student=student.strip()
          if ' ' not in student:
                  print('invalid student name & score')
                  continue
           name , score=student.rsplit(' ',1)
          name_student=all(char.isalpha() or char=='_' 
                           or char==' ' for char in name)
          score_student=all(char.isdigit() for char in score)
          if name_student and score_student:
             score=int(score)
             if 20>=score>=0:
                 print('valid student name & score')
                 print('----------------------------------')
                 if  name in students:
                     print('The name is repetitive')
                     continue
                 else:
                      students[name]=score
                      sum_scores+=score
                      scores.append(score)
                 break
             else:
                  print('you must choose a integer of [0,20]')
                  print('----------------------------------')
                  continue
          else:
               print('invalid student name & score')
               print('----------------------------------')
               continue   
average=sum_scores/number
for score in scores:
    if score>=10:
        pass_count+=1
    else:
        fail_count+=1
maximum=scores[0]
minimum=scores[0]
max_name=name
min_name=name
for name , score in students.items():
    if score>maximum:
       maximum=score
       max_name=name
    if score<minimum:
       minimum=score
       min_name=name
for name , score in students.items():
    if score> average:
        above_average[name]=score
print('________________________________________')
print('students information dictionary=',students)
print('________________________________________')
print('sum scores=',sum_scores)
print('________________________________________')
print('average scores=',average)
print('________________________________________')
print('maximum scores=',maximum)
print('________________________________________')
print('minimum scores=',minimum)
print('________________________________________')
print('pass count=',pass_count)
print('________________________________________')
print('fail count =',fail_count)
print('________________________________________')
print('pass count + fail count=',pass_count + fail_count)
print('________________________________________')
print('max_name & maximum =',[max_name,maximum])
print('________________________________________')
print('min_name & minimum =',[min_name,minimum])
print('________________________________________')
print('above average =',above_average)
print('________________________________________')
if    average>=17:
      print('class is very good')
elif  17>average>=14:
      print('class is good')
elif  14>average>=10:
      print('class is mediocrity')
else:
     print('class is feeble')















              
