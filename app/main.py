def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r") as data_file,
            open(report_file_name, "w") as result_file):
        result = {}
        data = data_file.read().split("\n")

        for line in data:
            if not line:
                break
            operation, amount = line.split(",")
            result[operation] = result.get(operation, 0) + int(amount)

        result_file.write("supply," + str(result["supply"]) + "\n")
        result_file.write("buy," + str(result["buy"]) + "\n")
        result_file.write(
            "result," + str(result["supply"] - result["buy"]) + "\n"
        )
