#김밥 2500, 참치김밥 3500, 돈까스김밥 3500, 고추참치김밥 3500, 소고기김밥 4500, 치즈김밥 3000, 셀러드김밥 2500, 꼬마김밥 1200, 충무김밥 20000, 꽈리김밥 3500 ,진미김밥 2700
#라면 4000, 치즈라면 4500, 된장라면 4700, 떡라면 4800, 만두라면 4500, 떡만두라면 5000, 카레라면 4500, 해물라면 5500, 짜장라면 4200, 비빔라면 4200
#돈가스 8000, 치즈돈가스 9000, 고치돈 10000, 등심돈가스 7500, 안심돈가스 7500, 피카츄돈가스 500, 새우돈가스 7500, 대왕돈가스 12000, 치킨돈가스 6000, 함박스테이크 9500
#제육덮밥 7000, 오무라이스 7000, 하이라이스 7000, 오징어덮밥 7500, 짜장덮밥 6500, 소고기덮밥 8000, 카레덮밥 6500, 돌솥비빔밥 7000, 김치덮밥 6500
#김치찌개 6500, 된장찌개 6500, 순두부찌개 6500, 내장찌개 6500, 해물된장찌개 8500, 부대찌개 7800
#떡볶이 3000, 치즈떡볶이 4500, 라볶이 5000, 마약떡볶이 99900, 컵떡볶이 500
#우동 3000, 튀김우동 4500, 김치우동 4500, 유부우동 4500
#육개장 6000, 알탕 7500, 갈비탕 8000, 황태해장국 7000, 순대국밥 5500, 명태국밥 7000, 공기밥 1000

# Menu = [{"kimbap":2500, "chamkim": 3500, "donkim": 4500, "gochamkim":3500, "sogokim":4500, "cheekim": 3000, "salkim":2500, "kkokim":1500, "chungkim":20000, "kkarikim":3500, "jinkim":2700 },
#         {"ramen": 4000, "cheera": 4500, "doinra":4700, "ddokra":4800, "manra":4500, "ddokmanra":5000, "curryra":4500, "haera":5500, "jjara":4200, "bira": 4200},
#         {"don":8000, "cheedon":9000, "gocheedon":10000, "deungdon":7500, "andon":7500, "pidon":500, "saedon":7500, "daedon":12000, "chidon":6000, "hambak":9500},
#         {"jeyuk":7000, "omura":7000, "hira":7000, "odup": 7500, "jjadup":6500, "sogodup":8000, "currydup":6500, "dolsot": 7000, "kimdup":6500},
#         {"kimjji":6500, "doinjji":6500, "soonjji":6500, "naejji":6500, "haejji":8500, "bujji":7800},
#         {"ddukbok":3000, "cheedduk":4500, "rabbok":5000, "madduk":99900, "cupdduk":500},
#         {"woodong":3000, "tuiwoo":4500, "kimwoo":4500, "yoowoo":4500},
#         {"yookgae":6000, "altang":7500, "galbi":8000, "hwangtae":7000, "sundae":5500, "myungtae":7000, "gongki":1000}]

