# What I learned (algorithm)

### 알고리즘 공부하면서 배운 유용한 팁들 🙄 (update ~ing)

1. 정수로 이루어진 리스트를 [] 떼고 문자열로 출력하는 법

   ```python
   #[0, 1, 2, 3]을 0 1 2 3 으로 출력하고 싶음!
   lst = [0, 1, 2, 3]
   lst = ' '.join(map(str, lst)) # input 받을 때만 map 쓰지 말고 이럴 때 요긴하게 쓰자
   lst = ' '.join([str(x) for x in result])
   ```


2. 반복문에서 `break` 활용 잘 하기. 주로 언제? 범위 처음부터 끝까지 다 돌 필요 없이 한 번 조건을 만족하는 값을 찾고 바로 반복문을 빠져 나가고 싶을 때!

3. `while True:` 는 언제 사용? 특정 조건을 만나기 전까지 무한으로 반복을 돌리고 싶을 때

4. 알고리즘 풀기 위해서 자체적인 함수를 정의할 땐 최대한 조건을 간단하게! 사용자 정의 함수가 너무 복잡해지면 예외 케이스가 발생하기 쉽다. 대신 함수 가동을 위한 **거름 장치를 최대한 빡세게** 하기

   ```python
   # SWEA_11570 제곱 팰린드롬 수
   팰린드롬 판별 함수) N이 들어오면 N을 string화 시켜서 판별
   이를 가동하기 전에 int(N**0.5)와 N**0.5가 같은지를 우선 판단하면 함수에서 굳이 N**0.5가 int인지를 판별할 필요 없음! (판별하려면 is_integer() 같은거 써야 됨)
   그리고 애초에 함수에 넣기 전에 int 변환을 시켜준다면 함수에서 굳이 N을 int화 한 다음 다시 string 변환할 필요가 없음!
   ```

5. `if if` vs `if elif` : `if if` 의 경우 첫번째 if를 만족하더라도 두번째 if를 확인 vs `if elif`의 경우 첫번째 if를 만족하면 elif를 확인하지 않음 -> 둘 다 써도 괜찮은 경우 후자를 쓸 때 실행시간 절약 가능!

   ```python
   # if if
   num = 10 
   if num == 10:
       print('이 값은 10이야!')
   if num < 20:
       print('이 값은 20보다는 적은 값이야!')
   '''
   이 값은 10이야!
   이 값은 20보다는 적은 값이야!
   '''
   # if elif
   num2 = 10 
   if num2 == 10:
       print('이 값은 10이야!')
   elif num < 20:
       print('이 값은 20보다는 적은 값이야!')
   '''
   이 값은 10이야!
   if를 만족했으므로 elif는 확인하지 않음.
   만약 num2 =9라면 if를 만족하지 않아서 elif 확인 후 이 값은 20보다는 적은 값이야!가 출력
   '''
   ```


6. 한 줄에 하나씩 출력하는거 print문 한개에 쓰는 법: `sep='\n'` 사용

   ```python
   print(a+b, a-b, a*b, a//b, a%b, sep='\n')
   ```

7. for문 돌릴 때 입출력 속도 높이는 법: `input` 대신 `sys.stdin.readline` 사용

   ```python
   # 기존
   T = int(input())
   A, B = map(int, input().split())
   # 속도 높이기
   T = int(sys.stdin.readline())
   A, B = map(int, sys.stdin.readlint().split())
   ```

8. EOF(End of file): 입력이 끝날 때까지 계속 출력하는..

   ```python
   try:
       [...]
   except: # 입력이 더이상 없다거나 에러가 나면 할 것
       break
   ```

9. 리스트에서 `.remove(값)` 은 첫 값만 지우기 때문에 중복된 값이 있으면 나중의 값을 지울 수 없음. 이럴 때는 `del list[해당 인덱스]` 를 하든지 단순히 리스트의 값을 재할당 해주면 됨

10. 특정 실수를 소숫점 n째자리까지 출력하고 싶을 때

    ```python
    # 셋째자리까지 출력
    a = 1.456765566
    print(f'{a:.3f}')
    print("%.3f" % a)
    ```

11. for 안에 if 조건문 만족하면 break 있을 때, for를 다 돌았을 시 무언가를 해주고 싶다? for - else 를 쓰면 됨! (else 생략하면 x)

12. string으로 이루어진 리스트의 요소들을 각각 int로 바꿔서 다시 리스트화 하고 싶을 때

    ```python
    tmp = ['1', '2', '3']
    list(map(int, tmp))
    # list로 감싸지 않으면 map object가 되어버림
    ```

13. 문자열 출력 시 대소문자 확인 잘 하기, 델타 쓸 때 델타 값 중복되진 않았는지 확인 잘 하기 제발 ...!!!!

14. sample input으로 테스트 해보고 싶을 때

    ```python
    import sys
    sys.stdin = open('input.text', 'r')
    ```

15. DFS 를 재귀로 풀 때 한 depth 더 내려가기 전에 어떤 행위를 한다면(ex. 배열에 체크 등등) depth 내려간 후에 다시 복원하기(다음 경우를 위해서!)

16. `if ~ in/not in` 쓸 땐 `list` 보다 `set`을 쓰는 것이 시간복잡도가 더 낮다