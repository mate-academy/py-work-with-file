def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:

    supply, buy = 0, 0
    with (open(data_file_name, "r") as data_file,
          open(report_file_name, "w") as report_file):
        temp_list = data_file.read().split("\n")
        print(temp_list)
        for line in temp_list:
            if "supply" in line:
                supply += int(line.replace("supply,", ""))
            if "buy" in line:
                buy += int(line.replace("buy,", ""))
        report_file.write(f"supply,{supply}\n"
                          f"buy,{buy}\n"
                          f"result,{supply - buy}\n")
