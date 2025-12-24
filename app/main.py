def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:

    cache = {
        "supply": 0,
        "buy": 0
    }

    with open(data_file_name, "r") as data_to_read:

        for line in data_to_read:

            line = line.strip()
            if not line:
                continue

            split_line = line.split(",")

            operation_type = split_line[0]
            amount = split_line[1]

            cache[operation_type] += int(amount)

    with open(report_file_name, "w") as data_to_write:

        supply = cache["supply"]
        buy = cache["buy"]
        result = supply - buy

        data_to_write.write(f"supply,{supply}\n"  # noqa: E231
                            f"buy,{buy}\n"  # noqa: E231
                            f"result,{result}\n")  # noqa: E231
