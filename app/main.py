def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    with open(data_file_name, "r") as data_file:
        data_list = []
        data = data_file.readline()
        while data:
            data_list.append(data.strip().split(","))
            data = data_file.readline()

        supply_res = 0
        buy_res = 0
        for row in data_list:
            if row[0] == "supply":
                supply_res += int(row[1])

            if row[0] == "buy":
                buy_res += int(row[1])

        with open(report_file_name, "w") as report_file:
            report_file.write(
                f"supply,{supply_res}\n"
                + f"buy,{buy_res}\n"
                + f"result,{supply_res - buy_res}\n"
            )
