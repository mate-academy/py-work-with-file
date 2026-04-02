def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r") as source,
          open(report_file_name, "w")as result):
        supply = 0
        buy = 0

        for line in source:
            info = line.strip().split(",")

            if info[0] == "supply":
                supply += int(info[1])
            elif info[0] == "buy":
                buy += int(info[1])

        result.write("supply," + str(supply) + "\n")
        result.write("buy," + str(buy) + "\n")
        result.write("result," + str(supply - buy) + "\n")
