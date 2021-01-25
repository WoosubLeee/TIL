def dec_to_bin(n):
    result = []
    # base return 값
    if n < 2:
        return str(n)
    else:
        # n을 2로 나눈 몫에 대해 재귀 적용
        result += dec_to_bin(n // 2)
        result += str(n % 2)
    return ''.join(result)


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    print(dec_to_bin(10))
    # => '1010'
    print(dec_to_bin(5))
    # => '101'
    print(dec_to_bin(50))
    # => '110010'