#https://github.com/umaimahmohammed-cpu/BIO511_dugga_umaimah_2025.git
#part 1 loops &if else
numbers = [15, -5, -12, 7, 10, -7, 3, -10, 4]


# a. 
sum_values =0 
abs_values=[]
for num in numbers:
    if abs(num) >= 10:
        abs_values.append(num)
        sum_values += num
print(abs_values)
print(sum_values)

# 2. b

cubes_nums = [] # empty list to save the list of cubes 
for items in numbers: #go over the loop
    if items >= 0:  # if itsms are more than 0
        continue  # skip posative numbers 
    else:
        cubes_nums.append(items **3 )   # to add it to the list 
print (f' the cube of nums is {cubes_nums}')

#c
scanned =[]
repeated = False

for num in abs_values:
    if num in scanned:
        print (f'the duplicate is {num}')
        repeated = True  #if true stop
        break
    else:
                scanned.append(num)  # add to scanned
if not repeated:
     print("No repeats")

#-------------------------------------------------------
#part 2
# read a file 
import csv 
import pandas as pd
import matplotlib.pyplot as plt


rows = [] ##empty list to store the contant 
with open("brca_head500_genes.csv", "r") as file:
    reader = csv.reader(file, delimiter =',')
    for row in reader:
        rows.append(row)

header = rows[0]  # first row is header
data = rows[1:]   # remaining rows are data
df = pd.DataFrame(data, columns=header)

print("\nDataFrame:")
print(df)

# 2.2.1 
# create a function 
def histoplot(dataframe):
    #plt.hist(dataframe['fpkm_log2']) # my original 
    plt.hist(dataframe['fpkm_log2'].dropna(), bins=30, color='skyblue', edgecolor='black') # .dropna ai help i forgot 
    plt.title('Distribution of gene expression')
    plt.xlabel('expression')
    plt.ylabel('number of genes')
    plt.show() 
    plt.savefig('fpkm_distribution.png', dpi=300) 
#2.2.2
#print the function 
histoplot(df)