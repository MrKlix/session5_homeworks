import math
import operator

class Calculator:
    def __init__(self, zahl1, zahl2=None):
        self.zahl1 = zahl1
        self.zahl2 = zahl2

    def get_CalcResult(self, myOperator):
        opsCalc = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,
            "potenz": operator.pow
        }

        opsAdv = {"log": math.log, "wurzel": math.sqrt}

        if myOperator in opsAdv:
            op_funcAdv = opsAdv[myOperator]
            return op_funcAdv(self.zahl1)
        elif myOperator in opsCalc:
            op_funcCalc = opsCalc[myOperator]
            return op_funcCalc(self.zahl1, self.zahl2)
        else:
            return self.zahl1 * self.zahl1
