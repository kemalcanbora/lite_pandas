import pandas as pd
from minimalist_dataframe import MinimalistDataframe

data = [['alex', 10, "M"],['bob', 12, "M"],['clarke', 13, "F"],
        ["mario", 12, "M"],['robinho', 10, "M"],['ronaldo', 12, "M"],
        ['lore', 13, "F"],["kore", 12, "M"],
        ['vuko', 10, "M"],['bobi', 12, "M"],['koke', 13, "F"],
        ["python", 12, "M"]]

## Create Dataframe
df = pd.DataFrame(data, columns=['Name', 'Age', "sex"])
md = MinimalistDataframe(dataframe=df)

## Get column values
f1 = md.get_column_values(column_name="Name")
print(f1)

## Get spesific rows
f2 = md.get_spesific_rows(column_name="Age",value=10,logic="eq")
print(f2)

## select_some_row
f3 = md.select_some_row(select_index_column="Name",selected_column_sought=["alex","robinho"])
print(f3)