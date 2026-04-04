def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as current_file:
        lines = [line[:-1].split(",") for line in current_file]
        result = {}

        for operation, amount in lines:
            if operation in result:
                result[operation] += int(amount)
            else:
                result[operation] = int(amount)

        result["result"] = result.get("supply") - result.get("buy")
        result_for_file = (f"supply,{result['supply']}\n"
                           f"buy,{result['buy']}\n"
                           f"result,{result['result']}\n")

        with open(report_file_name, "w") as report:
            report.write(result_for_file)
