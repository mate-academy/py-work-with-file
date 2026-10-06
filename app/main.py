def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r") as data_file,
          open(report_file_name, "w") as report_file):
        data = {}

        for line in data_file.read().split("\n"):
            if line == "":
                break
            key, value = line.split(",")
            if key in data:
                data[key] += int(value)
            else:
                data[key] = int(value)

        supply = data["supply"]
        buy = data["buy"]
        result = int(supply) - int(buy)

        report_file.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
