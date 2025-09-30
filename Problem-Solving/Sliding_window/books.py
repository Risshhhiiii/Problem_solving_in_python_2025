books = [2, 5, 3, 4, 3, 6, 7, 8, 5, 2, 1, 3, 4]
k = int(input())
summ = sum(books[:k])
max_sum = summ  # use a separate variable for max sum
for i in range(1, len(books) - k + 1):
    summ = summ - books[i - 1] + books[i + k - 1]
    max_sum = max(summ,max_sum)
print(max_sum)

