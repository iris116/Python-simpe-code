import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
import itertools
import openpyxl
from openpyxl import load_workbook

pd.set_option('display.max_columns',1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth',1000)

#################    SETTING
data = pd.read_excel("D:\query.xlsx")                                             # Data source
p = 4000                                                                            # Minimum Sample size
LEVEL = 0.2                                                                         # Show % of combination
combine_limit = 3                                                                   # MAX SEGMENTS FOR EACH GROUP(<=3)
#################    OPEN DATA PAKAGE
ATTRIBUTEPCA = data.loc[:,'attributes':'category']
ATTSHAPE = ATTRIBUTEPCA.shape[1]
ATTRIBUTEPCA = data.iloc[:,2:ATTSHAPE]

ATTRIBUTE = data.loc[:,'attributes':'category']
ATTSHAPE = ATTRIBUTE.shape[1]
ATTRIBUTE = data.iloc[:, 2:ATTSHAPE]
ATTRIBUTE_COL = ATTRIBUTE.columns.tolist()
for ccol in np.arange(ATTRIBUTE.shape[1]):
    for crow in np.arange(ATTRIBUTE.shape[0]):
        ATTRIBUTE_UNIT = str(ATTRIBUTE.iloc[crow, ccol])
        ATTRIBUTE_UNIT = ATTRIBUTE_COL[ccol]+': '+ATTRIBUTE_UNIT
        ATTRIBUTE.iloc[crow, ccol] = ATTRIBUTE_UNIT

print(ATTRIBUTE)



LABEL = data.loc[:,:'attributes']
LABEL = data.iloc[:, 0:1]

CATEGORY = data.loc[:,'category':]
CATEGORY = CATEGORY.iloc[:,1:]
CATEGORY_LIST = CATEGORY.columns.tolist()

print('CATEGORY AS: ')
print(CATEGORY_LIST)
print('LABEL AS:')
print(LABEL.columns.tolist())
print('ATTRIBUTES AS:')
print(ATTRIBUTEPCA.columns.tolist())
c = 1
print('Minimun sample size: '+str(p*c))
print('Max attributes for each combination: '+str(combine_limit))
print('Show ' +str((LEVEL)*100) +'% Combination')
##########   DESCRIPTION
datapca = ATTRIBUTEPCA
labelencoder = LabelEncoder()
ss_pca = StandardScaler()
for col in datapca.columns:
    datapca[col] = labelencoder.fit_transform(datapca[col].astype(str))
datapca = pd.DataFrame(datapca)

print('Description: ')
print(datapca.describe())
print('Unique values:')
print(datapca.nunique())


############### BUILD COMBINATION LIST
l = []
im_list = []
list_result_combinations = []
original = ATTRIBUTE
L = original.shape[1]
generator = (x for x in range(L))
for x in generator:
   im_list.append(x)
combine_limit = combine_limit+1
if len(im_list)<=combine_limit:
   limit= len(im_list)+1
else:
   limit = combine_limit
for i in range(1, limit):  # 调用组合函数
   iterator = itertools.combinations(im_list, i)
   list_result_combinations.append(list(iterator))
a = list(list_result_combinations)

for m in range(0, len(a)):
    for i in a[m]:
        l.append(list(i))
acc = []
i = 0

Label = LABEL.columns.values.tolist()
Label = Label[-1]
conj_all = pd.DataFrame(columns=['A', 'B', 'C', Label, 'MEAN', 'COUNT', 'CATEGORY'])

result = ATTRIBUTE.iloc[0:0,:]
con = pd.DataFrame(columns=['MEAN','COUNT'])
result = pd.concat([result, con], axis=1, sort=False)
print(l)
for cc in np.arange(len(CATEGORY_LIST)):

    y = CATEGORY.columns.values.tolist()
    y = y[cc]
    print('Running combination by: '+y)
    for n in l:

        data0 = ATTRIBUTE.iloc[:, n]
        dataraw = pd.concat([data0, LABEL.iloc[:, 0], CATEGORY.iloc[:, cc]], axis=1).dropna()
        mapping = pd.concat([data0, LABEL.iloc[:, 0]], axis=1).columns.values.tolist()

        groupedm = dataraw.groupby(mapping, as_index=False).mean()
        groupedm.rename(columns={y: 'MEAN'}, inplace=True)
        groupedc = dataraw.groupby(mapping, as_index=False).count()
        groupedc.rename(columns={y: 'COUNT'}, inplace=True)
        groupedme = dataraw.groupby(mapping, as_index=False).median()
        groupedme.rename(columns={y: 'MEDIAN'}, inplace=True)
        groupedstd = dataraw.groupby(mapping, as_index=False).agg({y: np.std})
        groupedstd.rename(columns={y: 'STD'}, inplace=True)

        grouped        = pd.concat([groupedm, groupedc['COUNT']], axis=1)
        grouped_backup = pd.concat([groupedm, groupedc['COUNT']], axis=1)

        dataraw_filter = pd.concat([data0, CATEGORY.iloc[:, cc]], axis=1).dropna()
        mapping_filter = data0.columns.values.tolist()
        grouped_filter = dataraw_filter.groupby(mapping_filter, as_index=False).count()
        count = grouped_filter[grouped_filter[y] > c * p]

        if not count.empty:
            for jj in np.arange(count.shape[0]):

                conj_inner = pd.DataFrame(columns=['A', 'B', 'C', Label, 'MEAN', 'COUNT', 'CATEGORY'])

                for ii in np.arange(grouped_backup.shape[0]):

                    X1 = grouped_backup.iloc[ii, :grouped_backup.shape[1] - 3].tolist()

                    X2 = count.iloc[jj, :count.shape[1] - 1].tolist()

                    if X1 == X2:
                        P1 = grouped.iloc[ii:ii+1, :]
                        if P1.shape[1]==4:
                              P1C = P1.columns.values.tolist()
                              P1.rename(columns={P1C[0]: 'A'}, inplace=True)
                        if P1.shape[1]==5:
                              P1C = P1.columns.values.tolist()
                              P1.rename(columns={P1C[0]: 'A',P1C[1]:'B'}, inplace=True)

                        if P1.shape[1] == 6:
                              P1C = P1.columns.values.tolist()
                              P1.rename(columns={P1C[0]: 'A', P1C[1]:'B', P1C[2]:'C'}, inplace=True)

                        P1.insert(0, 'CATEGORY', y)

                        conj_inner = pd.concat([conj_inner, P1], axis=0, sort=False)
                        #conj['MEAN'] = conj['MEAN'].astype('float64')
                conj_inner = conj_inner.sort_values(by='MEAN', axis=0, ascending=False)
                conj_inner = conj_inner.iloc[:int(conj_inner.shape[0]*LEVEL), :]
                conj_all = pd.concat([conj_all, conj_inner], axis=0, sort=False)

###########  SAVE TO
        conj_all.to_excel(r'D:/NEW_COMB.xlsx',sheet_name='OUTPUT')
