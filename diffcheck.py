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
Merge.to_excel('P:\PartTimers\DuyNguyen\Python Practice\pythonpractice\Invert Check.xlsx')
Merge['check counts']= Merge.apply( lambda x: (x.count_1 == x.count_2) | ((pd.isna(x.count_1)) & (pd.isna(x.count_2))) , axis =1  )
Merge['check voucher']= Merge.apply( lambda x: (x.voucher_1 == x.voucher_2) | ((pd.isna(x.voucher_1)) & (pd.isna(x.voucher_2))), axis =1  )
Merge['check qualifier']= Merge.apply( lambda x: (x.qualifier_1 == x.qualifier_2) | ((pd.isna(x.qualifier_1)) & (pd.isna(x.qualifier_2))), axis =1  )
Merge['check grossweight']= Merge.apply( lambda x: (x.grossweight_1 == x.grossweight_2) | ((pd.isna(x.grossweight_1)) & (pd.isna(x.grossweight_2))), axis =1)
Merge['check tareweight']= Merge.apply( lambda x: (x.tareweight_1 == x.tareweight_2) | ((pd.isna(x.tareweight_1)) & (pd.isna(x.tareweight_2))), axis =1  )
Merge['check netweight']= Merge.apply( lambda x: (x.netweight_1 == x.netweight_2) | ((pd.isna(x.netweight_1)) & (pd.isna(x.netweight_2))), axis =1)
Merge = Merge[['stationid',
 'speciesname','check counts','count_1','count_2','check voucher','voucher_1','voucher_2',
 'check qualifier','qualifier_1','qualifier_2',
 'check grossweight','grossweight_1','grossweight_2',
 'check tareweight','tareweight_1','tareweight_2',
 'check netweight','netweight_1','netweight_2']]
Merge.to_excel('P:\PartTimers\DuyNguyen\Python Practice\pythonpractice\Invert Check.xlsx',index = False)