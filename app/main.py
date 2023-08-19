def create_report(data_file_name: str, report_file_name: str) -> None:
    rez = {}
    with open(f"{data_file_name}", "r") as data_file:
        while True:
            line = data_file.readline()
            if not line:
                break
            arr = line.split(",")
            if arr[0] not in rez:
                rez[arr[0]] = 0
                rez[arr[0]] += int(arr[1])
            else:
                rez[arr[0]] += int(arr[1])
    with open(f"{report_file_name}", "w") as report_file:
        report_file.write(f"supply,{rez['supply']}\n")
        report_file.write(f"buy,{rez['buy']}\n")
        report_file.write(f"result,{rez['supply'] - rez['buy']}\n")
