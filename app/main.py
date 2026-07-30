def create_report(data_file_name: str, report_data_name: str) -> None:
    with open(data_file_name, "r") as file_in,\
         open(report_data_name, "w") as file_out:
        mean_supply = 0
        mean_buy = 0
        mean_result = 0
        for item in file_in.read().split("\n"):
            if item.split(",")[0] == "supply":
                mean_supply += int(item.split(",")[1])
            if item.split(",")[0] == "buy":
                mean_buy += int(item.split(",")[1])
        mean_result = mean_supply - mean_buy
        file_out.write(
            f"supply,{mean_supply}\n"
            f"buy,{mean_buy}\n"
            f"result,{mean_result}\n"
        )
