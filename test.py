graduation, score = map(int, input("졸업학점과 이수학점을 입력하세요: ").split('.'))

if graduation >= 2 and score >=140:
    print('졸업가능')
elif graduation < 2 and score >=140:
    print('졸업학점 부족으로 인한 졸업 불가능')
elif graduation >= 2 and score < 140:
    print('이수학점 부족으로 인한 졸업 불가능')
else:
    print("졸업학점과 이수학점 둘 다 부족합니다. 졸업 불가능")