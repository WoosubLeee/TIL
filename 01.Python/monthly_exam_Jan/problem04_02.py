def caesar(word, n):
    word_list = []
    for i in word:
        # ASCII 숫자를 활용하여 대소문자 구분
        if ord(i) <= 90:
            # n만큼 증가시켰을 때 대소문자 범위를 벗어나지 않는지 확인
            if ord(i) + n > 90:
                # 벗어난다면 n만큼 더하고 26만큼 감소시켜 글자 변환
                word_list += chr(ord(i)+n-26)
            else:
                # 벗어나지 않는다면 n만큼만 더하여 글자 변환
                word_list += chr(ord(i)+n)
        else:
            # 위와 동일
            if ord(i) + n > 122:
                word_list += chr(ord(i)+n-26)
            else:
                word_list += chr(ord(i)+n)
    return ''.join(word_list)


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    print(caesar('apple', 5))
    # => 'fuuqj'
    print(caesar('ssafy', 1))
    # => 'ttbgz'
    print(caesar('Python', 10))
    # => 'Zidryx'