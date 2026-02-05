def create_report(data_file_name: str, report_file_name: str):
    dict_result = {}
    file_data = open(data_file_name)
    for line in file.readlines()
        dic_result.[line.split(",")[0]] += line.split(",")[1]
    file_data.close()  
    file_report = open(report_file_name, "w")
    for key, value in dic_result.items():
        file_report.write(f"{key},{value})
    file_report.close()
