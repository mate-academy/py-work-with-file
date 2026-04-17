def create_report(data_file_name: str, report_file_name: str) -> str:
    data_file = open(data_file_name, "r")
    supply = 0
    buy = 0
    for line in data_file.readlines():
        line = line.strip()
        if line == "":
            pass
        else:
            operation, amount = line.split(",")
            if operation == "supply":
                supply += int(amount)
            else:
                buy += int(amount)
    result = supply - buy
    result_file = open(report_file_name, "w")
    result_file.write(f"supply,{supply}\n")
    result_file.write(f"buy,{buy}\n")
    result_file.write(f"result,{result}\n")
    data_file.close()
    result_file.close()
