def create_report(data_file_name: str, report_file_name: str):
    with open(data_file_name, "r") as file_in, \
            open(report_file_name, "w") as file_out:
        text = file_in.read()
        text = text.split("\n")
        supply_sum = 0
        buy_sum = 0
        for i in text:
            i = i.split(",")
            if i[0] == "supply":
                supply_sum += int(i[1])
            if i[0] == "buy":
                buy_sum += int(i[1])
        report = f"supply,{supply_sum}\n" \
                 f"buy,{buy_sum}\n" \
                 f"result,{supply_sum - buy_sum}\n"
        file_out.write(report)
