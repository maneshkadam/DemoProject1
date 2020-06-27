X = [[1,2,3],  
       [4,5,6],  
       [7,8,9]]
Y =[[1,2,3],
    [5,3,4],
    [6,8,10]]
for i in range(len(X)):
    for j in range(len(X)):
        print(X[i][j]+Y[i][j])