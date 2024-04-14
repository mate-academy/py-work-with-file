def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r") as f1,
          open(report_file_name, "w") as f2):
        data_dict = {}
        for line in f1:
            if "," in line:
                operation, amount = line.split(",")
                amount = int(amount)
                if data_dict.get(operation):
                    data_dict[operation] += amount
                else:
                    data_dict[operation] = amount
        supply = data_dict["supply"]
        buy = data_dict["buy"]
        result = supply - buy
        f2.write("supply," + str(supply) + "\n")
        f2.write("buy," + str(buy) + "\n")
        f2.write("result," + str(result) + "\n")
