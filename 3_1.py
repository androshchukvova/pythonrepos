def is_palindrome(seq):
    return seq == seq[::-1]

words = input('Vvedit stroku: ').split()
print("TRUE" if is_palindrome(words) else "FALSE")