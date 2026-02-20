def create_report(data_file_name: str, report_file_name: str) -> None:
    sum_supply = 0
    sum_buy = 0
    data_file = open(data_file_name)
    for line in data_file.readlines():
        index = line.find(",")
        value = int(line[index + 1:])

        if line[0] == "s":
            sum_supply += value
        else:
            sum_buy += value
    result = sum_supply - sum_buy
    data_file.close()

    report_file = open(report_file_name, "w")
    report_file.write(f"supply,{int(sum_supply)}\n")
    report_file.write(f"buy,{int(sum_buy)}\n")
    report_file.write(f"result,{int(result)}\n")
    report_file.close()
