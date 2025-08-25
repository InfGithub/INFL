import math

def get_Greatest_Common_Divisor(a: int, b: int) -> int:
    """最大公约数"""
    if a < b:
        a, b = b, a

    def comp(a, b):
            
        if b==0:
            r: int = a

        if b!=0:
            r: int = a % b
            
        if r == 0:
            return b
            
        if r != 0:
            a = b
            b = r
            return comp(a, b)
        
    return int(comp(a, b))

def get_Least_Common_Multiple(a: int, b: int) -> int:

    """最小公倍数"""

    return int(a * b / get_Greatest_Common_Divisor(a, b))

def get_Prime_is(n: int) -> bool:

    """判定素数"""

    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    index: int = 3
    n_sqrt: int = math.ceil(math.sqrt(n))
    while index * index <= n_sqrt:
        if n % index == 0:
            return  False
        index+=2
    return True

def multiplyList(List: list[int]):

    """求列表的乘积"""

    result = 1
    for x in List:
        result = result * x
    return result

def two_points_get_function(A: tuple[float, float], B: tuple[float, float]) -> tuple[float, float]:
    K = (B[1] - A[1]) / (B[0] - A[0])
    return K, A[1] - K * A[0]

def find_intersection(A: tuple[float, float], B: tuple[float, float]) -> tuple[float, float]:
    x = (A[1] - B[1]) / (B[0] - A[0])
    y = A[0] * x + A[1]
    return x, y

def points_get_pos(A: tuple[float, float],
                   B: tuple[float, float],
                   C: tuple[float, float],
                   D: tuple[float, float]) -> tuple[float, float]:
    F0: tuple[float, float] = two_points_get_function(A, B)
    F1: tuple[float, float] = two_points_get_function(C, D)
    return find_intersection(F0, F1)

if __name__ == "__main__":
    pass