def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r")
          as file_in, open(report_file_name, "w") as file_out):
        supply, buy = 0, 0
        for line in file_in.readlines():
            split_line = line.split(",")
            if split_line[0] == "supply":
                supply += int(split_line[1])
            else:
                buy += int(split_line[1])
        file_out.write(
            f"supply, {supply}\n"
            f"buy, {buy}\n"
            f"result, {supply - buy}\n"
            .replace(" ", "")
        )
