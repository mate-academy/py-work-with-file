def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as data_file:
        for line in data_file.readlines():
            match(line.split(",")[0]):
                case "supply":
                    supply += int(line.split(",")[1])
                case "buy":
                    buy += int(line.split(",")[1])

    with open(report_file_name, "x") as report_file:
        report_file.write(f"supply,{supply}\n")
        report_file.write(f"buy,{buy}\n")
        report_file.write(f"result,{supply-buy}\n")
