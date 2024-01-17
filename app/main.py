def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    supply = 0
    buy = 0
    with (open(data_file_name, "r") as file_in,
          open(report_file_name, "w") as file_out):
        for row in file_in.readlines():
            str_row_into_list = row.split(",")
            data, value = str_row_into_list[0], str_row_into_list[1]
            if data == "supply":
                supply += int(value)
            else:
                buy += int(value)
        result = supply - buy
        file_out.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
