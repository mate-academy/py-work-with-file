def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name) as get:
        with open(report_file_name, "w") as output:
            info = []
            for line in get:
                info.append(line.split(","))
            supply = 0
            buy = 0
            for part in info:
                if part[0] == "supply":
                    supply += int(part[1])
                else:
                    buy += int(part[1])
            result = supply - buy
            output.write(f"supply,{supply}\n"
                         f"buy,{buy}\n"
                         f"result,{result}\n")
