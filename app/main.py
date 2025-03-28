def create_report(data_file_name: str,
                  report_file_name: str
                  ) -> None:
    with open(data_file_name, "r") as file_in, \
            open(report_file_name, "w") as file_out:
        text = file_in.read()
        supply_sum = 0
        buy_sum = 0
        for line in text.split("\n"):
            if "supply" in line:
                supply_sum += int(line.split(",")[1])
            if "buy" in line:
                buy_sum += int(line.split(",")[1])
        total_result = supply_sum - buy_sum
        text_out = f"supply,{supply_sum} buy,{buy_sum} result,{total_result}"
        for line in text_out.split():
            file_out.write(line + "\n")
