import pandas as pd

dosya_data = pd.read_csv("veri.csv")
print(dosya_data)
dosya_data.info()




dosya_data = pd.read_csv("veri.csv")


numeric_columns = dosya_data.select_dtypes(include=['int64', 'float64']).columns
num_cols = len(numeric_columns)

print("Sayısal sütun sayısı:", num_cols)
import os
print("Dosya Boyutu(Byte)")
print(os.path.getsize('veri.csv'))

