import pandas as pd
from pylatex import Enumerate, Itemize

df = pd.read_excel('./uomBirds.xlsx')
dfgrouped = df.groupby("Family")

for group_name, group_data in dfgrouped:
    # Process each group_data as needed
    print(f"Group Name: {group_name}")
    print(group_data)
    # Perform your operations on the group_data
      
    
        

 


with open("./LatexCode.tex", "a") as tex_file:
    tex_file.write(firstLevelList.dumps())


    