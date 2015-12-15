import input_day01

inputData = input_day01.getInput()

floorNumber = 0
firstBasement = -1

for index, char in zip(xrange(len(inputData)), inputData):
    if char == '(':
        floorNumber += 1
    elif char == ')':
        floorNumber -= 1
        if(floorNumber == -1 and firstBasement == -1):
            firstBasement = index + 1

print 'floorNumber: ', floorNumber
print 'firstBasement: ', firstBasement
