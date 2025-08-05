
import math
from typing import List, Tuple
    
def abin(number: int, digits: int = None) -> str:
    if digits == None:  return bin(number)[2:]
    else:  return bin(number)[2:].zfill(digits)

def ahex(number: int, digits: int = None) -> str:
    if digits == None:  return hex(number)[2:]
    else:  return hex(number)[2:].zfill(digits)

def adec(number: str, base: int):
    return int(number, base)

def get_Greatest_Common_Divisor(a: int, b: int) -> int:
    """GCD"""
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

    """LCM"""

    return int(a * b / get_Greatest_Common_Divisor(a, b))

def get_Prime_is(n: int) -> bool:

    """Prime"""

    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    index: int = 3
    n_sqrt: int = math.ceil(math.sqrt(n))
    while index*index <= n_sqrt:
        if n%index == 0:
            return  False
        index+=2
    return True

def multiplyList(List):

    result = 1
    for x in List:
        result = result * x
    return result

class frac():
    ...

class frac():

    """分数系统"""

    def __init__(self, nume: int, deno: int):

        self.nume: int = nume
        self.deno: int = deno

    def __str__(self):
        return f"frac: {self.nume}/{self.deno}"

    def reduce(self) -> frac:

        Gcd: int = get_Greatest_Common_Divisor(self.nume, self.deno)
        nume = int(self.nume / Gcd)
        deno = int(self.deno / Gcd)
        return frac(nume, deno)

    def __add__(self, other) -> frac:

        if other == 0:
            return self

        if type(other) != frac:
            raise TypeError(f"cannot frac and {type(other)}")

        if self.deno == other.deno:
            return frac(self.nume + other.deno, self.nume)
        
        if self.deno != other.deno:
            
            Lcm = get_Least_Common_Multiple(self.deno, other.deno)
            a = int(Lcm / self.deno)
            b = int(Lcm / other.deno)
            return frac(self.nume*a + other.nume*b, self.deno*a)

    def __mul__(self, other) -> frac:

        return frac(self.nume*other.nume, self.deno*other.deno)

    def to_float(self) -> float:
        return self.nume / self.deno

def find_third_point(A: Tuple[float, float], d1: float, 
                    B: Tuple[float, float], d2: float, 
                    tol: float = 1e-10) -> List[Tuple[float, float]]:
    """
    求解平面坐标系中两点距离求第三点坐标问题
    
    参数:
        A: 第一个点坐标 (x1, y1)
        d1: 到第一个点的距离
        B: 第二个点坐标 (x2, y2)
        d2: 到第二个点的距离
        tol: 数值计算容差 (默认1e-10)
    
    返回:
        交点坐标列表 (可能包含0, 1, 2个解)
    """
    x1, y1 = A
    x2, y2 = B
    
    # 计算线性方程系数
    a: float = 2 * (x2 - x1)
    b: float = 2 * (y2 - y1)
    c: float = d1**2 - d2**2 + x2**2 - x1**2 + y2**2 - y1**2
    
    solutions: List[Tuple[float, float]] = []
    
    # 处理两点重合的情况
    if abs(a) < tol and abs(b) < tol:
        if abs(d1 - d2) < tol:
            print("两点重合且距离相等：无穷多解")
        else:
            print("两点重合但距离不等：无解")
        return solutions
    
    # 处理一般情况 (b ≠ 0)
    if abs(b) > tol:
        # 二次方程系数
        A_coeff: float = a**2 + b**2
        B_coeff: float = -2*b**2*x1 - 2*a*(c - b*y1)
        C_coeff: float = b**2*x1**2 + (c - b*y1)**2 - d1**2*b**2
        
        # 计算判别式
        D: float = B_coeff**2 - 4*A_coeff*C_coeff
        
        # 处理实数解
        if D < -tol:
            pass  # 无实数解
        elif abs(D) < tol:
            # 一个解
            x_val: float = -B_coeff / (2*A_coeff)
            y_val: float = (c - a*x_val) / b
            solutions.append((x_val, y_val))
        else:
            # 两个解
            sqrtD: float = math.sqrt(D)
            x1_val: float = (-B_coeff + sqrtD) / (2*A_coeff)
            y1_val: float = (c - a*x1_val) / b
            solutions.append((x1_val, y1_val))
            
            x2_val: float = (-B_coeff - sqrtD) / (2*A_coeff)
            y2_val: float = (c - a*x2_val) / b
            solutions.append((x2_val, y2_val))
    
    # 处理垂直线情况 (b = 0, a ≠ 0)
    else:
        x_val: float = c / a
        # 计算y值
        t: float = d1**2 - (x_val - x1)**2
        
        if t < -tol:
            pass  # 无实数解
        elif abs(t) < tol:
            # 一个解
            solutions.append((x_val, y1))
        else:
            # 两个解
            sqrt_t: float = math.sqrt(t)
            solutions.append((x_val, y1 + sqrt_t))
            solutions.append((x_val, y1 - sqrt_t))
    
    return solutions