import pandas
excel_files=['sample1.xlsx', 'sample2.xlsx', 'sample3.xlsx', 'sample4.xlsx']
combine=pandas.DataFrame()

for file in excel_files:
    df=pandas.read_excel(file, skiprows=4)
    combine=combine.append(df, ignore_index=True)

combine.to_excel('Combined.xlsx')