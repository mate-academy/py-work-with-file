def create_report(data_file_name: str, report_file_name: str) -> None:
    result = {}

    with (open(data_file_name) as data_file):
        for line in data_file:
            type_info, amount = line.split(",")
            result[type_info] = result.get(type_info, 0) + int(amount)
    difference = result["supply"] - result["buy"]

    with open(report_file_name, "a") as report_file:
        report_file.write("supply," + str(result["supply"]) + "\n")
        report_file.write("buy," + str(result["buy"]) + "\n")
        report_file.write("result," + str(difference) + "\n")
