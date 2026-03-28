def create_report(data_file_name: str, report_file_name: str) -> None:
    data: dict[str, int] = {"supply": 0, "buy": 0}
    with open(data_file_name, "r") as source, open(
        report_file_name, "w"
    ) as target:
        for line in source.readlines():
            line = line.strip()
            if line != "\n":
                field, value = line.split(",")
                data[field] = data.get(field, 0) + int(value)
        target.write(
            "\n".join(
                [
                    f"supply,{data['supply']}",
                    f"buy,{data['buy']}",
                    f"result,{data['supply'] - data['buy']}\n",
                ]
            )
        )
