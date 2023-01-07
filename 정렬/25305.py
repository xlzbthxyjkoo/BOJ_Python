N, k = map(int, input().split()) #응시자 수, 수상자 수
x = list(map(int, input().split()))  #점수

print(sorted(x)[-k]) #sorted는 오름차순이므로 반대로 세어주기
