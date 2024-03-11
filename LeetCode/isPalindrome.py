def isPalindrome(x):
    if x < 0:
        return False

    num_list = []
    while x > 0:
        digit = x % 10
        x //= 10
        num_list.insert(0, digit)

    left_p = 0
    right_p = len(num_list) - 1
    while left_p < right_p:
        if num_list[left_p] != num_list[right_p]:
            return False
        left_p += 1
        right_p -= 1
    return True

def isPalindrome_StrImp(x):
    if (x < 0 or x != 0 and x % 10 == 0):
        return False
    temp = str(x)
    return temp == temp[::-1]

x = -121

print(isPalindrome(x))
print(isPalindrome_StrImp(x))