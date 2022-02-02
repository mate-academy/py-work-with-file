def create_report(data_file_name: str, report_file_name: str):
    supply = 0
    buy = 0
    with open(data_file_name, 'r') as filein:
        for line in filein:
            items = line.split(",")
            if len(items) > 0 and items[0] == 'supply':
                supply += int(items[1])
            elif len(items) > 0 and items[0] == 'buy':
                buy += int(items[1])
    result = supply - buy
    dict_result = {"supply": supply, "buy": buy, "result": result}
    with open(report_file_name, 'w') as fileout:
        for name, value in dict_result.items():
            fileout.writelines(f'{str(name)},' + str(value) + '\n')
