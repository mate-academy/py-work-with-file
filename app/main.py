def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as source, open(
        report_file_name, "a"
    ) as report:
        source_data = [
            (data.split(",")[0], int(data.split(",")[1]))
            for data in [
                line.replace("\n", "") for line in source.readlines()
            ]
        ]
        report_data = {"supply": 0, "buy": 0, "result": 0}
        print(source_data)
        for pair in source_data:
            if pair[0] not in report_data.keys():
                report_data[pair[0]] = pair[1]
            else:
                report_data[pair[0]] += pair[1]
        report_data["result"] = (
            report_data["supply"] - report_data["buy"]
        )
        final_result = "".join(f"{k},{v}\n" for k, v in report_data.items())
        report.write(final_result)
