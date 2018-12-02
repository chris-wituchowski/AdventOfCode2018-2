import time

inputStr = """abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz"""

startTime = time.time()

inputList = list(map(str, inputStr.splitlines()))

for string in inputList:
