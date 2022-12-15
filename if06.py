def main(a,b,c):
    """
    Find how many positive and how many negative numbers there are in the given numbers.
    check the following conditions:
    "there are a lot of positive numbers",
    "there are a lot of negative numbers"

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        string: string with the result
    """
    count=0
    if a>0:
        count+=1
    if b>0:
        count+=1
    if c>0:
        count+=1
    
    if count>3-count:
        return "there are a lot of positive numbers"
    else:
        return "there are a lot of negative numbers"