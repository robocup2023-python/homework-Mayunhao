def matrixaddition(matrix1,matrix2):
   matrix=[]
   for i in range(len(matrix1)):
      row = []
      for j in range(len(matrix1[i])):
         matrix1[i][j]+=matrix2[i][j]
         row.append(matrix1[i][j])
      matrix.append(row)
   return matrix
matrix1=[[12,7,3],[4,5,6],[7,8,9]]
matrix2=[[5,8,1],[6,7,3],[4,5,9]]
matrix=matrixaddition(matrix1,matrix2)
print("[")
for i in matrix:
   print(i)
print("]")
