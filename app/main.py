def create_report(data_file_name: str, report_file_name: str) -> None:
    with (
        open(data_file_name, "r") as file_in,
        open(report_file_name, "w") as file_out
    ):
        text = [t.replace("\n", "").split(",") for t in file_in.readlines()]
        supply = 0
        buy = 0
        for element in text:
            if element[0] == "supply":
                supply += int(element[1])
            if element[0] == "buy":
                buy += int(element[1])
        result = supply - buy
        file_out.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