# kimbaphan = {"김밥", "참치김밥", "돈까스김밥", "고추참치김밥", "소고기김밥", "치즈김밥", "셀러드김밥", "꼬마김밥", "충무김밥", "꽈리김밥", "진미김밥"}
# kimbapru = {"kimbap":2500, "chamkim": 3500, "donkim": 4500, "gochamkim":3500, "sogokim":4500, "cheekim": 3000, "salkim":2500, "kkokim":1500, "chungkim":20000, "kkarikim":3500, "jinkim":2700}
# ramenru = {"ramen": 4000, "cheera": 4500, "doinra":4700, "ddokra":4800, "manra":4500, "ddokmanra":5000, "curryra":4500, "haera":5500, "jjara":4200, "bira": 4200}
# donggasru = {"don":8000, "cheedon":9000, "gocheedon":10000, "deungdon":7500, "andon":7500, "pidon":500, "saedon":7500, "daedon":12000, "chidon":6000, "hambak":9500}
# dupbapru = {"jeyuk":7000, "omura":7000, "hira":7000, "odup": 7500, "jjadup":6500, "sogodup":8000, "currydup":6500, "dolsot": 7000, "kimdup":6500},
# jjigaeru = {"kimjji":6500, "doinjji":6500, "soonjji":6500, "naejji":6500, "haejji":8500, "bujji":7800}
# dduckbokru = {"ddukbok":3000, "cheedduk":4500, "rabbok":5000, "madduk":99900, "cupdduk":500}
# woodongru = {"woodong":3000, "tuiwoo":4500, "kimwoo":4500, "yoowoo":4500}
# tangru = {"yookgae": 6000, "altang": 7500, "galbi": 8000, "hwangtae": 7000, "sundae": 5500, "myungtae": 7000, "gongki": 1000}

menu = {"김밥":2500, "참치김밥":3500, "돈가스김밥":3500, "고추참치김밥":3500, "소고기김밥":4500, "치즈김밥":3000, "셀러드김밥":2500, "꼬마김밥":1200, "충무김밥":20000, "꽈리김밥":3500, "진미김밥":2700,
        "라면":4000, "치즈라면":4500, "된장라면":4700, "떡라면":4800, "만두라면":4500, "떡만두라면":5000, "카레라면":4500, "해물라면":5500, "짜장라면":4200, "비빔라면":4200,
        "돈가스":8000, "치즈돈가스":9000, "고치돈":10000, "등심돈가스":7500, "안심돈가스":7500, "피카츄돈가스":500, "새우돈가스":7500, "대왕돈가스":12000, "치킨돈가스":6000, "함박스테이크":9500,
        "제육덮밥":7000, "오무라이스":7000, "하이라이스":7000, "오징어덮밥":7500, "짜장덮밥":6500, "소고기덮밥":8000, "카레덮밥":6500, "돌솥비빔밥":7000, "김치덮밥":6500,
        "김치찌개":6500, "된장찌개":6500, "순두부찌개":6500, "내장찌개":6500, "해물된장찌개":8500, "부대찌개":7800,
        "떡볶이":3000, "치즈떡볶이":4500, "라볶이":5000, "마약떡볶이":99900, "컵떡볶이":500,
        "우동":3000, "튀김우동":4500, "김치우동":4500, "유부우동":4500,
        "육개장":6000, "알탕":7500, "갈비탕":8000, "황태해장국":7000, "순대국밥":5500, "명태국밥":7000, "공기밥":1000}

order = []  # 장바구니
order_sum = 0 # 주문 가격 총액
while True:
        user_order = input("메뉴를 입력하세요.주문 종료는 z을 누르세요")
        if ('z' in user_order) or ('ㅋ' in user_order):
                if len(order) == 0:
                        print("메뉴를 잘못 입력하셨습니다.")
                        continue
                else:
                        break
        if user_order not in menu:
                print("메뉴에 없습니다.")
        else:
                order_sum += menu[user_order]
                order.append(user_order)

#메뉴 추가 할인
if 2 <= len(order):
        order_sum = order_sum * 0.8
elif 3 <= len(order):
        order_sum = order_sum * 0.75
elif 4 <= len(order):
        order_sum = order_sum * 0.7
else:
        order_sum = order_sum * 1

how_order = input("식사방식을 선택해주세요. 1. 매장식사 2. 배달 3. 포장")
if how_order == '1':
        order_sum = order_sum * 1
elif how_order == '2':
        order_sum = order_sum + 8900
elif how_order == '3':
        order_sum = order_sum * 0.9

print("주문 메뉴는 {0}입니다".format(", ".join(order)))
print("주문 총액은 {0}입니다".format(order_sum))