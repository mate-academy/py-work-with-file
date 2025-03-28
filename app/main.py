def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as file_in, \
            open(report_file_name, "a") as file_out:

        for line in file_in:
            split_line = line.split(",")

            if split_line[0] == "supply":
                supply += int(split_line[1])

            elif split_line[0] == "buy":
                buy += int(split_line[1])

        result = supply - buy

        file_out.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
