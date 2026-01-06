# 리스트 컴프리헨션
# 일반적 코드 
numbers = []
for i in range(1, 11):
    if i % 2 == 0:
        numbers.append(i)
#리스트 컴프리헨션한 코드
numbers = [i for i in range(1, 11) if i % 2 == 0]
# 공백으로 구분된 여러 개의 숫자 리스트로 받기(ex. 1 2 3 4 5)
data = list(map(int, input().split()))

odd = [i for i in data if i %2==1]

print(sum(odd));

# 조금 더 줄일 수 있음
data = [i for i in map(int, input().split()) if i % 2 == 1]
print(sum(data))