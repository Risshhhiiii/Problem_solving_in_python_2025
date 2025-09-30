matrix = [[1,1,1,0,1],
        [1,1,0,0,0],
        [1,0,0,1,1]]

def fire(grid,i,j):
    if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]!=1 :
        return
    grid[i][j] = 2
    fire(grid,i+1,j) #down
    fire(grid,i-1,j) #up
    fire(grid,i,j+1) #right
    fire(grid,i,j-1) #left

fire(matrix,0,0)
for row in matrix:
    print(row)
count = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j]==1:
            count+=1
print(count)