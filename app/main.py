def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as new_file:
        lines = new_file.readlines()
    supplies = sum([int(line.split(",")[1]) for line in lines if line.split(",")[0] == "supply"])
    buyes = sum([int(line.split(",")[1]) for line in lines if line.split(",")[0] == "buy"])
    result = supplies - buyes
    with open(report_file_name, "w") as file_second:
        file_second.write(f"supply,{supplies}\n")
        file_second.write(f"buy,{buyes}\n")
        file_second.write(f"result,{result}\n")
