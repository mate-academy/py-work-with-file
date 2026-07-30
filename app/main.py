def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data, \
            open(report_file_name, "w") as report:
        buy = supply = 0
        for line in data:
            line = line.split(",")
            value = int(line[1])
            match line[0]:
                case "buy":
                    buy += value
                case "supply":
                    supply += value

        report.write(
            f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n"
        )
