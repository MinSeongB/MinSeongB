br = ("=" * 100)

# ['one', 'two', 'three']라는 리스트의 첫 번째 요소인 'one'이 먼저 i 변수에 대입된 후 print(i)라는 문장을 수행한다.
# 다음에 'two'라는 두 번째 요소가 i 변수에 대입된 후 print(i) 문장을 수행하고 리스트의 마지막 요소까지 이것을 반복한다.
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)
print(br)

print("다양한 for문의 사용")

a = [(1, 2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)

print(br)



