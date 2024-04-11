def create_report(data_file_name: str, report_file_name: str) -> None:
    operations = {"supply": 0, "buy": 0}
    with open(data_file_name, "r") as input_file:
        for line in input_file.readlines():
            line_mapped = line.split(",")
            if len(line_mapped) == 2:
                line_mapped[1] = line_mapped[1][:-1]
                if line_mapped[0] == "supply":
                    operations["supply"] += int(line_mapped[1])
                elif line_mapped[0] == "buy":
                    operations["buy"] += int(line_mapped[1])
    operations["result"] = operations["supply"] - operations["buy"]

    with open(report_file_name, "w") as out_file:
        for operation, amount in operations.items():
            out_file.write(f"{operation},{amount}\n")


# create_report("grapes.csv", "report.csv")
