import time
import math
import sys

try:
    uniCharacter = str(sys.argv[1]) if len(sys.argv) > 1 and len(sys.argv[1]) >= 1 else "*"
    timeSleep = (int(sys.argv[2]) if len(sys.argv) > 2 else 1500) / 100000
except:
    print("Please provide the parameters as follows:")
    print(f"python3 {sys.argv[0]} [CHARACTER] [MILLISECONDS]")
    sys.exit()

starCount = 0
starMax = 30

wholeLoopCount = 0
wholeLoopMax = 5


while wholeLoopCount < wholeLoopMax:
    while starCount < starMax:
        if starCount == 0 and wholeLoopCount != 0:
            print(" " * len(uniCharacter) * math.floor(starMax - starCount) + uniCharacter)
        else:
            time.sleep(timeSleep)
            print(" " * len(uniCharacter) * math.floor(starMax - starCount) + uniCharacter * (starCount + 1) + uniCharacter * starCount)
        starCount += 1

    while starCount > 0:
        time.sleep(timeSleep)
        print(" " * len(uniCharacter) * math.floor(starMax - starCount) + uniCharacter * (starCount + 1) + uniCharacter * starCount)
        starCount -= 1
        if starCount == 0 and wholeLoopCount == (wholeLoopMax - 1):
            print(" " * len(uniCharacter) * math.floor(starMax - starCount) + uniCharacter)
    
    wholeLoopCount += 1
    time.sleep(timeSleep)