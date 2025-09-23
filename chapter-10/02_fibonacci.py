def fib(n):
    """
    Calculate the Fibonacci's series value for integer n
    
    Parameters:
    - n: The number to use in the Fibonacci's series.
    
    Returns: The calculated value of the Fibonacci's series for n
    """

    loop = n    
    last = 0
    current = 1
    
    while loop >= 0:
        last, current = current, last + current
        loop -= 1
        
    return last
        
        