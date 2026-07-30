def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r") as in_f,
          open(report_file_name, "a") as out_f):
        in_lines = in_f.readlines()
        supply = []
        buy = []
        for line in in_lines:
            split_line = line.split(",")
            if split_line[0] == "supply":
                supply.append(int(split_line[1]))
            if split_line[0] == "buy":
                buy.append(int(split_line[1]))
        sum_supply = sum(supply)
        sum_buy = sum(buy)
        result = sum_supply - sum_buy
        out_f.write(f"supply,{sum_supply}\n")
        out_f.write(f"buy,{sum_buy}\n")
        out_f.write(f"result,{result}\n")
