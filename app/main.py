def create_report(data_file_name: str, report_file_name: str):
    supply_total = 0
    buy_total = 0

    with open(data_file_name, 'r') as data_file:
        for line in data_file:
            line = line.strip()
            if not line:
                continue  # Pomijamy puste linie
            operation, amount_str = line.split(',')
            amount = int(amount_str)
            if operation == 'supply':
                supply_total += amount
            elif operation == 'buy':
                buy_total += amount

    result = supply_total - buy_total

    with open(report_file_name, 'w') as report_file:
        report_file.write(f'supply,{supply_total}\n')
        report_file.write(f'buy,{buy_total}\n')
        report_file.write(f'result,{result}\n')

# write your code here
