# [파이썬 3.0 이후 버전의 keys 함수, 어떻게 달라졌나?]
#
# 파이썬 2.7 버전까지는 a.keys() 호출 시 리턴값으로 dict_keys가 아닌 리스트를 리턴한다. 리스트를 리턴하기 위해서는 메모리의 낭비가 발생하는데 파이썬 3.0 이후 버전에서는 이러한 메모리 낭비를 줄이기 위해 dict_keys라는 객체를 리턴해 준다.
# 다음에 소개할 dict_values, dict_items 역시 파이썬 3.0 이후 버전에서 추가된 것들이다. 만약 3.0 이후 버전에서 리턴값으로 리스트가 필요한 경우에는 "list(a.keys())"를 사용하면 된다.
# dict_keys, dict_values, dict_items 등은 리스트로 변환하지 않더라도 기본적인 반복성(iterate) 구문(예: for문)들을 실행할 수 있다.
#
# dict_keys 객체는 다음과 같이 사용할 수 있다. 리스트를 사용하는 것과 차이가 없지만, 리스트 고유의 함수인 append, insert, pop, remove, sort등의 함수를 수행할 수는 없다

br = ("=" * 100)

a = {'name': 'bms', 'phone': '01025804945', 'birth': '0705'}
print(a.keys())

for bms_list in a.keys():
    print(bms_list  )



# dict_keys 객체를 리스트로 변환하려면 다음과 같이 하면 된다.
print(list(a.keys()))


# Key를 얻는 것과 마찬가지 방법으로 Value만 얻고 싶다면 a.values()처럼 values 함수를 사용하면 된다. values 함수를 호출하면 dict_values 객체가 리턴되는데,
# dict_values 객체 역시 dict_keys 객체와 마찬가지로 리스트를 사용하는 것과 동일하게 사용하면 된다.
a.values()
print(br)
print('Value 리스트 만들기(values)')
print(a.values())
print(br)
