def solution(S):
    l= len(S)
    print l
    b = list(S)
    print b
    b.sort()
    print b
    ans=""
    for n in range(l):
        for m in range(l):
            if (n != m):
                ans += S[m]
                print ans






if __name__ == '__main__':
    solution("hot")