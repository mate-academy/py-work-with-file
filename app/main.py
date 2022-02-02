def create_report(data_file_name: str, report_file_name: str):
    sum_supply = 0
    sum_buy = 0
    with open(data_file_name, 'r') as file:
        for line in file.readlines():
            line = line.strip().split(',')
            if line[0] == "supply":
                sum_supply += int(line[1])
            elif line[0] == "buy":
                sum_buy += int(line[1])

    with open(report_file_name, 'w') as new_file:
        new_file.writelines(f"supply,{sum_supply}\n")
        new_file.writelines(f"buy,{sum_buy}\n")
        new_file.writelines(f"result,{sum_supply - sum_buy}\n")
