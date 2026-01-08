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

# 파이썬 한 줄 조건문
# 참일 때 값 if 조건 else 거짓일 때 값
data = [("High" if i >= 10 else "Low") for i in map(int, input().split())]
# 실행 순서
# 1. input().split() : 사용자 문자열을 공백 기준으로 쪼개서 리스트로 생성
# 2. map(int, ~) : 쪼개진 문자열들을 하나씩 정수(int)로 변환
# 3. for i in ~ : 변환된 숫자들을 하나씩 꺼내서 i에 대입
# 4. "High" ~ : i를 검사해서 최종 값을 결정하고 리스트에 넣기

while True:
    input_data = input()
    if input_data == "그만":
        break
    if input_data % 2 == 0:
        print("짝수")
    else:
        print("홀수")
# 위에 코드에서는 형변환 이슈가 발생한다
# input()으로 받은 값은 컴퓨터가 문자열로 인식
# 계산을 위해서는 int()로 감싸야 한다 ex. int(input_data)

def check_number(number) : 
    if number % 2 == 0 :
        return 'Even'
    else :
        return 'Odd' 
    
while True :
    num = input('숫자를 입력하세요 : ' )
    check_number(int(num))
    if num == '그만' :
        break
# 두가지 오류 발생
# 1. 숫자인지 먼저 확인하는 것이 아닌 그만이라는 단어가 나왔는지 먼저 확인 후 int형으로 형변환을 해야한다
# 2. return을 하지만 출력을 하진 않는다 print(check_number(int(num)))를 해줘야 함 