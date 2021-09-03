countgroup=1
def check_to_search(p_i,p_j,matrix):
    allow=True
    if p_j-1 <0:
        allow=False
    if p_j+1 >len(matrix[0])-1:
        allow=False
    if p_i-1<0:
        allow=False
    if p_i+1>len(matrix)-1:
        allow=False
    return allow



def looking_for1(p_i,p_j,matrix):
    global countgroup
    if matrix[p_i][p_j]==1:
        matrix[p_i][p_j]=0
        if matrix[p_i][p_j+1] == 1:
            countgroup =countgroup+1
            if check_to_search(p_i,p_j+1,matrix):
                looking_for1(p_i,p_j+1,matrix)
        if matrix[p_i][p_j-1] == 1:
            countgroup =countgroup+1
            if check_to_search(p_i,p_j-1,matrix):
                looking_for1(p_i,p_j-1,matrix)

        if matrix[p_i+1][p_j] == 1:
            countgroup =countgroup+1
            if check_to_search(p_i+1,p_j,matrix):
                looking_for1(p_i+1,p_j,matrix)
        if matrix[p_i-1][p_j] == 1:
            countgroup =countgroup+1
            if check_to_search(p_i-1,p_j,matrix):
                looking_for1(p_i-1,p_j,matrix)

    return countgroup


myarray=[[0,0,1,0,1],
         [1,1,1,1,0],
         [1,0,1,1,0],
         [1,0,1,1,0]]

print(looking_for1(1,1,myarray))