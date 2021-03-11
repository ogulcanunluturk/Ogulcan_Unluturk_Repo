# 5 dictionary
dictionary1 = {'name': 'Ogulcan Unluturk', 'qualification': 'Btech', 'experience': 'fresher'} 
dictionary2 = {'name': 'Deniz Kaya', 'qualification': 'MTech', 'experience': 'tutor'} 
dictionary3 = {'name': 'Omer Cengiz', 'qualification': 'BE', 'experience': 'expert'} 
dictionary4 = {'name': 'Ahmet Solak', 'qualification': 'ME', 'experience': 'professional'} 
dictionary5 = {'name': 'Merve Kaynak', 'qualification': 'PG', 'experience': 'fresher'} 

listOfdict = [dictionary1, dictionary2, dictionary3, dictionary4, dictionary5]

try:
 cv_file = open('cv', 'wt')
 for x in listOfdict:
     
     # write contents to cv file
     for key, value in x.items():
         cv_file.write('{} {}\n'.format(key, ''.join(value)))
     # new line for next cv
     cv_file.write('\n')
 # save file
 cv_file.close() 
  
except: 
    print("Error")

# print information on screen
f = open("cv", "r")
print(f.read())