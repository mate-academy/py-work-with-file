def create_report(data_file_name: str, report_file_name: str):
    dict_data = {}

    with open(data_file_name, 'r') as file:
        for line in file:
            key, value = line.strip().split(',')
            dict_data[key] = dict_data.get(key, 0) + int(value)

        dict_data['result'] = int(dict_data['supply']) - int(dict_data['buy'])

    with open(report_file_name, 'w') as file:
        for key, value in dict_data.items():
            file.write(f"{key},{value}\n")



    
