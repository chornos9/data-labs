#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'lab-intro-pandas/your-code'))
	print(os.getcwd())
except:
	pass

#%%
# repaso/intro pandas: @albertogcmr

import pandas as pd


df = pd.read_csv('./titanic.csv')


#%%
df.head()


#%%
df.tail()


#%%
df.describe()


#%%
df.info()


#%%
df.columns


#%%
df.index


#%%
df.dtypes


#%%
df.head()


#%%
df['Age']


#%%
df.Age


#%%
df.Sex.value_counts() # siendo una serie
# df.Age.value_counts() # siendo una serie


#%%
df_aux = df.copy()


#%%
# memoria

a = [1,2,3]
b = a
# así no hay problemas 
# b = [x for x in a]
a, b


#%%
a[0] = 99
a, b


#%%
b[1] = 99
a, b


#%%
df_aux.head()


#%%
# axis=0
# axis='index'
# axis=1
# axis='columns'
df_aux.drop(1, axis=0) # .head()


#%%
df_aux.head() # qué ha pasado? vuelve a aparecer


#%%
# hay dos opciones: 

# df_aux = df_aux.drop(1, axis=0) # reasignar
df_aux.drop(1, axis=0, inplace=True)


#%%
df_aux.head()


#%%
df_aux.drop(labels=[2,3,4], 
            axis=0, 
            errors='ignore', 
            inplace=True) # usar los nombres de los parámetros

df_aux.head() 


#%%
# errors

df_aux.drop(labels=[2,3,4,5], errors='ignore', axis=0, inplace=True) # usar los nombres de los parámetros
df_aux.head() 


#%%
df_aux = df.copy()
df_aux.shape


#%%
df_aux = df.copy()
df_aux.dropna(inplace=True)
df_aux.shape


#%%
df_aux = df.copy()
df_aux.dropna(axis=1, inplace=True)
df_aux.shape


#%%
# ¿qué ha pasado?

df.info()


#%%
registros = df_aux.shape[0]
registros


#%%
df_num = df._get_numeric_data()
df_num.head()


#%%
# replace

df.replace('male', 'XY').replace('female', 'XX').head()


#%%
df_replace = df.replace(to_replace={'male': 'hombre', 'female': 'mujer'}, inplace=False)
df_replace.head()


#%%
df_rename = df.rename(columns={'Sex': 'Sexo'}, inplace=False)
df_rename.columns


#%%
df.head()


#%%
# df.Survived.value_counts()
df.Survived.unique()


#%%
set(df.Survived)


#%%
df.dtypes


#%%
df_astype = df.copy()
serie = df_astype.Survived
# df_astype.Survived = serie.astype('bool')
df_astype['Survived'] = serie.astype('bool')
df_astype.head()


#%%
df_astype.dtypes


#%%
df_astype._get_numeric_data() # booleano es numérico


#%%
df_astype = df.copy()
serie = df_astype.Pclass
df_astype['Pclass'] = serie.astype(dtype='float64', errors='ignore')
df_astype.head()


#%%
df_astype.dtypes


#%%
df.head()


#%%
# i de índice

df.iloc[1:4, 3:5]
df.iloc[1:4, :]
df.iloc[1:4, -1]
df.iloc[1:4, ::-1]


#%%
df.iloc[1:4, [3,5,7]]


#%%
df.loc[1:4, 'Name':'Sex']


#%%
df.loc[1:3, ['Name', 'Sex', 'Ticket']]


#%%
# df.transpose()
df.T 


#%%
df.head()


#%%
df.sample()


#%%
# df.head()
df_nc = df.copy()
df_nc['nueva columna'] = df_nc['Pclass'] * 2 + df_nc['Fare'] / 100 # siempre que la operación esté permitida
df_nc.head()


#%%
# df.Name.str.split()
names = df.Name.str.split('a')
names[:5]


#%%
df.head()


#%%
df.Pclass.sum()
df.sum()


#%%
df.min()


#%%
df.max()


#%%
df.count()


#%%
df.mean()


#%%
df.head()


#%%
df[df['Sex']=='male']


#%%
# paréntesis importante

df[(df['Age'] > 50) & (df['Survived'] == 1) | (df['SibSp'] == 3) & ~(df['Survived'].isin([2,3,4]))]


#%%
df.isnull() # .head()


#%%
df.isnull().sum() # .head()


#%%
df.head()


#%%
df.fillna('-').head()


#%%
df.head()


#%%
# Next steps

# set_index

# reset_index

# drop duplicates
# pandas.DataFrame.drop_duplicates

# pandas.DataFrame.apply(funcion)
# df['Age'].apply(lambda x: x+3)
# pandas.DataFrame.apply(lambda x: x['Sex'] + x['Name'])

# merge -> join en sql

# concat -> append de dataframes


#%%
df.head()


#%%
df.set_index('PassengerId', inplace=True)


#%%
df.head()


#%%
df.reset_index(inplace=True)


#%%
df.head()


#%%
# +10 años a todo el mundo

def suma10(x): 
    return x + 10

df.Age = df.Age.apply(suma10)
df.head()


#%%



