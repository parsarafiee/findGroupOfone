countgroup=1
countgroup_of_one_array=[]
def check_to_search(p_i,p_j,matrix):
    allow=True
    if p_j <0:
        allow=False
    if p_j >len(matrix[0])-1:
        allow=False
    if p_i<0:
        allow=False
    if p_i>len(matrix)-1:
        allow=False
    return allow



def looking_for1(p_i,p_j,matrix,countgroup):
    # global countgroup
    if matrix[p_i][p_j]==1:
        matrix[p_i][p_j]=0
        if check_to_search(p_i,p_j+1,matrix):
            if matrix[p_i][p_j+1] == 1:
                countgroup =countgroup+1
                countgroup = looking_for1(p_i,p_j+1,matrix,countgroup)
        if check_to_search(p_i,p_j-1,matrix):
            if matrix[p_i][p_j-1] == 1:
                countgroup =countgroup+1
                countgroup = looking_for1(p_i,p_j-1,matrix,countgroup)
        if check_to_search(p_i+1,p_j,matrix):
            if matrix[p_i+1][p_j] == 1:
                countgroup =countgroup+1
                countgroup = looking_for1(p_i+1,p_j,matrix,countgroup)
        if check_to_search(p_i-1,p_j,matrix):
            if matrix[p_i-1][p_j] == 1:
                countgroup =countgroup+1
                countgroup = looking_for1(p_i-1,p_j,matrix,countgroup)

    return countgroup


myarray=[[0,0,1,0,1],
         [1,1,0,1,0],
         [1,1,0,1,0],
         [0,0,0,0,0],
         [1,1,0,1,0]]

for i in range (0, len(myarray)):
    for j in range (0, len(myarray[i])):
        a= looking_for1(i,j,myarray,countgroup)
        if a >=2 :

            countgroup_of_one_array.append(a)

print("number of group of 1 is  : "+format(len(countgroup_of_one_array)) )
print((countgroup_of_one_array))
