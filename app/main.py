def create_report(data_file_name: str, report_file_name: str):
    with open(f"{data_file_name}", "r") as file_in, \
            open(f"{report_file_name}", "a") as file_out:
        suppy_list = []
        buy_list = []
        for line in file_in:
            temp_line = line.split(",")
            if temp_line[0] == "supply":
                suppy_list.append(int(temp_line[1]))
            else:
                buy_list.append(int(temp_line[1]))
        file_out.write(f"supply,{sum(suppy_list)}\n"
                       f"buy,{sum(buy_list)}\n"
                       f"result,{sum(suppy_list) - sum(buy_list)}\n")
