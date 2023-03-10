import random
registers = {"R0":0,"R1":0,"R2":2,"R3":4,"R4":0,"R5":0,"R6":0,"R7":0,"R8":0,"R9":0,"R10":0,"R11":0,"R12":0,"PC":0}
fileName = input("Enter filename including the format: \n")
f = open(fileName,"r")
fileArr = f.readlines()
mainMem = [random.randint(1,30) for i in range(1000)]
def ADD(R1,R2,R3):
  registers[R1] = registers[R2] + registers [R3]
  registers["PC"] +=1
nFileArray = []
CMP  = False
for line in fileArr:
  newLine = line.strip() 
  nFileArray.append(newLine)  
print(nFileArray)
for i in range(len(nFileArray)):
  statement = nFileArray[i]
  function_name, param_string = statement.split(" ", 1)
  params = [p.strip() for p in param_string.split(",")]
  if CMP == False:
    if nFileArray[i][0:3] == "ADD":
      ADD(params[0],params[1],params[2])
print(registers) 