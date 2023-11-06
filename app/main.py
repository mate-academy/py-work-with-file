def create_report(data_file_name: str, report_file_name: str) -> None:
    csv_data = {"supply": 0, "buy": 0}

    with (open(data_file_name, "r") as data_file,
          open(report_file_name, "w") as report_file):
        for line in data_file:
            data = line.strip().split(",")

            csv_data[data[0]] += int(data[1])

        for key, value in csv_data.items():
            report_file.write(f"{key},{value}\n")

        result = csv_data["supply"] - csv_data["buy"]
        report_file.write(f"result,{result}")
