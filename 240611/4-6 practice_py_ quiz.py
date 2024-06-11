#Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오.

#예)http://naver.com

# 규칙1 : http:// 부분은 제외 --> naver.com
# 규칙2 : 처음 만나는 점 (.) 이후 부분은 제외 --> naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e'갯수+ "!"로 구성
#                 (nav)              (5)       (1)       (!)
#예) 생성된 비밀번호 :nav51!

url = "http://naver.com"
my_str = url.replace("http://", "") # 규칙1
print(my_str)
my_str= my_str[:my_str.index(".")] #규칙2
my_str[0:5] -> 0~5 직전까지. (0,1,2,3,4)
print(my_str)

#한글로 된 사용자명 때문에 오류가 난듯하다.http://등을 사용할때 나는 오류일 가능성도 있다.
#>>> & C:/Users/최유영/AppData/Local/Programs/Python/Python312/python.exe "c:/Users/최유영/Desktop/파이썬/6시간_코딩_유튜브/4-6 practice_py_ quiz.py"  
#  File "<stdin>", line 1
#   & C:/Users/최유영/AppData/Local/Programs/Python/Python312/python.exe "c:/Users/최유영/Desktop/파이썬/6시간_코딩_유튜브/4-6 practice_py_ quiz.py"  
#    ^
#SyntaxError: invalid syntax
>>>

password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀 번호는 {1} 입니다. ".format(url, password))