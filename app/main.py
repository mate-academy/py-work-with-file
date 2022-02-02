def create_report(data_file_name: str, report_file_name: str):
    with open(data_file_name, "r") as data:
        lines = data.readlines()
        result = {
            "supply": 0,
            "buy": 0
        }
        for line in lines:
            if len(line) > 2:
                split_line = line.strip("\n").split(",")
                result[split_line[0]] += int(split_line[1])

        result["result"] = result["supply"] - result["buy"]

        with open(report_file_name, "w") as report:
            for key, value in result.items():
                report.write(f"{key},{value}\n")
