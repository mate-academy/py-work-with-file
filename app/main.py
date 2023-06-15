def create_report(data_file_name: str, report_file_name: str) -> None:
    suply = 0
    buy = 0
    with (open(data_file_name, "r") as file_1,
          open(report_file_name, "a") as file_2):

        for line in file_1.readlines():
            save_line = line.split(",")
            if save_line[0] == "supply":
                suply += int(save_line[1])
            elif save_line[0] == "buy":
                buy += int(save_line[1])

        file_2.write(f"supply,{suply}\n")
        file_2.write(f"buy,{buy}\n")
        file_2.write(f"result,{suply - buy}\n")
