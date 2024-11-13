def create_report(data_file_name: str, report_file_name: str) -> None:
    dictionary_spreadsheet = {}
    with open(data_file_name, "r") as data_file:
        for line in data_file:
            data_type = line.split(",")[0]
            amount = int(line.split(",")[1].replace("\n", ""))
            if data_type not in dictionary_spreadsheet:
                dictionary_spreadsheet[data_type] = amount
            else:
                dictionary_spreadsheet[data_type] += amount
    result = dictionary_spreadsheet["supply"] - dictionary_spreadsheet["buy"]
    dictionary_spreadsheet["result"] = result
    with open(report_file_name, "w") as report_file:
        for key, value in dictionary_spreadsheet.items():
            report_file.write(f"{key},{value}\n")
