def create_report(data_file_name: str, report_file_name: str) -> None:
    result_dict = {"supply": 0, "buy": 0}

    try:
        with open(data_file_name, "r") as data_file:
            for line in data_file:
                line = line.strip()

                if not line:
                    continue

                operation, amount = line.split(",")

                if operation == "supply":
                    result_dict["supply"] += int(amount)
                elif operation == "buy":
                    result_dict["buy"] += int(amount)

        result = result_dict["supply"] - result_dict["buy"]

        with open(report_file_name, "w") as report_file:
            report_file.write(f"supply,{result_dict['supply']}\n")
            report_file.write(f"buy,{result_dict['buy']}\n")
            report_file.write(f"result,{result}\n")

    except FileNotFoundError:
        return
