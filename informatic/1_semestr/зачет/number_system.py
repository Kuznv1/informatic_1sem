def conver_to(num, base):
    digits = list('0123456789abcdefghijklmnopqrstuvwxyz')
    if base > len(digits):
        return None
    result = str()
    while num > 0:
        result = digits[num % base] + result 
        num //= base
    return result