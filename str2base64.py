import sys

def str2ASCII(s):
    result = []
    for letter in s:
        result.append(ord(letter))
    return result

def ASCII2bin(asc): # a will be  a list made by str2ASCII
    bin_result = ""
    for element in range(0,len(asc)):
        bin_result += '0' + bin(asc[element])[2:]
    if len(bin_result) % 6 != 0:
        block = 6 - len(bin_result) % 6
        bin_result += '0' * block + '=' * (block // 2) 
    return bin_result

def bin2base64(b):
    table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    sign_lst = []
    result = ''
    i = len(b) // 6  # no float, class int
    start = 0
    for _ in range(0,i):
        a = int(b[start:start+6], 2)
        sign_lst.append(a)
        start += 6
    for sign in sign_lst:
        result += table[sign]
    result += b[-1]
    return result


print(str2ASCII('Hello'))
print(ASCII2bin(str2ASCII('Hello')))
print(bin2base64(ASCII2bin(str2ASCII('Hello'))))
