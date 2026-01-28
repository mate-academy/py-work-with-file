def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    file_read = open(data_file_name, "r")
    total = {}
    for line in file_read.readlines():
        line.strip().strip("\n")
        if line != "":
            operation_amount = line.split(",")
            if len(operation_amount) == 2:
                total[operation_amount[0]] += int(operation_amount[1])
    total["result"] = total["supply"] - total["buy"]
    file_write = open(report_file_name, "w")
    for key, value in total.items():
        file_write.write(f"{key},{value}\n")
    file_read.close()
    file_write.close()
