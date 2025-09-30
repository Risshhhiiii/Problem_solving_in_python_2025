n = int(input())
vote_to = list((map(int,input().split())))
age = list(map(int,input().split()))
d = {}
for i in range(n):
    if age[i] >= 18 :
        if vote_to[i] not in d:
            d[vote_to[i]] = 1
        else:
            d[vote_to[i]]+=1
max_votes = -1
winner = None
for candidate in d:
    if d[candidate] > max_votes:
        max_votes = d[candidate]
        winner = candidate
print(winner)