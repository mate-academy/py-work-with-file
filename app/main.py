
def create_report(data_file_name: str, report_file_name: str) -> None:
    data = {"supply":0, "buy":0}
    read_file = open(data_file_name, "r")
    for line in read_file.readlines():
        operation_type = line.split(",")[0]
        amount = int(line.split(",")[1])
        data[operation_type] += amount
    read_file.close()

    write_file = open(report_file_name, "w")
    write_file.write(f"supply,{data['supply']}\n")
    write_file.write(f"buy,{data['buy']}\n")
    write_file.write(f"result,{data['supply'] - data['buy']}\n")
    write_file.close()
