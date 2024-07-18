---
layout: page
title: 03 Data Science
---

| Tables        | Are           | Cool   |
| ------------- |:-------------:| -----: |
| col 3 is      | right-aligned | 53231฿ |
| col 2 is      | centered      |   399฿ |
| zebra stripes | are neat      |    33฿ |


# Pandas

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Series
```
import pandas as pd
series = pd.Series(["A","B","AB","O"])
series[4] = "O-"
print(series)
```

## DataFrame
```
import pandas as pd
data  = [1,2,3,4,5]
df1 = pd.DataFrame(data)
# display(df1)

data = [['Alice', 21], ['Bob', 22], ['Cathy', 23]]
df2 = pd.DataFrame(data, columns = ["Name", "Age"])
df2
```
Output:

| Name        | Age           |
| ----------- |:-------------:|
| Alice       | 21            |
| Bob         | 22            |
| Cathy       | 23            |

```
d = {'name' : pd.Series(['Alice','Bob','Cathy','Dave']),
    'Age': pd.Series([21,22,23,24]),
    'Score' : pd.Series([80,85,90,95])}

df3 = pd.DataFrame(d)
df3
```
Output:
| Name        | Age           | SCore        |
| ----------- |:-------------:|-------------:|
| Alice       | 21            | 80           |
| Bob         | 22            | 85           |
| Cathy       | 23            | 90           |
| Dave        | 24            | 95           |

`df3.info()`




## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.


Thanks for reading!
