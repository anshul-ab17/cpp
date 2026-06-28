def countBinaryPalindromicNumbers(low: int, high: int) -> int:
    def is_binary_palindrome(n: int) -> bool:
        s = bin(n)[2:]
        return s == s[::-1]
    
    # For large ranges, generate palindromes directly instead of checking each number
    count = 0
    # Standard check approach for smaller bounds:
    for num in range(low, high + 1):
        if is_binary_palindrome(num):
            count += 1
    return count
