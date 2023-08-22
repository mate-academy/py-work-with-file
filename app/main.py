def create_report(data_file_name: str, report_file_name: str) -> None:
    sum_supply = 0
    sum_buy = 0
    with (open(data_file_name, "r") as file_in,
          open(report_file_name, "w") as file_out):
        data = file_in.read()
        lines = data.split("\n")
        for line in lines:
            line = line.replace("\n", "")
            line_list = line.split(",")
            if line_list[0] == "supply":
                sum_supply += int(line_list[1])
            if line_list[0] == "buy":
                sum_buy += int(line_list[1])
        file_out.write(f"supply,{sum_supply}\n")
        file_out.write(f"buy,{sum_buy}\n")
        file_out.write(f"result,{sum_supply - sum_buy}\n")
