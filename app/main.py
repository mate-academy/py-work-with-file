def create_report(data_file_name: str, report_file_name: str) -> None:
    date = {"supply": 0, "buy": 0}
    with (
        open(data_file_name, "r") as date_file,
        open(report_file_name, "w") as report_file
    ):
        one_line: list
        for line in date_file:
            one_line = line.replace(",", " ").split()

            if "supply" in one_line:
                date["supply"] += int(one_line[1])
            else:
                date["buy"] += int(one_line[1])

        date.update({"result": (date["supply"] - date["buy"])})

        for key, value in date.items():
            report_file.write("{},{}\n".format(key, value))
