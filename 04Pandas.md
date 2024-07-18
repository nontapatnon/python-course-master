## Pongsakorn

* 1231664
* 64654654
* 646464


```python
# pip install pandas
```

### Series


```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

    C:\Users\Nontapat\AppData\Local\Temp\ipykernel_30788\2151744951.py:1: DeprecationWarning: 
    Pyarrow will become a required dependency of pandas in the next major release of pandas (pandas 3.0),
    (to allow more performant data types, such as the Arrow string type, and better interoperability with other libraries)
    but was not found to be installed on your system.
    If this would cause problems for you,
    please provide us feedback at https://github.com/pandas-dev/pandas/issues/54466
            
      import pandas as pd
    


```python
import pandas as pd
series = pd.Series(["A","B","AB","O"])
series[4] = "O-"
print(series)
```

    0     A
    1     B
    2    AB
    3     O
    4    O-
    dtype: object
    


```python
series
```




    0     A
    1     B
    2    AB
    3     O
    4    O-
    dtype: object



### DataFrame


```python
import pandas as pd
pd.__version__
```




    '2.2.0'




```python
import pandas as pd
data  = [1,2,3,4,5]
df1 = pd.DataFrame(data)
# display(df1)

data = [['Alice', 21], ['Bob', 22], ['Cathy', 23]]
df2 = pd.DataFrame(data, columns = ["Name", "Age"])
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alice</td>
      <td>21</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bob</td>
      <td>22</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Cathy</td>
      <td>23</td>
    </tr>
  </tbody>
</table>
</div>




```python
d = {'name' : pd.Series(['Alice','Bob','Cathy','Dave']),
    'Age': pd.Series([21,22,23,24]),
    'Score' : pd.Series([80,85,90,95])}

df3 = pd.DataFrame(d)
df3
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>Age</th>
      <th>Score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alice</td>
      <td>21</td>
      <td>80</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bob</td>
      <td>22</td>
      <td>85</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Cathy</td>
      <td>23</td>
      <td>90</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Dave</td>
      <td>24</td>
      <td>95</td>
    </tr>
  </tbody>
</table>
</div>




```python
df3.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 4 entries, 0 to 3
    Data columns (total 3 columns):
     #   Column  Non-Null Count  Dtype 
    ---  ------  --------------  ----- 
     0   name    4 non-null      object
     1   Age     4 non-null      int64 
     2   Score   4 non-null      int64 
    dtypes: int64(2), object(1)
    memory usage: 228.0+ bytes
    


```python
df3.columns
```




    Index(['name', 'Age', 'Score'], dtype='object')




```python
for i in df3['name']:
    print(i)
```

    Alice
    Bob
    Cathy
    Dave
    


```python
for i in df3['Age']:
    print(i)
```

    21
    22
    23
    24
    


```python
df3
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>Age</th>
      <th>Score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alice</td>
      <td>21</td>
      <td>80</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bob</td>
      <td>22</td>
      <td>85</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Cathy</td>
      <td>23</td>
      <td>90</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Dave</td>
      <td>24</td>
      <td>95</td>
    </tr>
  </tbody>
</table>
</div>




```python
df4 = df3[df3['Score'] > 80]
df4
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>Age</th>
      <th>Score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Bob</td>
      <td>22</td>
      <td>85</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Cathy</td>
      <td>23</td>
      <td>90</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Dave</td>
      <td>24</td>
      <td>95</td>
    </tr>
  </tbody>
</table>
</div>




```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```


```python
# pip install seaborn
```


