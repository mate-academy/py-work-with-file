def create_report(data_file_name: str, report_file_name: str) -> None:
    totals_dict = {"supply": 0, "buy": 0}
    try:
        with open(data_file_name, "r") as input_file:
            for line in input_file:
                line = line.strip()
                if not line:
                    continue

                try:
                    operation_type, amount = line.split(",")
                    totals_dict[operation_type] += int(amount)

                except ValueError:
                    continue

    except FileNotFoundError:
        raise FileNotFoundError(f"File {data_file_name} not found!")

    result = totals_dict["supply"] - totals_dict["buy"]

    try:
        with open(report_file_name, "w") as output_file:
            output_file.write(f"supply,{totals_dict['supply']}\n")
            output_file.write(f"buy,{totals_dict['buy']}\n")
            output_file.write(f"result,{result}\n")

    except OSError:
        raise OSError(f"Cannot write to file {report_file_name}!")
