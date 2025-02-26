def create_report(data_file_name: str, report_file_name: str):
    total_supply = 0
    total_buy = 0

    file = open(data_file_name, 'r')

    for line in file:
        line = line.strip()

        if line:
            line = line.split(',')

            if line[0] == 'supply':
                total_supply += int(line[1])
            elif line[0] == 'buy':
                total_buy += int(line[1])

    file.close()

    result = total_supply - total_buy

    file = open(report_file_name, "w")
    file.write(f"supply,{total_supply}\n")
    file.write(f"buy,{total_buy}\n")
    file.write(f"result,{result}\n")

    file.close()
