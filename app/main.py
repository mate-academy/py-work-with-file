def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as file:
        for line in file:
            data = line.strip().split(",")
            if len(data) < 2:
                continue
            cmd = data[0].strip()
            numbers_str = data[1].strip().split()
            numbers = [int(x) for x in numbers_str if x.isdigit()]
            total = sum(numbers)
            if cmd == "supply":
                supply += total
            elif cmd == "buy":
                buy += total
    with open(report_file_name, "w") as result:
        result.write(f"supply,{supply}\n")
        result.write(f"buy,{buy}\n")
        result.write(f"result,{supply - buy}\n")
