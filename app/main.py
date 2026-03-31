def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(
        data_file_name,
        "r",
    ) as source, open(report_file_name, "w") as report_file:
        results = {"supply": 0, "buy": 0, "result": 0}
        for line in source.readlines():
            operation = line.split(",")
            results[operation[0]] += int(operation[1].strip())
        results["result"] = results["supply"] - results["buy"]

        for key, value in results.items():
            report_file.write(f"{key},{value}\n")
