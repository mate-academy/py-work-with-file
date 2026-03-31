def create_report(data_file_name: str, report_file_name: str) -> None:
    temporary_dict = {"supply": 0, "buy": 0}
    with (
        open(data_file_name, "r") as file_in,
        open(report_file_name, "a") as file_out
    ):
        for name in file_in:
            position, value = name.split(",")
            temporary_dict[position] += int(value)

        temporary_dict["result"] = \
            temporary_dict["supply"] - temporary_dict["buy"]

        for position, value in temporary_dict.items():
            file_out.write(f"{position},{str(value)}\n")
