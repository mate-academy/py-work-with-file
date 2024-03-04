def create_report(data_file_name: str, report_file_name: str) -> None:

    with open(data_file_name, "r") as file:

        read_lines = file.readlines()

        multy_supply = sum(int(i.split(",")[1])
                           for i in read_lines if i.split(",")[0] == "supply")

        multy_buy = sum(int(i.split(",")[1])
                        for i in read_lines if i.split(",")[0] == "buy")

    with open(report_file_name, "w") as file:

        file.write(
            f"supply,{multy_supply}\n"
            f"buy,{multy_buy}\n"
            f"result,{multy_supply - multy_buy}\n"
        )
