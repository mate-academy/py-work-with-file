def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name) as data_file:
        data = {}
        for line in data_file:
            key, value = line.split(",")
            if key in data:
                data[key] += int(value.strip())
            else:
                data[key] = int(value.strip())
        result = data["supply"] - data["buy"]
    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{data['supply']}\n")
        report_file.write(f"buy,{data['buy']}\n")
        report_file.write(f"result,{result}\n")


if __name__ == "__main__":
    create_report(data_file_name="data1.csv", report_file_name="report.csv")
