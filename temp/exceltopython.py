# Import pandas
import pandas as pd
import numpy as np

# Assign spreadsheet filename to `file`
file = 'Book1.xlsx'

# Load spreadsheet
xl = pd.ExcelFile(file)



# Print the sheet names
print(xl.sheet_names)
print(type(xl))
# Load a sheet into a DataFrame by name: df1
df1 = xl.parse('Sheet1')
# print(df1.head([20]))
h = df1.as_matrix([2])
print(type(df1.head(20)))
print(df1.head(20))
print(df1.iloc[[0,20],[0,2,4]])

mydict = df1.iloc[:,[0,2,4]].to_dict('index')
print(len(mydict))
inchoptimdict = {}
for x in range(len(mydict)):
    currentvalue = mydict[x]["Inches"]
    # for y in range(len(mydict)):
    currentOD = mydict[x]["OD inches"]

    currentthick = mydict[x]["WallThickn.inches"]
    # inchoptimdict.setdefault(currentvalue, {currentOD : {"thick": [].append(currentthick)}})
    inchoptimdict.setdefault(str(currentvalue), {})
    inchoptimdict[str(currentvalue)].setdefault(str(currentOD), [])
    inchoptimdict[str(currentvalue)][str(currentOD)].append(str(currentthick))


    # tempvalue = mydict[y]["Inches"]
    # if(tempvalue == currentvalue):
    #     print(tempvalue)
    #     inchoptimdict.setdefault(tempvalue, {})
    #
    #     inchoptimdict[tempvalue].setdefault("OD inches", [])
    #     inchoptimdict[tempvalue]["OD inches"].append(mydict[y]["OD inches"])



print(inchoptimdict)



mydict = df1.iloc[:,[1,3,5]].to_dict('index')
mmoptimdict = {}
for x in range(len(mydict)):
    currentvalue = mydict[x]["mm"]
    # for y in range(len(mydict)):
    currentOD = mydict[x]["OD mm"]

    currentthick = mydict[x]["WallThickn.mm"]
    mmoptimdict.setdefault(str(currentvalue),{})
    mmoptimdict[str(currentvalue)].setdefault(str(currentOD), [])
    mmoptimdict[str(currentvalue)][str(currentOD)].append(str(currentthick))




print(mmoptimdict)
# print(sorted(mmoptimdict.iterkeys()))
# print(mmoptimdict['6'])



# print(mydict)
# print(mydict[0]["OD inches"])
#
# print(mydict.values())
# print(mydict.keys())

# mydict = {}
# print(len(df1))
# for x in range(len(df1)):
#     currentid = df1.iloc[x,0]
#     print(type(df1.iloc[x,[2,4]]))
#     currentvalue = df1.iloc[x,[2,4]]
#     mydict.setdefault(currentid, [])
#     mydict[currentid].append(currentvalue)
#
# print(mydict)
# print(df1.to_dict()) ['WallThickn.inches']

# print(df1.as_matrix([0,1]))
