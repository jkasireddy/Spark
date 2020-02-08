# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    """

    :param S:
    :return:
    """
    # get the length of the string
    l =len(S)
    # instantiating the Answer
    ans =""
    for n in range(l):
        print n
        # iterate over the string
        if S[n]> S[n+1]:
            for m in range(l):
                if (n!=m):
                    ans +=S[m]
                    print ans

            return ans
        # else:

    #  now leave the last charact
    ans=S[0:l-1]
    print ans
    return ans

    # write your code in Python 3.6
    # b=list(S)
    # print(b)
    # b.sort()
    # print(b)
    # pass


if __name__ == '__main__':
    solution("codility")
