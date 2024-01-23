import pandas as pd
from pylatex import Enumerate, Itemize , Description


def mergeBirdNames(commonName, otherNames):
    # # Convert both names to title case
    commonName = commonName.title()
    if pd.isna(otherNames):
        return commonName
    final_name = commonName
    for name in otherNames.split(","):
        final_name+= "/"+name.title()
    return final_name

df = pd.read_excel('./uomBirds.xlsx')
dfgrouped = df.groupby("Family") #grouping by family of the bird.

firstOrderList = Itemize()

for group_name, group_data in dfgrouped:
    # Process each group_data as needed
    print(f"Group Name: {group_name}")
    print(group_data)
    # Perform your operations on the group_data
    firstOrderList.add_item(group_name)
    
    secondOrderList = Enumerate()
    for index,bird in group_data.iterrows():
        secondOrderList.add_item(bird["Scientific Name"]+"\n"+mergeBirdNames(bird["Common Name"],bird["Other names"]))
        thirdOrderList = Description()
       
        thirdOrderList.add_item("H: ",bird["Habitat and Distribution"])
        thirdOrderList.add_item("D: ",bird["Diet"])
        thirdOrderList.add_item("R: ",bird["Recorded Area(s)"])
        secondOrderList.append(thirdOrderList)
    firstOrderList.append(secondOrderList)
    
        

 


with open("./LatexCode.tex", "w") as tex_file:
    tex_file.write(firstOrderList.dumps())


    