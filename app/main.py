def create_report(data_file_name: str, report_file_name: str) -> None:
    with (
        open(data_file_name, "r") as source_file,
        open(report_file_name, "w") as report_file,
    ):
        data = {"supply": 0, "buy": 0}
        for line in source_file.readlines():
            key, value = line.split(",")
            data[key] += int(value)
        data["result"] = data["supply"] - data["buy"]

        result = "\n".join([f"{key},{value}" for key, value in data.items()])
        report_file.write(result + "\n")
