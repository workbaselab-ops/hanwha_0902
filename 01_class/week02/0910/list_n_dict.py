# my_list = ["a", "b", "c"]
# my_dict = {"name" : "John", "age" : 34}           # 키의 이름으로 찾는다

# [문제]1번째 값의 이름을 가져와라
my_family = [{"name" : "김은영", "age" : 37},       #[0]
                {"name" : "김희영", "age" : 34},    #[1]
                {"name" : "김소영", "age" : 29}     #[2]
                ]

# for문에서 직접 user 변수 만든다.
for user in my_family:                
      if user["name"] == "김희영":   #user 매개변수로 지정
          print(user)

print("---")
#---------------
# {'name': '김희영', 'age': 34}
#---------------


# 김희영이 몇번째 인지 모를때
# my_family의 개수만큼 반복하면서 0부터 번호를 하나씩 꺼내자.
for i in range(len(my_family)):    
      if my_family[i]["name"] == "김희영":
           print(i)
           print(my_family[i])
           print(i, my_family[i])
# i = index 
# len() = 리스트에 몇 개 있는지 센다.

print("---")
#---------------
# 1
# {'name': '김희영', 'age': 34}
# 1 {'name': '김희영', 'age': 34}
#---------------



for i, user in enumerate(my_family):   
     if my_family[i]["name"] == "김희영":
          print(i, user)

#enumerate()가 순서와 데이터를 동시에 가져온다.
print("---")
#---------------
# 1 {'name': '김희영', 'age': 34}
#---------------