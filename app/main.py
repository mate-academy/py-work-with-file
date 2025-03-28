def create_report(data_filename: str, report_file_name: str) -> None:
    with (open(data_filename, "r") as file_in,
          open(report_file_name, "w") as file_out):

        info = file_in.read().splitlines()

        report_data = {"supply": 0, "buy": 0}

        for elem in info:
            if elem.split(",")[0] == "supply":
                report_data["supply"] += int(elem.split(",")[1])
            elif elem.split(",")[0] == "buy":
                report_data["buy"] += int(elem.split(",")[1])

        file_out.write(f"supply,{report_data['supply']}\n"
                       f"buy,{report_data['buy']}\n"
                       f"result,"
                       f"{report_data['supply'] - report_data['buy']}\n")
