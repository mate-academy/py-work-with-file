def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    with (
        open(data_file_name, "r") as data_csv,
        open(report_file_name, "w") as report
    ):
        result = {}
        for data in [data.split(",") for data in data_csv.read().split()]:
            if data[0] not in result.keys():
                result[data[0]] = int(data[1])
                continue
            result[data[0]] += int(data[1])
        else:
            result["result"] = result["supply"] - result["buy"]

        report.write(f"supply,{result['supply']}\n")
        report.write(f"buy,{result['buy']}\n")
        report.write(f"result,{result['result']}\n")
