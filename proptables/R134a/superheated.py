import pandas as pd
from bisect import bisect_left
from pathlib import Path
from proptables.R134a.import_data import data_path_Super
from proptables.R134a.import_data import data_path_SupPreSat

class SuperHeated:
    def __init__(self):   
        self.dfSuperHeated=pd.read_csv(data_path_Super,header=None)
        self.pre=[60,100,140,180,200,240,280,320,400,500,600,700,800,900,1000,1200,1400,1600,1800,2000]
        self.dfSupSat=pd.read_csv(data_path_SupPreSat)


    ######################################################### Super Heated 1st Tables###################################
    def superheated_Pres_60(self):
        table=self.dfSuperHeated.iloc[2:17,0:5]
        return table

    def superheated_Pres_100(self):
        table=self.dfSuperHeated.iloc[2:17,6:10]
        table.insert(0,1,self.dfSuperHeated.iloc[2:17,0])
        # print(table)
        return table

    def superheated_Pres_140(self):
        table=self.dfSuperHeated.iloc[2:17,11:15]
        table.insert(0,1,self.dfSuperHeated.iloc[2:17,0])
        # print(table)
        return table

    ######################################################### Super Heated 3nd Tables###################################

    def superheated_Pres_180(self):
        table=self.dfSuperHeated.iloc[20:34,0:5]
        # print(table)
        return table

    def superheated_Pres_200(self):
        table=self.dfSuperHeated.iloc[20:34,6:10]
        table.insert(0,1,self.dfSuperHeated.iloc[20:34,0])
        # print(table)
        return table

    def superheated_Pres_240(self):
        table=self.dfSuperHeated.iloc[20:34,11:15]
        table.insert(0,1,self.dfSuperHeated.iloc[20:34,0])
        # print(table)
        return table

    ######################################################### Super Heated 3rd Tables###################################
    def superheated_Pres_280(self):
        table=self.dfSuperHeated.iloc[37:51,0:5]
        # print(table)
        return table

    def superheated_Pres_320(self):
        table=self.dfSuperHeated.iloc[37:51,6:10]
        table.insert(0,1,self.dfSuperHeated.iloc[37:51,0])
        # print(table)
        return table

    def superheated_Pres_400(self):
        table=self.dfSuperHeated.iloc[37:51,11:15]
        table.insert(0,1,self.dfSuperHeated.iloc[37:51,0])
        # print(table)
        return table

    ######################################################### Super Heated 4th Tables###################################
    def superheated_Pres_500(self):
        table=self.dfSuperHeated.iloc[54:69,0:5]
        # print(table)
        return table

    def superheated_Pres_600(self):
        table=self.dfSuperHeated.iloc[54:69,6:10]
        table.insert(0,1,self.dfSuperHeated.iloc[54:69,0])
        # print(table)
        return table

    def superheated_Pres_700(self):
        table=self.dfSuperHeated.iloc[54:69,11:15]
        table.insert(0,1,self.dfSuperHeated.iloc[54:69,0])
        # print(table)
        return table

    ######################################################### Super Heated 5th Tables###################################
    def superheated_Pres_800(self):
        table=self.dfSuperHeated.iloc[72:87,0:5]
        # print(table)
        return table

    def superheated_Pres_900(self):
        table=self.dfSuperHeated.iloc[72:87,6:10]
        table.insert(0,1,self.dfSuperHeated.iloc[72:87,0])
        # print(table)
        return table

    def superheated_Pres_1000(self):
        table=self.dfSuperHeated.iloc[72:87,11:15]
        table.insert(0,1,self.dfSuperHeated.iloc[72:87,0])
        # print(table)
        return table

    ######################################################### Super Heated 6th Tables###################################
    def superheated_Pres_1200(self):
        table=self.dfSuperHeated.iloc[90:106,0:5]
        # print(table)
        return table

    def superheated_Pres_1400(self):
        table=self.dfSuperHeated.iloc[72:87,6:10]
        table.insert(0,1,self.dfSuperHeated.iloc[72:87,0])
        # print(table)
        return table

    def superheated_Pres_1600(self):
        table=self.dfSuperHeated.iloc[72:87,11:15]
        table.insert(0,1,self.dfSuperHeated.iloc[72:87,0])
        # print(table)
        return table

    ######################################################### Super Heated 6th Tables###################################
    def superheated_Pres_1800(self):
        table=self.dfSuperHeated.iloc[111:125,0:5]
        # print(table)
        return table

    def superheated_Pres_2000(self):
        table=self.dfSuperHeated.iloc[111:125,6:10]
        table.insert(0,1,self.dfSuperHeated.iloc[111:125,0])
        # print(table)
        return table
##########################################################################################################################################
    def superheatedTable_interpolate(self,result,Pressure):
        result=result.reset_index(drop=True)
        result=result.set_axis(["Temp","v","energy","enthalpy","entropy"],axis=1)
        if Pressure in self.dfSupSat["Pressure"].values:
            indexing=self.dfSupSat[self.dfSupSat["Pressure"].values==Pressure].index.values
            result["Temp"].values[1]=self.dfSupSat["SaturatedTemperature"].values[indexing][0]
        result=result.iloc[1:]
        # result=result.reset_index(drop=True)
        result=result.apply(pd.to_numeric)
        return result
    
    def superheated_Pres_unknown(self,table1,Pressure1,table2,Pressure2,Pressure):
        table1=self.superheatedTable_interpolate(table1,Pressure1)
        table2=self.superheatedTable_interpolate(table2,Pressure2)

        return table1+(table2-table1).multiply((Pressure-Pressure1)/(Pressure2-Pressure1))


##########################################################################################################################################

def superheatedtable(pressure):
    sup=SuperHeated()
    pre=[60,100,140,180,200,240,280,320,400,500,600,700,800,900,1000,1200,1400,1600,1800,2000]
    mode=[
        sup.superheated_Pres_60(),sup.superheated_Pres_100(),sup.superheated_Pres_140(),
        sup.superheated_Pres_180(),sup.superheated_Pres_200(),sup.superheated_Pres_240(),sup.superheated_Pres_280(),
        sup.superheated_Pres_320(),sup.superheated_Pres_400(),sup.superheated_Pres_500(),sup.superheated_Pres_600(),sup.superheated_Pres_700(),
        sup.superheated_Pres_800(),sup.superheated_Pres_900(),sup.superheated_Pres_1000(),sup.superheated_Pres_1200(),sup.superheated_Pres_1400(),
        sup.superheated_Pres_1600(),sup.superheated_Pres_1800(),sup.superheated_Pres_2000()
    ]
    if pressure in pre:
        val=pre.index(pressure)
        result=sup.superheatedTable_interpolate(mode[val],pressure)
        result=result.set_axis(["Temp","v","energy","enthalpy","entropy"],axis=1)
        result=result.reset_index(drop=True)
        return result
    bk=bisect_left(pre,pressure)
    result=sup.superheated_Pres_unknown(mode[bk-1],pre[bk-1],mode[bk],pre[bk],pressure)
    result=result.set_axis(["Temp","v","energy","enthalpy","entropy"],axis=1)
    result=result.reset_index(drop=True)
    return result


# print(superheatedtable(450))
# print(superheatedtable(100))

# print(superheatedtable(61))
    

