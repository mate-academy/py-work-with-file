def create_report(data_file_name: str, report_file_name: str) -> None:
    bought = 0
    supplied = 0

    with open(data_file_name, "r") as f:
        lines = f.readlines()

    for line in lines:
        if "buy" in line:
            buy = int(line.split(",")[1])
            bought += buy
        elif "supply" in line:
            supply = int(line.split(",")[1])
            supplied += supply

    result = supplied - bought

    with open(report_file_name, "w") as new_file:
        new_file.write(f"supply,{supplied}\n")
        new_file.write(f"buy,{bought}\n")
        new_file.write(f"result,{result}\n")
