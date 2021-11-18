########## Angkan Baidya ##########
########## abaidya ##############
########## 112309655 #############
import re
import os
def rename(path):
  if os.path.isdir(path) == False:
      return(path + " "+ "does not exist!")
  numbers = []
  pattern = "^snap(\d{3}).txt"
  fakefiles = os.listdir(path)
  if len(fakefiles) == 0:
      return ("Directory is empty")
  for i in fakefiles:
   if os.path.isdir(path+"/"+i):
       fakefiles.remove(i)
 
  for files in fakefiles:
      test = re.search(pattern,files)
      if test:
          numbers.append(test.group(1))
  if len(numbers) == 0:
      return 
  numberstonumbers=  [int(x) for x in numbers]
  numberstonumbers.sort()
  numbertocompare = numberstonumbers[0]
  if numbertocompare > 999:
      return 
  i = 0
  while i < len(numberstonumbers):
      if (numberstonumbers[i]>999):
          del numberstonumbers[i]
      else:
          i+= 1
  snapinsertlow = "snap"
  snapending = ".txt"
  snaplownumber = "00"
  snapmidnumber = "0"
  finalist = []
  lengthtocompare = len(numberstonumbers)
  print(numberstonumbers)
  for x in range(lengthtocompare):
      if (numbertocompare < 10):
          finalnumber = str(numbertocompare)
          fullycombined = snapinsertlow+snaplownumber+finalnumber+snapending
          finalist.append(fullycombined)
      if (numbertocompare < 100) and (numbertocompare > 9):
          finalnumber = str(numbertocompare)
          fullycombined = snapinsertlow+snapmidnumber+finalnumber+snapending
          finalist.append(fullycombined)
      if (numbertocompare>99):
          finalnumber = str(numbertocompare)
          fullycombined = snapinsertlow+finalnumber+snapending
          finalist.append(fullycombined)
      numbertocompare=numbertocompare +1
  counter = 0
  print(fakefiles)
  print(finalist)
  for files in fakefiles:
      test = re.search(pattern,files)
      if test:
          for i in range(len(finalist)):
              if files not in finalist and (os.path.isfile(path+"/"+finalist[i]) == False):
                  if (os.path.isdir(path+"/"+finalist[i]) == True):
                    raise ValueError("Path already exists")
                  os.rename(os.path.join(path,files),
                  os.path.join(path,finalist[i]))
                  break
              i = i+ 1
 
  fakefilestwo = os.listdir(path)
  print(fakefilestwo)