def create_report(data_file_name: str,
                  report_file_name: str) -> None:
    file_1 = f"{data_file_name}"
    file_2 = f"{report_file_name}"
    with open(file_1, "r") as data, open(file_2, "w") as report:
        buy = 0
        supply = 0
        for line in data.readlines():
            action = line.rstrip("\n").split(",")
            if action[0] == "supply":
                supply += int(action[1])
            if action[0] == "buy":
                buy += int(action[1])
        result = supply - buy
        report.write(f"supply,{supply}\n"
                     f"buy,{buy}\n"
                     f"result,{result}\n")


# all tests pass, but on practice we need to use data file names in
# following format:
# "../apples.csv"
