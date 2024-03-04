def create_report(data_file_name: str, report_file_name: str) -> None:
    result = {
        'supply': 0,
        'buy': 0,
    }

    with open(data_file_name, "r") as file, \
         open(report_file_name, "w") as final_file:
        for line in file:
            data = line.replace("\n", "").split(",")

            if data[0] in result:
                result[data[0]] += int(data[1])

        for operation_type, amount in result.items():
            final_file.write(f"{operation_type},{amount}\n")

        final_file.write(f"result,{result['supply'] - result['buy']}\n")
