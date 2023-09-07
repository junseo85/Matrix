# creating Matrix

row = int(input("enter the row number:"))
col = int(input("enter the col number:"))
print("enter the elements for matrix1:")

# print nested list for Matrix 1
Matrix1 = [[int(input()) for i in range(col)] for j in range(row)]
print(Matrix1)
# print as table format
for i in range(row):
    for j in range(col):
        print(format(Matrix1[i][j], "<3"), end="")

    print()

print("enter the elements for matrix2:")
# print nested list for Matrix 2
Matrix2 = [[int(input()) for i in range(col)] for j in range(row)]
print(Matrix2)
# print as table format
for i in range(row):
    for j in range(col):
        print(format(Matrix1[i][j], "<3"), end="")

    print()
# Matrix 1 and Matrix 2 addition
result = [[0 for i in range(col)] for j in range(row)]
for i in range(len(Matrix1)):
    for j in range(len(Matrix2)):
        result[i][j] = Matrix1[i][j] + Matrix2[i][j]
print("result is:", result)
for i in range(row):
    for j in range(col):
        print(format(result[i][j], "<3"), end="")
    print()