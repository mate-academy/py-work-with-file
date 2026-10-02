def create_report(data_file_name: str, report_file_name: str) -> str:
    with (open(data_file_name, "r") as src_file,
          open(report_file_name, "w") as dst_file
          ):

        total_supply = 0
        total_buy = 0

        for line in src_file:
            data = line.strip().split(",")

            if data[0] == "supply":
                total_supply += int(data[1])

            if data[0] == "buy":
                total_buy += int(data[1])

        result = total_supply - total_buy

        dst_file.write(
            f"supply,{total_supply}\n"
            f"buy,{total_buy}\n"
            f"result,{result}\n"
        )
