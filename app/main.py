def create_report(data_file_name: str, report_file_name: str):
    with open(data_file_name, "r") as data_file, \
            open(report_file_name, "w") as report_file:
        data = data_file.read()
        data_str = data.replace("\n", " ")
        data_list = data_str.split()
        supply = 0
        buy = 0
        for elem_list in data_list:
            new_elem_list = elem_list.split(",")
            if new_elem_list[0] == "supply":
                supply += int(new_elem_list[1])
            elif new_elem_list[0] == "buy":
                buy += int(new_elem_list[1])
        result = supply - buy
        report_file.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
