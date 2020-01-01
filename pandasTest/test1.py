import numpy as np
import pandas as pd
#3.2.1----create object
s=pd.Series([1,3,5,np.nan,6,8])
dates=pd.date_range('20130101',periods=6)
df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
df2=pd.DataFrame({
    'A':1.,
    'B':pd.Timestamp('20130102'),
    'C':pd.Series(1,index=list(range(4)),dtype='float32'),
    'D':np.array([3]*4,dtype='int32'),
    'E':pd.Categorical(["test","train","test","train"]),
    'F':'foo'})
#3.2.2----view data
df.head()
df.tail(3)
df.index
df.columns
df.to_numpy()
df.describe()#quick statistic summary
df.T#transposing you data
df.sort_index(axis=1,ascending=False)
df.sort_values(by='B')
#3.2.3------selection:at,iat,loc,iloc
df['A']#select A column
df[0:3]#select column 0-3
df['20130102':'20130104']#select row from 20130102 to 20130104
#print(dates)
#print(df.loc[dates[0]])
#print(df.loc[:,['A','B']])
#print(df.loc['20130102':'20130104',['A','B']])#select row and columns
#print(df.loc['20130102',['A','B']])
#print(df.loc[dates[0],'A'])
#print(df.at[dates[0],'A'])
#print(df)
#print(df.iloc[3])#select 3th row
#print(df.iloc[3:5,0:2])
#print(df.iloc[[1,2,4],[0,2]])
#print(df.iloc[1:3,:])
#print(df.iloc[:,1:3])
#print(df.iloc[1,1])
#print(df.iat[1,1])
#print(df[df.A>0])#select columnsA >0 of  rows
#print(df[df>0])
#df2[df2['E'.isin(['two','four'])]]
s1=pd.Series([1,2,3,4,5,6],index=pd.date_range('20130101',periods=6))
df['F']=s1#setting value
df.at[dates[0],'A']=0
df.iat[0,1]=0
df.loc[:,'D']=np.array([5]*len(df))
df2=df.copy()
df2[df2>0]=-df2
#3.2.4-----missing data:np.nan
df1=df.reindex(index=dates[0:4],columns=list(df.columns)+['E'])
df1.loc[dates[0]:dates[1],'E']=1
#df1.dropna(how='any')
#df1.fillna(value=5)
#3.2.5----operation
#print(df)
#print(df.mean())
#print(df.mean(1))
s=pd.Series([1,3,5,np.nan,6,8],index=dates).shift(2)
#print(s)
#df.sub(s,axis='index')
#print(df)
#print(df.apply(lambda x:x.max()))
#print(df.apply(np.cumsum))#addsum
s=pd.Series(np.random.randint(0,7,size=10))
#print(s)
#print(s.value_counts())
s=pd.Series(['A','B','C','Aaba','Baca',np.nan,'CABA','dog','cat'])
#print(s)
#print(s.str.lower())
#3.2.6----merge
df=pd.DataFrame(np.random.randn(10,4))
pieces=[df[:3],df[3:7],df[7:]]#merge
#print(df[:3])
#print(df[3:7])
#print(df[7:])
#print(df)
#print(pd.concat(pieces))#merge
left=pd.DataFrame({'key':['foo','foo'],'lval':[1,2]})
right=pd.DataFrame({'key':['foo','foo'],'rval':[4,5]})
#print(left)
#print(right)
#print(pd.merge(left,right,on='key'))
df=pd.DataFrame(np.random.randn(8,4),columns=['A','B','C','D'])
s=df.iloc[3]
#print(df)
#print(df.append(s,ignore_index=True))#appaned
#3.2.7------grouping:splitting,  applying,  Combining.....,
df=pd.DataFrame({'A':['foo','bar','foo','bar','foo','bar','foo','foo'],
                 'B':['one','one','two','three','two','two','one','three'],
                 'C':np.random.randn(8),
                 'D':np.random.randn(8)
                 })
#print(df)
#print(df.groupby('A').sum())
#print(df.groupby(['A','B']).sum())
#3.2.8----resharping
tuples=list(zip(*[['bar','bar','baz','baz','foo','foo','qux','qux'],
                  ['one','two','one','two','one','two','one','two']]))
index=pd.MultiIndex.from_tuples(tuples,names=['first','second'])
df=pd.DataFrame(np.random.randn(8,2),index=index,columns=['A','B'])
df2=df[:4]
#print(df2)
stacked=df2.stack()
#print(stacked)
df=pd.DataFrame({'A':['one','one','two','three']*3,
                 'B':['A','B','C']*4,
                 'C':['foo','foo','foo','bar','bar','bar']*2,
                 'D':np.random.randn(12),
                 'E':np.random.randn(12)})
#print(df)
#print(pd.pivot_table(df,values='D',index=['A','B'],columns=['C']))
#3.2.9 time series
rng=pd.date_range('1/1/2012',periods=100,freq='S')
ts=pd.Series(np.random.randint(0,500,len(rng)),index=rng)
#print(rng)
#print(ts)
#print(ts.resample('5Min').sum())
#3.2.10---categoricals
df=pd.DataFrame({"id":[1,2,3,4,5,6],
                 "raw_grade":['a','b','b','a','a','e']})
df["grade"]=df["raw_grade"].astype("category")
df["grade"].cat.categories=["very good","good","very bad"]
#print(df)
#print(df["grade"])
#3.2.11---plotting
ts=pd.Series(np.random.randn(1000),index=pd.date_range('1/1/2000',periods=1000))
#print(ts)
ts=ts.cumsum()
#print(ts)
#3.2.12---getting data in/out
#print(df)
#df.to_csv('foo.csv')
#df.read_csv('foo.vsv')
#df.to_hdf('foo.h5','df')
#df.read_hdf('foo.h5','df')
#df.to_excel('foo.xlsx',sheet_name='Sheet1')
pd.read_excel('foo.xlsx','Sheet1',index_col=None,na_values=['NA'])
#print(df)
#3.2.13---gotchas
#if pd.Series([False,True,False]):
print("I was true")
