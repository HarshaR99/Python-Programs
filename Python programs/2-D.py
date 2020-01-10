# 2-D lists

number_grid = [
    [1,2,3],
    [4,5,6],
    [0]
]

# nested for loop
for row in number_grid :
    print(row)

print("Next for loop")

for row in number_grid :
    for col in row :
        print(col)