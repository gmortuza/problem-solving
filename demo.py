# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    if len(S) <=2
        return S
    S = list(S)

    rem = False
    if len(S) % 2 == 0:
        rem = True
        S.insert(len(S)//2, "X")
    middle = len(S)//2
    for i in range(1, len(S)//2 + 1):
        if S[middle + i] == S[middle - i] and not S[middle + i] == '?':
            pass
        elif S[middle + i] == S[middle - i] == '?':
            S[middle + i] = S[middle - i] = 'a'
        elif S[middle + i] == '?':
            S[middle + i] = S[middle - i]
        elif S[middle - i] == '?':
            S[middle - i] = S[middle + i]
        else:
            return "NO"
    if rem:
        del(S[middle])
    return "".join(i for i in S)

N = "a?b?a"
print(solution(N))