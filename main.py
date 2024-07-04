from tabula import read_pdf
from tabulate import tabulate
 
#reads table from pdf file
df = read_pdf("data/Karnataka/BLR_South.pdf") #address of pdf file
print(tabulate(df[0]))