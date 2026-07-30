def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as recieved_file:
        ls = recieved_file.readlines()
        data_ls = []
        for word in ls:
            element = word.split()
            data = element[0].split(",")
            data_ls.append(data)
        supply = 0
        buy = 0
        result = 0
        for item in data_ls:
            if item[0] == "supply":
                supply += int(item[1])
            if item[0] == "buy":
                buy += int(item[1])
            result = supply - buy

    with open(report_file_name, "w") as output_file:
        output_file.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
