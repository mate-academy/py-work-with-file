def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:

    operations = {"supply": 0, "buy": 0}

    with open(data_file_name, "r") as file_in:
        for row in file_in:

            row_list = row.split(",")
            operation = row_list[0]
            amount = int(row_list[1])

            if operation in operations:
                operations[operation] += amount

    result = operations["supply"] - operations["buy"]

    with open(report_file_name, "w") as file_out:
        file_out.write(f"supply,{operations['supply']}\n")
        file_out.write(f"buy,{operations['buy']}\n")
        file_out.write(f"result,{result}\n")
