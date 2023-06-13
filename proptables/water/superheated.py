import pandas as pd
from bisect import bisect_left
from pathlib import Path
from proptables.water.import_data_water import data_path_SuperHeat,data_path_SuperSat

class SuperHeated:
    def __init__(self):   
        self.dfSuperHeated=pd.read_csv(data_path_SuperHeat,header=None)
        self.dfSupSat=pd.read_csv(data_path_SuperSat)
        self.pre=list(map(float,(self.dfSupSat["Pressure"])))
        # print(self.pre)

    ######################################################### Super Heated 1st Tables###################################
    def superheated_Pres_0010(self):
        table=self.dfSuperHeated.iloc[4:20,0:5]
        # print(table)
        return table

    def superheated_Pres_0050(self):
        table=self.dfSuperHeated.iloc[4:20,6:10]
        table.insert(0,1,self.dfSuperHeated.iloc[4:20,0])
        # print(table)
        return table

    def superheated_Pres_0100(self):
        table=self.dfSuperHeated.iloc[4:20,11:15]
        table.insert(0,1,self.dfSuperHeated.iloc[4:20,0])
        print(table)
        return table

    ######################################################### Super Heated 3nd Tables###################################

    def superheated_Pres_0200(self):
        table=self.dfSuperHeated.iloc[24:38,0:5]
        # print(table)
        return table

    def superheated_Pres_0300(self):
        table=self.dfSuperHeated.iloc[24:38,6:10]
        table.insert(0,1,self.dfSuperHeated.iloc[24:38,0])
        # print(table)
        return table

    def superheated_Pres_0400(self):
        table=self.dfSuperHeated.iloc[24:38,11:15]
        table.insert(0,1,self.dfSuperHeated.iloc[24:38,0])
        # print(table)
        return table

    ######################################################### Super Heated 3rd Tables###################################
    def superheated_Pres_0500(self):
        table=self.dfSuperHeated.iloc[42:55,0:5]
        # print(table)
        return table

    def superheated_Pres_0600(self):
        table=self.dfSuperHeated.iloc[42:55,6:10]
        table.insert(0,1,self.dfSuperHeated.iloc[42:55,0])
        # print(table)
        return table

    def superheated_Pres_0800(self):
        table=self.dfSuperHeated.iloc[42:55,11:15]
        table.insert(0,1,self.dfSuperHeated.iloc[42:55,0])
        # print(table)
        return table

    ######################################################### Super Heated 4th Tables###################################
    def superheated_Pres_1000(self):
        table=self.dfSuperHeated.iloc[59:72,0:5]
        # print(table)
        return table

    def superheated_Pres_1200(self):
        table=self.dfSuperHeated.iloc[59:72,6:10]
        table.insert(0,1,self.dfSuperHeated.iloc[59:72,0])
        # print(table)
        return table

    def superheated_Pres_1400(self):
        table=self.dfSuperHeated.iloc[59:72,11:15]
        table.insert(0,1,self.dfSuperHeated.iloc[59:72,0])
        # print(table)
        return table

    ######################################################### Super Heated 5th Tables###################################
    def superheated_Pres_1600(self):
        table=self.dfSuperHeated.iloc[76:89,0:5]
        # print(table)
        return table

    def superheated_Pres_1800(self):
        table=self.dfSuperHeated.iloc[76:89,6:10]
        table.insert(0,1,self.dfSuperHeated.iloc[76:89,0])
        # print(table)
        return table

    def superheated_Pres_2000(self):
        table=self.dfSuperHeated.iloc[76:89,11:15]
        table.insert(0,1,self.dfSuperHeated.iloc[76:89,0])
        # print(table)
        return table

    ######################################################### Super Heated 6th Tables###################################
    def superheated_Pres_2500(self):
        table=self.dfSuperHeated.iloc[93:105,0:5]
        # print(table)
        return table

    def superheated_Pres_3000(self):
        table=self.dfSuperHeated.iloc[93:105,6:10]
        table.insert(0,1,self.dfSuperHeated.iloc[93:105,0])
        # print(table)
        return table

    def superheated_Pres_3500(self):
        table=self.dfSuperHeated.iloc[93:105,11:15]
        table.insert(0,1,self.dfSuperHeated.iloc[93:105,0])
        # print(table)
        return table

    ######################################################### Super Heated 6th Tables###################################
    def superheated_Pres_4000(self):
        table=self.dfSuperHeated.iloc[109:121,0:5]
        # print(table)
        return table

    def superheated_Pres_4500(self):
        table=self.dfSuperHeated.iloc[109:121,6:10]
        table.insert(0,1,self.dfSuperHeated.iloc[109:121,0])
        # print(table)
        return table
    
    def superheated_Pres_5000(self):
        table=self.dfSuperHeated.iloc[109:121,11:15]
        table.insert(0,1,self.dfSuperHeated.iloc[109:121,0])
        # print(table)
        return table
    
        ######################################################### Super Heated 7th Tables###################################
    def superheated_Pres_6000(self):
        table=self.dfSuperHeated.iloc[125:136,0:5]
        # print(table)
        return table

    def superheated_Pres_7000(self):
        table=self.dfSuperHeated.iloc[125:136,6:10]
        table.insert(0,1,self.dfSuperHeated.iloc[125:136,0])
        # print(table)
        return table
    
    def superheated_Pres_8000(self):
        table=self.dfSuperHeated.iloc[125:136,11:15]
        table.insert(0,1,self.dfSuperHeated.iloc[125:136,0])
        # print(table)
        return table
    
