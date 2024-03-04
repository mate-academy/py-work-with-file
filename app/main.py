def create_report(data_file_name: str, report_file_name: str):
    buy_result = 0
    supply_result = 0

    with open(data_file_name, 'r') as file:
        for information in file:
            information = list(information.split(','))
            if information[0] == 'supply':
                supply_result += int(information[1])
            if information[0] == 'buy':
                buy_result += int(information[1])

    with open(report_file_name, 'w') as file_report:
        file_report.write(f'supply,{supply_result}\n'
                          f'buy,{buy_result}\n'
                          f'result,{supply_result - buy_result}\n')
