import pandas as pd


df = pd.read_csv("insuranceRoundedBmiClean.csv")

test = {'Name': ['John', 'Alice', 'Bob'],
        'Age': [25, 30, 22],
        'City': ['New York', 'San Francisco', 'Los Angeles']}
df = pd.DataFrame(test)

#make data element
columns = df.columns.tolist()
rest_data = df.values.tolist()

data_element = [columns] + rest_data

#make atributes element
attributes_element = [{'field': column, 'type': str(df.dtypes[column])} for column in columns]

data = {"data": data_element, "attributes": attributes_element, "privacyModels" : None, "suppressionLimit" : None}

print(data)


