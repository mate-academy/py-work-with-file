import os


def create_report(data_file_name: str, report_file_name: str) -> None:
    if not os.path.exists(data_file_name):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        root_path = os.path.join(base_dir, data_file_name)

        if os.path.exists(root_path):
            data_file_name = root_path

    total_supply = 0
    total_buy = 0

    with open(data_file_name, 'r') as data_file:
        for line in data_file:
            stripped_line = line.strip()
            if not stripped_line:
                continue
            parts = stripped_line.split(',')
            if len(parts) < 2:
                continue

            operation = parts[0].strip()
            amount = parts[1].strip()

            if operation == 'supply':
                total_supply += int(amount)
            elif operation == 'buy':
                total_buy += int(amount)

    result = total_supply - total_buy

    with open(report_file_name, 'w') as report_file:
        report_file.write(f"supply,{total_supply}\n")
        report_file.write(f"buy,{total_buy}\n")
        report_file.write(f"result,{result}\n")