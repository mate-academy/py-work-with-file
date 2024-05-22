def create_report(data_file_name: str, report_file_name: str) -> None:
    data_dict = {"supply": 0, "buy": 0}
    with (open(data_file_name, "r") as file,
          open(report_file_name, "w") as report):
        for line in file:
            parts = line.strip().split(",")
            print(parts)
            if len(parts) != 2:
                continue
            operation = parts[0]
            amount = int(parts[1])
            if operation == "supply":
                data_dict["supply"] += amount
            if operation == "buy":
                data_dict["buy"] += amount
        report.write("supply," + str(data_dict["supply"]) + "\n")
        report.write("buy," + str(data_dict["buy"]) + "\n")
        report.write("result," + str(data_dict["supply"]
                                     - data_dict["buy"]) + "\n")
