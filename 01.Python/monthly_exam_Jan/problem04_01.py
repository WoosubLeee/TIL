def swap(word):
    word_list = []
    # for문을 활용하여 각 글자에 접근
    for i in word:
        # if문과 ASCII 숫자를 사용하여 대소문자 구분
        if ord(i) <= 90:
            # ASCII 숫자에 32를 더하여 소문자로 변환
            word_list += chr(ord(i)+32)
        else:
            # ASCII 숫자에 32를 빼 대문자로 변환
            word_list += chr(ord(i)-32)
    # list를 string으로 병합
    return ''.join(word_list)
            


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    print(swap('aPpLe'))
    # => 'ApPlE'
    print(swap('SSAFY'))
    # => 'ssafy'
    print(swap('Python'))
    # => 'pYTHON'