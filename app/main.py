def create_report(data_file_name: str, report_file_name: str):
    with open(data_file_name, "r") as file:
        file_list = file.readlines()

    sum_supply, sum_buy = 0, 0
    for line in file_list:
        line = line.strip().split(',')
        if 'supply' in line:
            sum_supply += int(line[1])
        elif "buy" in line:
            sum_buy += int(line[1])

    result_data = [
        f"supply,{sum_supply}\n",
        f"buy,{sum_buy}\n"
        f"result,{sum_supply - sum_buy}\n"
    ]

    with open(report_file_name, "w") as wfile:
        wfile.writelines(result_data)
