def create_report(data_file_name: str, report_file_name: str):
    with open(data_file_name, "r") as data_file,\
            open(report_file_name, "w") as report_file:
        supply = []
        buy = []

        for line in data_file.readlines():
            if line.startswith("supply"):
                supply.append(int(line.split(",")[1]))
            if line.startswith("buy"):
                buy.append(int(line.split(",")[1]))

            result = sum(supply) - sum(buy)

        report_file.write(f"supply,{sum(supply)}\n"
                          f"buy,{sum(buy)}\n"
                          f"result,{result}\n")
