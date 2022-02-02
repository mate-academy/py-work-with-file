def create_report(data_file_name: str, report_file_name: str):
    with open(data_file_name, "r") as f:
        lines = f.readlines()
        with open(report_file_name, "w") as f2:
            supply = 0
            buy = 0
            for line in lines:
                content = line.split(',')
                if content[0] == "supply":
                    supply += int(content[1])
                elif content[0] == "buy":
                    buy += int(content[1])
            f2.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")
            print("success")


if __name__ == "__main__":
    create_report()
