def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r") as input_file,
          open(report_file_name, "w") as output_file):
        supply = 0
        buy = 0
        input_list = input_file.read().replace(",", " ").split()
        for index, value in enumerate(input_list):
            if value == "supply":
                supply += int(input_list[index + 1])
            elif value == "buy":
                buy += int(input_list[index + 1])
        result = supply - buy
        output_file.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
