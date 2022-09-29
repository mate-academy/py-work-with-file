def create_report(data_file_name: str, report_file_name: str):
    with open(data_file_name, "r") as data:
        lines = data.readlines()
        with open(report_file_name, "w") as report:
            supply = 0
            buy = 0
            for line in lines:
                content = line.split(',')
                if content[0] == "supply":
                    supply += int(content[1])
                elif content[0] == "buy":
                    buy += int(content[1])
            report.write(f"supply,{supply}\n"
                         f"buy,{buy}\n"
                         f"result,{supply - buy}\n")
            print("success")


if __name__ == "__main__":
    create_report()