######################################################### Super Heated 8th Tables###################################
    def superheated_Pres_9000(self):
        table=self.dfSuperHeated.iloc[140:150,0:5]
        # print(table)
        return table

    def superheated_Pres_10000(self):
        table=self.dfSuperHeated.iloc[140:150,6:10]
        table.insert(0,1,self.dfSuperHeated.iloc[140:150,0])
        # print(table)
        return table
    
    def superheated_Pres_12500(self):
        table=self.dfSuperHeated.iloc[140:150,11:15]
        table.insert(0,1,self.dfSuperHeated.iloc[140:150,0])
        print(table)
        return table
##########################################################################################################################################
    def superheatedTable_interpolate(self,result,Pressure):
        result=result.reset_index(drop=True)
        result=result.set_axis(["Temp","v","energy","enthalpy","entropy"],axis=1)
        if Pressure in self.dfSupSat["Pressure"].values:
            indexing=self.dfSupSat[self.dfSupSat["Pressure"].values==Pressure].index.values
            result["Temp"].values[1]=self.dfSupSat["SaturatedTemperature"].values[indexing][0]
        result=result.iloc[1:]
        result=result.apply(pd.to_numeric)
        return result
    
    def superheated_Pres_unknown(self,table1,Pressure1,table2,Pressure2,Pressure):
        table1=self.superheatedTable_interpolate(table1,Pressure1)
        table2=self.superheatedTable_interpolate(table2,Pressure2)

        return table1+(table2-table1).multiply((Pressure-Pressure1)/(Pressure2-Pressure1))


##########################################################################################################################################

def superheatedtable(pressure):
    sup=SuperHeated()
    pre=[0.01, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 12.5, 15.0, 17.5, 20.0, 25.0, 30.0, 40.0]
    mode=[
        sup.superheated_Pres_0010(),sup.superheated_Pres_0050(),sup.superheated_Pres_0100(),
        sup.superheated_Pres_0200(),sup.superheated_Pres_0300(),sup.superheated_Pres_0400(),sup.superheated_Pres_0500(),
        sup.superheated_Pres_0600(),sup.superheated_Pres_0800(),sup.superheated_Pres_1000(),sup.superheated_Pres_1200(),sup.superheated_Pres_1400(),
        sup.superheated_Pres_1400(),sup.superheated_Pres_1800(),sup.superheated_Pres_2000(),sup.superheated_Pres_2500(),sup.superheated_Pres_3000(),
        sup.superheated_Pres_3500(),sup.superheated_Pres_4000(),sup.superheated_Pres_4500(),
        sup.superheated_Pres_5000(),sup.superheated_Pres_6000(),sup.superheated_Pres_7000(),
        sup.superheated_Pres_8000(),sup.superheated_Pres_9000(),sup.superheated_Pres_10000(),
        sup.superheated_Pres_12500()
    ]
    if pressure in pre:
        val=pre.index(pressure)
        result=sup.superheatedTable_interpolate(mode[val],pressure)
        result=result.set_axis(["Temp","v","energy","enthalpy","entropy"],axis=1)
        return result
    bk=bisect_left(pre,pressure)
    result=sup.superheated_Pres_unknown(mode[bk-1],pre[bk-1],mode[bk],pre[bk],pressure)
    result=result.set_axis(["Temp","v","energy","enthalpy","entropy"],axis=1)
    return result


# print(superheatedtable(60))
# print(superheatedtable(100))

# print(superheatedtable(61))
sup=SuperHeated()
sup.superheated_Pres_9000()
sup.superheated_Pres_10000()
sup.superheated_Pres_12500()