from InfixToPostfix import *  # convToRPNExp 함수의 호출을 위해셔
from PostCalculator import *  # EvalRPNExp 함수의 호출을 위해서


def evalInfixExp(exp):
    expcpy = exp  # exp를 expcpy에 복사

    expcpy = convToRPNExp(expcpy)  # 후위 표기법의 수식으로 변환
    ret = EvalRPNExp(expcpy)  # 변환된 수식의 계산

    del expcpy  # 문자열 저장공간 해제
    return ret  # 계산결과 반환


def InfixCalculatorMain():
    exp1 = "1+2*3"
    exp2 = "(1+2)*3"
    exp3 = "((1-2)+3)*(5-2)"

    print(f"{exp1} = {evalInfixExp(exp1)}")
    print(f"{exp2} = {evalInfixExp(exp2)}")
    print(f"{exp3} = {evalInfixExp(exp3)}")


if __name__ == "__main__":
    InfixCalculatorMain()
