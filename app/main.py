def create_report(data_file_name: str, report_file_name: str = "") -> None:
    data_dict = {}
    io = []
    with open(data_file_name) as f_data:
        io = f_data.readlines()

    print(io)

    for data in io:
        if data.split(",")[0] in data_dict:
            data_dict[data.split(",")[0]] += int(data.split(",")[1])
        else:
            data_dict[data.split(",")[0]] = int(data.split(",")[1])

    with open(report_file_name,"w") as f_data:
        supply = str(data_dict["supply"])
        buy = str(data_dict["buy"])
        result = data_dict["supply"] - data_dict["buy"]

        f_data.write(f"supply,{supply}\n")
        f_data.write(f"buy,{buy}\n")
        f_data.write(f"result,{result}\n")
