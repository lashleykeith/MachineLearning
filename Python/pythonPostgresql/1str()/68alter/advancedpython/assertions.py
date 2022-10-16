'''
def divide_secure(number, divisor):
    if divisor == 0:
        raise ValueError("This is divisor is 0!")
    return number/divisor
'''

def divide_secure(number, divisor):
    assert divisor != 0, "Divided a number by zero!"
    return number / divisor

print(divide_secure(10,0))
