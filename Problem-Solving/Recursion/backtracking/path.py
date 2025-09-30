def path(grid,i,j,p,n):
    if i==n-1 and j==n-1:
        print(p)
        return
    if i+1<n and grid[i+1][j]==1:
        path(grid,i+1,j,p+'D',n)
    if j+1<n and grid[i][j+1]==1:
        path(grid,i,j+1,p+'R',n)
    
matrix = [[1,0,0,0],
          [1,1,0,1],
          [1,1,0,0],
          [0,1,1,1]]

path(matrix,0,0,'',len(matrix))