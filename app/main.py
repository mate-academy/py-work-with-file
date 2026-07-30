def create_report(data_file_name: str,
                  report_file_name: str) -> None:
    sup = 0
    buy = 0
    with (open(data_file_name, "r") as file_in,
          open(report_file_name, "w") as file_out):
        for line in file_in:
            line_lst = line.split(",")
            if line_lst[0] == "supply":
                sup += int(line_lst[1])
            elif line_lst[0] == "buy":
                buy += int(line_lst[1])
        res = sup - buy
        file_out.write(f"supply,{sup}\nbuy,{buy}\nresult,{res}\n")
