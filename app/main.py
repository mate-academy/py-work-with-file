def create_report(data_file_name: str,
                  report_file_name: str) -> None:
    with (open(data_file_name, "r") as file_in,
          open(report_file_name, "w") as file_out):
        lines = file_in.readlines()
        result_data = {"supply": 0, "buy": 0, "result": 0}
        for line in lines:
            data_in_line = line.split(",")
            if data_in_line[0] == "supply":
                result_data["supply"] += int(data_in_line[1])
            if data_in_line[0] == "buy":
                result_data["buy"] += int(data_in_line[1])
        result_data["result"] = result_data["supply"] - result_data["buy"]
        for key in result_data.keys():
            file_out.write(f"{key},{result_data[key]}\n")
