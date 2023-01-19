# write your code here
def create_report(data_file_name: str, report_file_name: str) -> None:
    data_dict = {}
    with open(f"{data_file_name}", "r") as file_in:
        for line in file_in.read().split():
            name, values = line.split(",")
            if name in data_dict.keys():
                data_dict[name] += int(values)
                continue
            if name == "supply":
                data_dict["supply"] = int(values)
            if name == "buy":
                data_dict["buy"] = int(values)
        result = data_dict["supply"] - data_dict["buy"]

    with open(report_file_name, "w") as file_out:
        file_out.write(
            f"supply,{data_dict['supply']}\n"
            f"buy,{data_dict['buy']}\n"
            f"result,{result}\n"
        )