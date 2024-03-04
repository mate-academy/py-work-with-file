def create_report(data_file_name: str, report_file_name: str) -> None:
    result = {
        'supply': 0,
        'buy': 0,
    }

    with open(data_file_name, "r") as read_file, \
         open(report_file_name, "w") as write_file:
        for line in read_file:
            data = line.replace("\n", "").split(",")

            if data[0] in result:
                result[data[0]] += int(data[1])

        for operation_type, amount in result.items():
            write_file.write(f"{operation_type},{amount}\n")

        write_file.write(f"result,{result['supply'] - result['buy']}\n")