```python
df = pd.read_csv('https://nontapatnon.github.io/python-course-master/datascience/Titanic-Dataset.csv')
# display(df)
# df.head(10)
# df.tail(10)
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>
      <td>female</td>
      <td>35.0</td>
      <td>1</td>
      <td>0</td>
      <td>113803</td>
      <td>53.1000</td>
      <td>C123</td>
      <td>S</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0</td>
      <td>3</td>
      <td>Allen, Mr. William Henry</td>
      <td>male</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>373450</td>
      <td>8.0500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 891 entries, 0 to 890
    Data columns (total 12 columns):
     #   Column       Non-Null Count  Dtype  
    ---  ------       --------------  -----  
     0   PassengerId  891 non-null    int64  
     1   Survived     891 non-null    int64  
     2   Pclass       891 non-null    int64  
     3   Name         891 non-null    object 
     4   Sex          891 non-null    object 
     5   Age          714 non-null    float64
     6   SibSp        891 non-null    int64  
     7   Parch        891 non-null    int64  
     8   Ticket       891 non-null    object 
     9   Fare         891 non-null    float64
     10  Cabin        204 non-null    object 
     11  Embarked     889 non-null    object 
    dtypes: float64(2), int64(5), object(5)
    memory usage: 83.7+ KB
    


```python
df.columns
```




    Index(['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
           'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'],
          dtype='object')




```python
df[df['Survived'] == 0][['Name', 'Sex']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Sex</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Allen, Mr. William Henry</td>
      <td>male</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Moran, Mr. James</td>
      <td>male</td>
    </tr>
    <tr>
      <th>6</th>
      <td>McCarthy, Mr. Timothy J</td>
      <td>male</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Palsson, Master. Gosta Leonard</td>
      <td>male</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>884</th>
      <td>Sutehall, Mr. Henry Jr</td>
      <td>male</td>
    </tr>
    <tr>
      <th>885</th>
      <td>Rice, Mrs. William (Margaret Norton)</td>
      <td>female</td>
    </tr>
    <tr>
      <th>886</th>
      <td>Montvila, Rev. Juozas</td>
      <td>male</td>
    </tr>
    <tr>
      <th>888</th>
      <td>Johnston, Miss. Catherine Helen "Carrie"</td>
      <td>female</td>
    </tr>
    <tr>
      <th>890</th>
      <td>Dooley, Mr. Patrick</td>
      <td>male</td>
    </tr>
  </tbody>
</table>
<p>549 rows × 2 columns</p>
</div>




```python
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>
      <td>female</td>
      <td>35.0</td>
      <td>1</td>
      <td>0</td>
      <td>113803</td>
      <td>53.1000</td>
      <td>C123</td>
      <td>S</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0</td>
      <td>3</td>
      <td>Allen, Mr. William Henry</td>
      <td>male</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>373450</td>
      <td>8.0500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
  </tbody>
</table>
</div>




```python
import matplotlib.pyplot as plt
df['Survived'].value_counts()
```




    Survived
    0    549
    1    342
    Name: count, dtype: int64




```python
df.groupby(['Sex','Survived'])[['Survived']].count()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Survived</th>
    </tr>
    <tr>
      <th>Sex</th>
      <th>Survived</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">female</th>
      <th>0</th>
      <td>81</td>
    </tr>
    <tr>
      <th>1</th>
      <td>233</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">male</th>
      <th>0</th>
      <td>468</td>
    </tr>
    <tr>
      <th>1</th>
      <td>109</td>
    </tr>
  </tbody>
</table>
</div>




```python
# ax[0].set_title('Survivedvs Sex')
```


```python
df[['Sex', 'Survived']].groupby(['Sex']).mean().plot.bar()
plt.show()
```


![png](https://nontapatnon.github.io/python-course-master/md_image_src/output_28_0.png)
    



```python
f, ax = plt.subplots(1, 2, figsize = (18,8))
ax[0].set_title('Survived vs Sex')
df[['Sex', 'Survived']].groupby(['Sex']).mean().plot.bar(ax = ax[0])

ax[1].set_title('Sex:Survived vs Dead')
sns.countplot(x = 'Sex', hue = 'Survived', data = df, ax = ax[1])
plt.show()
```


    
![png](https://nontapatnon.github.io/python-course-master/md_image_src/output_29_0.png)
    



```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>
      <td>female</td>
      <td>35.0</td>
      <td>1</td>
      <td>0</td>
      <td>113803</td>
      <td>53.1000</td>
      <td>C123</td>
      <td>S</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0</td>
      <td>3</td>
      <td>Allen, Mr. William Henry</td>
      <td>male</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>373450</td>
      <td>8.0500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>886</th>
      <td>887</td>
      <td>0</td>
      <td>2</td>
      <td>Montvila, Rev. Juozas</td>
      <td>male</td>
      <td>27.0</td>
      <td>0</td>
      <td>0</td>
      <td>211536</td>
      <td>13.0000</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>887</th>
      <td>888</td>
      <td>1</td>
      <td>1</td>
      <td>Graham, Miss. Margaret Edith</td>
      <td>female</td>
      <td>19.0</td>
      <td>0</td>
      <td>0</td>
      <td>112053</td>
      <td>30.0000</td>
      <td>B42</td>
      <td>S</td>
    </tr>
    <tr>
      <th>888</th>
      <td>889</td>
      <td>0</td>
      <td>3</td>
      <td>Johnston, Miss. Catherine Helen "Carrie"</td>
      <td>female</td>
      <td>NaN</td>
      <td>1</td>
      <td>2</td>
      <td>W./C. 6607</td>
      <td>23.4500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>889</th>
      <td>890</td>
      <td>1</td>
      <td>1</td>
      <td>Behr, Mr. Karl Howell</td>
      <td>male</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>111369</td>
      <td>30.0000</td>
      <td>C148</td>
      <td>C</td>
    </tr>
    <tr>
      <th>890</th>
      <td>891</td>
      <td>0</td>
      <td>3</td>
      <td>Dooley, Mr. Patrick</td>
      <td>male</td>
      <td>32.0</td>
      <td>0</td>
      <td>0</td>
      <td>370376</td>
      <td>7.7500</td>
      <td>NaN</td>
      <td>Q</td>
    </tr>
  </tbody>
</table>
<p>891 rows × 12 columns</p>
</div>




```python
sns.countplot(df, x="Pclass")
```




    <Axes: xlabel='Pclass', ylabel='count'>




    
![png](https://nontapatnon.github.io/python-course-master/md_image_src/output_31_1.png)
    



```python
sns.countplot(data = df, x="Pclass", hue="Survived")
```




    <Axes: xlabel='Pclass', ylabel='count'>




    
![png](https://nontapatnon.github.io/python-course-master/md_image_src/output_32_1.png)
    



```python
sns.countplot(data = df , x="Pclass", hue="Survived", stat="percent")
```




    <Axes: xlabel='Pclass', ylabel='percent'>




    
![png](https://nontapatnon.github.io/python-course-master/md_image_src/output_33_1.png)
    



```python
df_f = pd.read_csv("https://nontapatnon.github.io/python-course-master/datascience/flight2.csv")
df_f
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>month</th>
      <th>passengers</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1949</td>
      <td>Jan</td>
      <td>112</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1949</td>
      <td>Feb</td>
      <td>118</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1949</td>
      <td>Mar</td>
      <td>132</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1949</td>
      <td>Apr</td>
      <td>129</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1949</td>
      <td>May</td>
      <td>121</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>139</th>
      <td>1960</td>
      <td>Aug</td>
      <td>606</td>
    </tr>
    <tr>
      <th>140</th>
      <td>1960</td>
      <td>Sep</td>
      <td>508</td>
    </tr>
    <tr>
      <th>141</th>
      <td>1960</td>
      <td>Oct</td>
      <td>461</td>
    </tr>
    <tr>
      <th>142</th>
      <td>1960</td>
      <td>Nov</td>
      <td>390</td>
    </tr>
    <tr>
      <th>143</th>
      <td>1960</td>
      <td>Dec</td>
      <td>432</td>
    </tr>
  </tbody>
</table>
<p>144 rows × 3 columns</p>
</div>




```python
df_may = df_f.query("month == 'May'")
sns.lineplot(data = df_may, x = "year", y = "passengers")
```




    <Axes: xlabel='year', ylabel='passengers'>




    
![png](https://nontapatnon.github.io/python-course-master/md_image_src/output_35_1.png)
    



```python
df_wide = df_f.pivot(index = "year", columns = "month", values= "passengers")
df_wide.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>month</th>
      <th>Apr</th>
      <th>Aug</th>
      <th>Dec</th>
      <th>Feb</th>
      <th>Jan</th>
      <th>Jul</th>
      <th>Jun</th>
      <th>Mar</th>
      <th>May</th>
      <th>Nov</th>
      <th>Oct</th>
      <th>Sep</th>
    </tr>
    <tr>
      <th>year</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1949</th>
      <td>129</td>
      <td>148</td>
      <td>118</td>
      <td>118</td>
      <td>112</td>
      <td>148</td>
      <td>135</td>
      <td>132</td>
      <td>121</td>
      <td>104</td>
      <td>119</td>
      <td>136</td>
    </tr>
    <tr>
      <th>1950</th>
      <td>135</td>
      <td>170</td>
      <td>140</td>
      <td>126</td>
      <td>115</td>
      <td>170</td>
      <td>149</td>
      <td>141</td>
      <td>125</td>
      <td>114</td>
      <td>133</td>
      <td>158</td>
    </tr>
    <tr>
      <th>1951</th>
      <td>163</td>
      <td>199</td>
      <td>166</td>
      <td>150</td>
      <td>145</td>
      <td>199</td>
      <td>178</td>
      <td>178</td>
      <td>172</td>
      <td>146</td>
      <td>162</td>
      <td>184</td>
    </tr>
    <tr>
      <th>1952</th>
      <td>181</td>
      <td>242</td>
      <td>194</td>
      <td>180</td>
      <td>171</td>
      <td>230</td>
      <td>218</td>
      <td>193</td>
      <td>183</td>
      <td>172</td>
      <td>191</td>
      <td>209</td>
    </tr>
    <tr>
      <th>1953</th>
      <td>235</td>
      <td>272</td>
      <td>201</td>
      <td>196</td>
      <td>196</td>
      <td>264</td>
      <td>243</td>
      <td>236</td>
      <td>229</td>
      <td>180</td>
      <td>211</td>
      <td>237</td>
    </tr>
  </tbody>
</table>
</div>




```python
sns.lineplot(data= df_wide["May"])
```




    <Axes: xlabel='year', ylabel='May'>




    
![png](https://nontapatnon.github.io/python-course-master/md_image_src/output_37_1.png)
    



```python
sns.lineplot(data = df_wide)
```




    <Axes: xlabel='year'>




    
![png](https://nontapatnon.github.io/python-course-master/md_image_src/output_38_1.png)
    



```python
# df_f
```


```python
sns.lineplot(data=df_f, x="year", y="passengers")
```




    <Axes: xlabel='year', ylabel='passengers'>




    
![png](https://nontapatnon.github.io/python-course-master/md_image_src/output_40_1.png)
    



```python

```

## Pandas - df - Series 


```python
import pandas as pd
```

    C:\Users\Nontapat\AppData\Local\Temp\ipykernel_37024\4080736814.py:1: DeprecationWarning: 
    Pyarrow will become a required dependency of pandas in the next major release of pandas (pandas 3.0),
    (to allow more performant data types, such as the Arrow string type, and better interoperability with other libraries)
    but was not found to be installed on your system.
    If this would cause problems for you,
    please provide us feedback at https://github.com/pandas-dev/pandas/issues/54466
            
      import pandas as pd
    


```python
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# plt.style.use('fivethirtyeight')
import warnings
warnings.filterwarnings('ignore')
%matplotlib inline
```


```python
blood['b'] = "A"
print(blood)
print(blood.is_unique)
blood.unique()
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    Cell In[9], line 1
    ----> 1 blood['b'] = "A"
          2 print(blood)
          3 print(blood.is_unique)
    

    NameError: name 'blood' is not defined



```python
import pandas as pd
s = pd.Series([1,2,3,4,5])

print(s[0])
```


```python
import pandas as pd
#create dataframe using a single list
data = [1,2,3,4,5]
df1 = pd.DataFrame(data)
print(df1)

#create dataframe using a list of lists
data = [['Alice',21],['Bob',22],['Cathy',23]]
df2 = pd.DataFrame(data,columns=['Name','Age'])
df2
```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python
import pandas as pd
blood = pd.Series(["A","B","AB","O"])
# print(blood)
blood
# print("blood has values:",blood.values,"with type",type(blood.values))
# print("blood has index:",blood.index,"with type",type(blood.index))
# print("All blood types", blood.dtype)
# blood[4] = 123
# blood.name="blood";
# print("blood has name:",blood.name)
# blood
```


```python

```


```python

```


```python

```


```python
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# plt.style.use('fivethirtyeight')
import warnings
warnings.filterwarnings('ignore')
%matplotlib inline
```


```python
data = pd.read_csv('https://nontapatnon.github.io/python-course-master/datascience/Titanic-Dataset.csv')
display(data)
```


```python
data[data['Survived']== 0 ][['Name'	,'Sex']]
```


```python
f,ax=plt.subplots(1,2,figsize=(18,8))
data['Survived'].value_counts().plot.pie(explode=[0,0.005],autopct='%1.1f%%',ax=ax[0],shadow=False)
ax[0].set_title('Survived')
ax[0].set_ylabel('')
sns.countplot(x = 'Survived',data=data,ax=ax[1])
ax[1].set_title('Survived')
plt.show()
```


```python
data.groupby(['Sex','Survived'])[['Survived']].count()
```


```python
f,ax=plt.subplots(1,2,figsize=(18,8))
data[['Sex','Survived']].groupby(['Sex']).mean().plot.bar(ax=ax[0])
ax[0].set_title('Survived vs Sex')
sns.countplot(x = 'Sex',hue='Survived',data=data,ax=ax[1])
ax[1].set_title('Sex:Survived vs Dead')
plt.show()
```


```python
f,ax=plt.subplots(1,2,figsize=(20,10))
data[data['Survived']==0].Age.plot.hist(ax=ax[0],bins=20,edgecolor='black',color='red')
ax[0].set_title('Survived= 0')
x1=list(range(0,85,5))
ax[0].set_xticks(x1)
data[data['Survived']==1].Age.plot.hist(ax=ax[1],color='green',bins=20,edgecolor='black')
ax[1].set_title('Survived= 1')
x2=list(range(0,85,5))
ax[1].set_xticks(x2)
plt.show()
```


```python
sns.countplot(data, x="Pclass")
```


```python
sns.countplot(data = data, x="Pclass", hue="Survived")
```


```python
sns.countplot(data = data , x="Pclass", hue="Survived", stat="percent")
```


```python
# https://seaborn.pydata.org/generated/seaborn.lineplot.html
# flights = sns.load_dataset("flights")
# flights.to_csv("flight2.csv", index = False)
# flights.head()

flights  = pd.read_csv("https://nontapatnon.github.io/python-course-master/datascience/flight2.csv")
flights
```


```python
may_flights = flights.query("month == 'May'")
sns.lineplot(data=may_flights, x="year", y="passengers")
```


```python
flights_wide = flights.pivot(index="year", columns="month", values="passengers")
flights_wide.head()
```


```python
sns.lineplot(data=flights_wide["May"])
```


```python
sns.lineplot(data=flights_wide)
```


```python
sns.lineplot(data=flights, x="year", y="passengers")
```


```python
flight2 = pd.read_csv("https://nontapatnon.github.io/python-course-master/datascience/flights.csv")

flight2.head()
```


```python
import pandas as pd
df_new = pd.DataFrame({'col1': [1,2,3] , "col2": [4,5,6]})
df_new.head()
```


```python
import plotly.express as px
import plotly.io as pio
pio.renderers.default = 'iframe'

df = px.data.iris()
df.head()
```


```python
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 size='petal_length', hover_data=['petal_width'])
fig.show()
```


```python
import plotly.express as px
df = px.data.tips()
df.head()
```


```python
df
```


```python
import plotly.express as px
df = px.data.tips()

fig = px.density_heatmap(df, x="total_bill", y="tip", text_auto=True)
fig.show()
```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```
