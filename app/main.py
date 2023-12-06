def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r") as file,
          open(report_file_name, "w") as result_file):
        supply, buy, = [], []
        for string in file:
            arg = string.split(",")
            if arg[0] == "supply":
                supply.append(arg[1].strip())
            elif arg[0] == "buy":
                buy.append(arg[1].strip())
        sum_suply = sum([int(i) for i in supply])
        sum_buy = sum([int(i) for i in buy])
        result_file.write(f"supply,{sum_suply}\n")
        result_file.write(f"buy,{sum_buy}\n")
        result_file.write(f"result,{sum_suply - sum_buy}\n")
