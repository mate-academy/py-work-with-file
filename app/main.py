def create_report(data_file_name: str, report_file_name: str) -> None:
    with (
        open(data_file_name, "r") as file_in,
        open(report_file_name, "w") as file_out
    ):
        content = file_in.read().split()
        value_supply = 0
        value_buy = 0
        for elem in content:
            value = elem.split(",")
            if value[0] == "supply":
                value_supply += int(value[1])
            elif value[0] == "buy":
                value_buy += int(value[1])

        report = f"supply,{value_supply}\n" \
                 f"buy,{value_buy}\n" \
                 f"result,{value_supply - value_buy}\n"
        file_out.write(report)
