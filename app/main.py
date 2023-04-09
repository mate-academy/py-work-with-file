def create_report(
    data_file_name: str,
    report_file_name: str
) -> None:
    with (
        open(data_file_name, "r") as file_in,
        open(report_file_name, "w") as file_out
    ):

        supply = 0
        buy = 0

        simple_data = file_in.read().split("\n")
        simpler_data = [data.split(",") for data in simple_data]
        for d_list in simpler_data:
            if d_list == [""]:
                break
            if d_list[0] == "supply":
                supply += int(d_list[1])
            else:
                buy += int(d_list[1])
        result = supply - buy
        file_out.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
