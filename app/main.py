def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file_in, open(
            report_file_name, "w") as file_out:
        data_dict = {
            "supply": 0,
            "buy": 0,
        }

        for line in file_in:
            data = line.split(",")
            data_dict[data[0]] += int(data[1])

        data_dict["result"] = data_dict["supply"] - data_dict["buy"]

        for key, value in data_dict.items():
            file_out.write(f"{key},{value}\n")
