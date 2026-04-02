# Work with files 

Implement function `create_report` 
which will make a report using data from the market after a working day. 

- Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before start

This method has two parameters:
- `data_file_name: str` - you should read data from this file
- `report_file_name: str` - you should write the result to this file

Input file has `.csv` format. CSV is a simple file format used to store tabular data.
This type of file is very popular for storing information. So we will start working on it. 
CSV stands for "comma-separated values". Its data fields are most often separated or delimited by a comma. 

For example, let's say you had a spreadsheet containing the following data:

    | operation type | amount  | 
| :------------: | :-------:|
| supply         | 30       | 
| buy            | 10       | 
| buy            | 13       | 
| supply         | 17       | 
| buy            | 10       | 

The above data could be represented in a CSV-formatted file as follows:
```csv
supply,30
buy,10
buy,13
supply,17
buy,10
```

__Your task is to read all data from the input csv file, 
create a report and write it to the new file (the name of this file is the second parameter of the method).__

Example of the report:
```csv
supply,47
buy,33
result,14
```

Explanation:
- `supply = 30 + 17 = 47`
- `buy = 10 + 13 + 10 = 33`
- `result = supply - buy = 47 - 33 = 14`

Note:

The last line of the file may be empty and should not be processed

Please use terminal here to run script/tests, to avoid file path errors
