def create_report(data_file_name: str, report_file_name: str) -> None:
    file_sorted = {"supply": 0, "buy": 0}
    with (open(data_file_name, "r") as first_f,
          open(report_file_name, "w") as second_f):
        file_contents = first_f.read().split("\n")
        for string in file_contents:
            if string:
                key, value = string.split(",")
                value = int(value)
                file_sorted[key] += value

        file_sorted["result"] = file_sorted["supply"] - file_sorted["buy"]

        for key, value in file_sorted.items():
            second_f.write(f"{key},{value}\n")
