files = ["data1.csv", "data2.csv", "readme.txt"]

# loop through files
# only process .csv files

for file in files:
    if file.endswith(".csv"):
        print (f"File name is {file}")
    else:
        continue


thresholds = [0.7, 0.8, 0.9]

# print each threshold multiplied by 100
for threshold in thresholds:
    print (f" threshold is : {threshold * 100}")




# keep adding 100 rows
# stop when rows >= 500
# print rows each time
rows = 0

while rows < 500:
    rows = rows + 100
    print (rows)