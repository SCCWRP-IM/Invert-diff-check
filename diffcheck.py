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
Merge.to_excel('P:\PartTimers\DuyNguyen\Python Practice\pythonpractice\Merge.xlsx')