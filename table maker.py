print("Table Tabular")
table = int(input("Enter the table that you want to make : "))
table_range = int(input("Enter the table range : "))

for i in range(1, table_range + 1) :
    result = str(table) + "x" + str(i) + "=" + str(table * i)
    print(result)