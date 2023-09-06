from csv import reader


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(rf"D:\python\mate\py-work-with-file\{data_file_name}",
              "r") as file:
        print(file)
        lines = reader(file)
        supply = 0
        buy = 0
        for line in lines:
            if line[0] == "supply":
                supply += int(line[1])
            elif line[0] == "buy":
                buy += int(line[1])
    new_file = open(rf"D:\python\mate\py-work-with-file\{report_file_name}",
                    "w")
    amount = supply - buy
    new_file.write(f"supply,{str(supply)}\n")
    new_file.write(f"buy,{str(buy)}\n")
    new_file.write(f"result,{str(amount)}\n")
