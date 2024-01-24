import pandas as pd
from pylatex import Enumerate, Itemize , Description ,Command


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
        dummyList = Description() 
                                                        #This "Dummylist" is a bulletless list and this is used to
                                                        #make the scientific name italic while the other names being bold. 
                                                        #Without using a list like this (See the previous commits.), using only three
                                                        #levels you cannot make the first line italic and second line of the same bullet 
                                                        #point bold.
        
        dummyList.add_item("",Command("textit",bird["Scientific Name"]+" ("+bird["Conservation Status"]+")"))
        dummyList.add_item("", Command("textbf",mergeBirdNames(bird["Common Name"],bird["Other names"])))
        secondOrderList.add_item(dummyList)
        thirdOrderList = Description()
       
        thirdOrderList.add_item("H: ",bird["Habitat and Distribution"])
        thirdOrderList.add_item("D: ",bird["Diet"])
        thirdOrderList.add_item("R: ",bird["Recorded Area(s)"])
        secondOrderList.append(thirdOrderList)
    firstOrderList.append(secondOrderList)
    
        

 


with open("./LatexCode.tex", "w") as tex_file:
    tex_file.write(firstOrderList.dumps())


    