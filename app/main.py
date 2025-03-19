def create_report(data_file_name: str, report_file_name: str) -> None:
    result_dict = {}
    with open(data_file_name, "r") as file_1,\
            open(report_file_name, "a") as file_2:
        splitted = file_1.read().splitlines()
        for value in splitted:
            if value == "":
                continue
            values = value.split(",")
            if not values[0] in result_dict:
                result_dict[values[0]] = int(values[1])
            else:
                result_dict[values[0]] += int(values[1])
        supply = result_dict["supply"]
        buy = result_dict["buy"]
        result = result_dict["supply"] - result_dict["buy"]
        file_2.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
