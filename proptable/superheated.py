import pandas as pd
from bisect import bisect_left

class SuperHeated:
    def __init__(self):   
        self.dfSuperHeated=pd.read_csv("D:\\Property Table\\proptable\\R134a_Super.csv",header=None)


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
        return mode[val]
    bk=bisect_left(pre,pressure)
    return mode[bk]
    

