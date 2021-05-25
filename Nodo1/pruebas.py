import sys
print(sys.path)
sys.path.append("..")
from operaciones import Operaciones

obj = Operaciones()

obj.saveNum(1)
obj.saveNum(1)
obj.saveNum(1)
obj.saveNum(1)
obj.saveNum(1)

obj.saveNum(2)
obj.saveNum(3)
obj.saveNum(3)
obj.sumNums()

    