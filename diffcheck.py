import pandas as pd


df1 = pd.read_excel("P:/PartTimers/DuyNguyen/Python Practice/pythonpractice/Bight18_Trawl_Data_1.xlsx",sheet_name = 'Inverts_1')
df2 = pd.read_excel("P:/PartTimers/DuyNguyen/Python Practice/pythonpractice/Bight18_Trawl_Data_2.xlsx",sheet_name = 'Inverts_2')
df1.rename(columns ={'StationID_Trawl#':'stationid',
                         'Species Name_TaxID':'speciesname',
                         'Total Count':'count',
                         'Vouchered':'voucher',
                         'Qualifier':'qualifier',
                         'Gross Weight (grams)': 'grossweight',
                         'Tare Weight (grams)':'tareweight',
                         'Net Weight (grams)':'netweight'}, inplace =True)
df2.rename(columns ={'StationID_Trawl#':'stationid',
                         'Species Name_TaxID':'speciesname',
                       'Total Count':'count',
                         'Vouchered':'voucher',
                         'Qualifier':'qualifier',
                         'Gross Weight (grams)': 'grossweight',
                         'Tare Weight (grams)':'tareweight',
                         'Net Weight (grams)':'netweight'}, inplace =True)
df1 = df1[['stationid','speciesname','count','voucher','qualifier','grossweight','tareweight','netweight']]
df2 = df2[['stationid','speciesname','count','voucher','qualifier','grossweight','tareweight','netweight']]

Merge = pd.merge(df1,df2, how ='outer', on = ['stationid','speciesname'], suffixes=('_1', '_2'))
#Merge.to_excel('P:\PartTimers\DuyNguyen\Python Practice\pythonpractice\Invert Check.xlsx')
Merge['check_counts']= Merge.apply( lambda x: (x.count_1 == x.count_2) | ((pd.isna(x.count_1)) & (pd.isna(x.count_2))) , axis =1  )
Merge['check_voucher']= Merge.apply( lambda x: (x.voucher_1 == x.voucher_2) | ((pd.isna(x.voucher_1)) & (pd.isna(x.voucher_2))), axis =1  )
Merge['check_qualifier']= Merge.apply( lambda x: (x.qualifier_1 == x.qualifier_2) | ((pd.isna(x.qualifier_1)) & (pd.isna(x.qualifier_2))), axis =1  )
Merge['check_grossweight']= Merge.apply( lambda x: (x.grossweight_1 == x.grossweight_2) | ((pd.isna(x.grossweight_1)) & (pd.isna(x.grossweight_2))), axis =1)
Merge['check_tareweight']= Merge.apply( lambda x: (x.tareweight_1 == x.tareweight_2) | ((pd.isna(x.tareweight_1)) & (pd.isna(x.tareweight_2))), axis =1  )
Merge['check_netweight']= Merge.apply( lambda x: (x.netweight_1 == x.netweight_2) | ((pd.isna(x.netweight_1)) & (pd.isna(x.netweight_2))), axis =1)
Merge['In both files?']= Merge.apply( lambda x: (x.check_counts == 'FALSE') | ((pd.isna(x.netweight_1)) & (pd.isna(x.netweight_2))), axis =1)
Merge = Merge[['stationid',
 'speciesname','check_counts','count_1','count_2','check_voucher','voucher_1','voucher_2',
 'check_qualifier','qualifier_1','qualifier_2',
 'check_grossweight','grossweight_1','grossweight_2',
 'check_tareweight','tareweight_1','tareweight_2',
 'check_netweight','netweight_1','netweight_2']]
#Merge.to_excel('P:\PartTimers\DuyNguyen\Python Practice\pythonpractice\Invert Check.xlsx',index = False)
species1 = set(zip(df1['stationid'].tolist(), df1['speciesname'].tolist()))
species2 = set(zip(df2['stationid'].tolist(), df2['speciesname'].tolist()))

#Below is the set of species that are in 1 but not 2
A = species1 - species2

#Below is the set of species that are in 2 but not 1
B = species2 - species1
Set1notSet2 =pd.DataFrame(A)
Set1notSet2.rename(columns ={0:"Stationid_1",1:"Speciesname_1"}, inplace = True)
Set2notSet1 =pd.DataFrame(B)
Set2notSet1.rename(columns ={0:"Stationid_2",1:"Speciesname_2"}, inplace = True)



#Below is the code to export the .py file to excel file
writer = pd.ExcelWriter('P:\PartTimers\DuyNguyen\Python Practice\pythonpractice\Invert Check.xlsx', engine = 'xlsxwriter')
Merge.to_excel(writer, sheet_name = 'Check for values')
Set1notSet2.to_excel(writer, sheet_name = 'In Set 1 not in Set 2 list')
Set2notSet1.to_excel(writer, sheet_name = 'In Set 2 not in Set 1 list')
writer.save()
writer.close()
