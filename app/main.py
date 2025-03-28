SUPPLY_OPERATION = "supply"
BUY_OPERATION = "buy"


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as file_in, \
         open(report_file_name, "w") as file_out:
        for line in file_in.readlines():
            operation, amount = line.split(",")

            if operation == SUPPLY_OPERATION:
                supply += int(amount)
            elif operation == BUY_OPERATION:
                buy += int(amount)

        result = supply - buy

        out_content = (
            f"{SUPPLY_OPERATION},{supply}\n"
            f"{BUY_OPERATION},{buy}\n"
            f"result,{result}\n"
        )

        file_out.write(out_content)
