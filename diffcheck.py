import pandas as pd
import numpy as np

invert1 = pd.read_excel("P:/PartTimers/DuyNguyen/Python Practice/pythonpractice/Bight18_Trawl_Data_1.xlsx",sheet_name = 'Inverts_1')
invert2 = pd.read_excel("P:/PartTimers/DuyNguyen/Python Practice/pythonpractice/Bight18_Trawl_Data_2.xlsx",sheet_name = 'Inverts_2')
invert1.rename(columns ={'StationID_Trawl#':'stationid',
                         'Species Name_TaxID':'speciesname',
                         'Total Count':'count',
                         'Vouchered':'voucher',
                         'Qualifier':'qualifier',
                         'Gross Weight (grams)': 'grossweight',
                         'Tare Weight (grams)':'tareweight',
                         'Net Weight (grams)':'netweight'}, inplace =True)
invert2.rename(columns ={'StationID_Trawl#':'stationid',
                         'Species Name_TaxID':'speciesname',
                       'Total Count':'count',
                         'Vouchered':'voucher',
                         'Qualifier':'qualifier',
                         'Gross Weight (grams)': 'grossweight',
                         'Tare Weight (grams)':'tareweight',
                         'Net Weight (grams)':'netweight'}, inplace =True)
invert1 = invert1[['stationid','speciesname','count','voucher','qualifier','grossweight','tareweight','netweight']]
invert2 = invert2[['stationid','speciesname','count','voucher','qualifier','grossweight','tareweight','netweight']]
Merge = pd.merge(invert1,invert2, how ='outer', on = ['stationid','speciesname'], suffixes=('_1', '_2'))

#Merge.to_excel('P:\PartTimers\DuyNguyen\Python Practice\pythonpractice\Invert Check.xlsx')
Mergeorigin = pd.merge(invert1,invert2, how ='outer', on = ['stationid','speciesname'], suffixes=('_1', '_2'))
Mergedrop = Mergeorigin.drop_duplicates(keep = 'first')
Merge['check counts']= Merge.apply( lambda x: x.count_1 == x.count_2, axis =1  )
Merge['check voucher']= Merge.apply( lambda x: x.voucher_1 == x.voucher_2, axis =1  )
Merge['check qualifier']= Merge.apply( lambda x: x.qualifier_1 == x.qualifier_2, axis =1  )
Merge['check grossweight']= Merge.apply( lambda x: x.grossweight_1 == x.grossweight_2, axis =1)
Merge['check tareweight']= Merge.apply( lambda x: x.tareweight_1 == x.tareweight_2, axis =1  )
Merge['check netweight']= Merge.apply( lambda x: x.netweight_1 == x.netweight_2, axis =1)
Diff = Merge[Merge.apply( lambda x: (x.count_1 != x.count_2) | (x.voucher_1 != x.voucher_2) | (x.qualifier_1 != x.qualifier_2)
|(x.grossweight_1 != x.grossweight_2) | (x.tareweight_1 != x.tareweight_2) |(x.netweight_1 != x.netweight_2), axis =1)]
with pd.ExcelWriter('P:\PartTimers\DuyNguyen\Python Practice\pythonpractice\diff_checkduy.xlsx') as writer:
    Mergeorigin.to_excel(writer, sheet_name = 'mergeorigin')
    Mergedrop.to_excel(writer, sheet_name = 'mergedrop')
    Diff.to_excel(writer, sheet_name = 'diff')
  