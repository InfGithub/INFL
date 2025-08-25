from math import ceil, sqrt

def greatest_common_divisor(a: int, b: int) -> int:
    """
    计算两个整数的最大公约数(GCD)。

    Args:
        a (int): 第一个正整数。
        b (int): 第二个正整数。

    Returns:
        int: 两个正整数的最大公约数。

    Example:
        >>> greatest_common_divisor(36, 48)
        12
    """

    while b != 0:
        a, b = b, a % b
    return abs(a)

def get_Least_Common_Multiple(a: int, b: int) -> int:
    """
    计算两个正整数的最小公倍数(LCM)。

    Args:
        a (int): 第一个正整数。
        b (int): 第二个正整数。

    Returns:
        int: 两个正整数的最小公倍数。

    Example:
        >>> get_Least_Common_Multiple(36, 48)
        144
    """

    return int(a * b / greatest_common_divisor(a, b))

def is_prime(n: int) -> bool:
    """
    判断一个正整数是否为素数。

    Args:
        n (int): 即要判断的正整数。
    
    Returns:
        bool: 如果是素数则返回True，否则返回False。

    Example:
        >>> is_prime(7)
        True
    """

    if n == 2:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    index: int = 3
    n_sqrt: int = ceil(sqrt(n))
    while index <= n_sqrt:
        if n % index == 0:
            return  False
        index+=2
    return True

def multiplyList(List: list[float]) -> float:
    """
    计算一个浮点数列表中所有元素的乘积。

    Args:
        List (list[float]): 浮点数列表。
    
    Returns:
        float: 浮点数列表中所有元素的乘积。

    Example:
        >>> multiplyList([1.5, 2.0, 3.5])
        9.0
    """

    result = 1.0
    for x in List:
        result = result * x
    return result

def two_points_get_function(A: tuple[float, float], B: tuple[float, float]) -> tuple[float, float]:
    """
    通过两个点确定直线方程 y = kx + b

    根据两点式直线方程计算斜率和截距

    Args:
        A (tuple[float, float]): 第一个点的坐标 (x, y)。
        B (tuple[float, float]): 第二个点的坐标 (x, y)。
    
    Returns:
        tuple[float, float]: 直线方程的斜率 k 和截距 b。
    
    Raises:
        ZeroDivisionError: 当两点x坐标相同（垂直线）时引发。

    Example:
        >>> two_points_get_function((1, 2), (3, 4))
        (1.0, 1.0)

    """

    K = (B[1] - A[1]) / (B[0] - A[0])
    return K, A[1] - K * A[0]

def find_intersection(A: tuple[float, float], B: tuple[float, float]) -> tuple[float, float]:
    """
    求两条直线的交点
    
    通过解两条直线的方程组求得交点坐标
    
    Args:
        line_a: 第一条直线的斜率和截距 (k, b)
        line_b: 第二条直线的斜率和截距 (k, b)
        
    Returns:
        交点坐标 (x, y)
        
    Raises:
        ZeroDivisionError: 当两条直线平行（斜率相同）时引发
        
    Examples:
        >>> find_intersection((1, 0), (-1, 2))
        (1.0, 1.0)
    """

    x = (A[1] - B[1]) / (B[0] - A[0])
    y = A[0] * x + A[1]
    return x, y

def points_get_pos(A: tuple[float, float],
                   B: tuple[float, float],
                   C: tuple[float, float],
                   D: tuple[float, float]) -> tuple[float, float]:
    """
    通过四点确定两条直线并求其交点
    
    先通过两点确定两条直线，再求这两条直线的交点
    
    Args:
        point_a: 第一条直线上的第一个点
        point_b: 第一条直线上的第二个点
        point_c: 第二条直线上的第一个点
        point_d: 第二条直线上的第二个点
        
    Returns:
        两条直线的交点坐标 (x, y)
        
    Examples:
        >>> get_intersection_from_points((0, 0), (1, 1), (0, 1), (1, 0))
        (0.5, 0.5)
    """

    F0: tuple[float, float] = two_points_get_function(A, B)
    F1: tuple[float, float] = two_points_get_function(C, D)
    return find_intersection(F0, F1)

if __name__ == "__main__":
    pass