def create_report(data_file_name: str, report_file_name: str):

    with open(data_file_name, "r") as data:
        trade = data.readlines()
        supply = 0
        buy = 0

        for line in trade:
            if line.split(",")[0] == "supply":
                supply += int(line.split(",")[1])
            else:
                buy += int(line.split(",")[1])

        with open(report_file_name, "w") as report:
            report.write(f"supply,{supply}\n"
                         f"buy,{buy}\n"
                         f"result,{supply - buy}\n")
