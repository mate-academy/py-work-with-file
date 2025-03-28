def create_report(data_file_name: str, report_file_name: str) -> None:
    temporary_storage = {}
    with open(data_file_name, "r") as file_in:
        for line in file_in.readlines():
            line = line.split(",")
            if line[0] in temporary_storage.keys():
                temporary_storage[line[0]] += int(line[1])
            else:
                temporary_storage[line[0]] = int(line[1])
    with open(report_file_name, "w") as report:
        supply = temporary_storage["supply"]
        buy = temporary_storage["buy"]
        report.write(f"supply,{str(supply)}\n")
        report.write(f"buy,{str(buy)}\n")
        report.write(
            f"result,{str(int(supply) - int(buy))}\n"
        )
