#check my code here

def create_report(data_file_name: str, report_file_name: str):
    dict_data = {}

    with open(data_file_name, 'r') as file:
        for line in file:
            key, value = line.strip().split(',')
            dict_data[key] = dict_data.get(key, 0) + int(value)

    with open(report_file_name, 'w') as file:
        for key, value in dict_data.items():
            file.write(f"{key},{value}\n")



    
