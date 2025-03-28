def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as input_file:
        all_data_as_str = input_file.read()

    all_data_as_str = all_data_as_str.replace("\n", " ")
    all_data_as_str = all_data_as_str.replace(",", " ")
    arr_all_data = all_data_as_str.split()
    supply = 0
    buy = 0

    for i in range(0, len(arr_all_data) - 1, 2):
        if arr_all_data[i] == "supply":
            supply += int(arr_all_data[i + 1])
        else:
            buy += int(arr_all_data[i + 1])

    result = supply - buy

    with open(report_file_name, "w") as output_file:
        output_file.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
