def create_report(data_file_name: str, report_file_name: str) -> None:
    with (
        open(data_file_name, "r") as dfn,
        open(report_file_name, "w") as rfn
    ):
        sum_buy = 0
        sum_supply = 0

        for line in dfn.readlines():
            if line.startswith("supply"):
                sum_supply += int(line.split(",")[1])
            if line.startswith("buy"):
                sum_buy += int(line.split(",")[1])

        result = sum_supply - sum_buy

        rfn.write(
            f"supply,{sum_supply}\n"
            f"buy,{sum_buy}\n"
            f"result,{result}\n"
        )
