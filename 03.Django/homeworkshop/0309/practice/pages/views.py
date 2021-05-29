import random
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render

# Create your views here.
def lotto(request):
    response = requests.get('https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=953').json()
    result = []
    for i in range(1, 7):  # 당첨번호를 result 리스트에 기록
        result.append(response[f'drwtNo{i}'])
    bonus = response['bnusNo']  # 보너스번호를 기록

    count = {'1등': 0, '2등': 0, '3등': 0, '4등': 0, '5등': 0, '꽝': 0}  # 1000회 반복의 결과를 저장할 딕셔너리 생성
    for i in range(1000):
        nums = random.sample(range(1, 46), 6)

        match = 0
        has_bonus = False
        for j in nums:  # 랜덤으로 생성한 6개의 번호에 대해
            if j in result:  # 당첨번호에 있다면
                match += 1
            elif j == bonus:  # 보너스번호라면
                has_bonus = True

        # 맞춘 개수에 따라 count 추가
        if match == 6:
            count['1등'] += 1
        elif match == 5:
            if has_bonus:
                count['2등'] += 1
            else:
                count['3등'] += 1
        elif match == 4:
            if has_bonus:
                count['4등'] += 1
            else:
                count['5등'] += 1
        else:
            count['꽝'] += 1

    PRIZE_URL = 'https://dhlottery.co.kr/gameResult.do?method=byWin'
    b_soup = BeautifulSoup(requests.get(PRIZE_URL).text, 'html.parser')
    total_prize = 0
    for i in range(1, 6):
        prize = b_soup.select(f'#article > div:nth-child(2) > div > table > tbody > tr:nth-child({i}) > td:nth-child(4)')
        prize = int(prize[0].text[:-1].replace(',', ''))
        total_prize += count[f'{i}등']*prize
    avg_prize = total_prize / 1000

    context = {
        'result': result,
        'bonus': bonus,
        'count': count,
        'avg_prize': f'{avg_prize:.0f}',
        'yield': f'{((avg_prize/1000)*100-100):.1f}%',
    }
    return render(request, 'pages/lotto.html', context)