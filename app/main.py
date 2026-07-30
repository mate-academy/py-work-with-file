def create_report(data_file_name: str, report_file_name: str):

    with open(data_file_name, "r") as data:
        trade = data.readlines()
        supply = 0
        buy = 0

        for line in trade:
            value = int(line.split(",")[1])
            if line.split(",")[0] == "supply":
                supply += value
            else:
                buy += value

        with open(report_file_name, "w") as report:
            report.write(f"supply,{supply}\n"
                         f"buy,{buy}\n"
                         f"result,{supply - buy}\n")
