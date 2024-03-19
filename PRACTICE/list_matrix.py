row1=['*','*','*']
row2=['*','*','*']
row3=['*','*','*']
matrix=[row1,row2,row3]
total_rows=len(matrix)
total_columns=len(matrix[0])  
print(total_rows,total_columns)
print(type(total_columns))
print(f"{row1}\n{row2}\n{row3}")

# alter_position=(input("Enter the position you want to alter : "))
# row_number=int(alter_position[0])
# column_number=int(alter_position[1])
# row_selected=matrix[row_number-1]
# row_selected[column_number-1]=input("Enter the value you want to alter : ")
# print(f"{row1}\n{row2}\n{row3}")


row=int(input("Enter the row number : "))
if row in range(1,total_rows):
    column=int(input("Enter the column number :"))
    if column in range(1,total_columns):
        matrix[row-1][column-1]=input(("Enter the value you want to alter : "))
        print(f"{row1}\n{row2}\n{row3}")
    else:
        print("Invalid column number")
else:
    print("Invalid row number")