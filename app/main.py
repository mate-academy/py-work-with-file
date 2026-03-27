def create_report(data_file_name: str, report_file_name: str) -> None:
    data = {}
    with open(data_file_name, "r") as f:
        data = {}
        lines = [line.rstrip() for line in f]
        for i in range(len(lines)):
            curr = lines[i].split(",")
            key, value = curr[0], int(curr[1])
            if key not in data:
                data[key] = value
            else:
                data[key] += value

    with open(report_file_name, "w") as f:
        if list(data.items())[0][0] == "supply":
            for key, value in list(data.items()):
                f.write(f"{key},{value}\n")
        else:
            for key, value in list(data.items())[::-1]:
                f.write(f"{key},{value}\n")

    with open(report_file_name, "r+") as f:
        lines = [line.rstrip() for line in f]
        res = int(lines[0].split(",")[1]) - int(lines[1].split(",")[1])
        f.write(f"result,{str(res)}\n")
