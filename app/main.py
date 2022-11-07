def create_report(data_file_name: str, report_file_name: str) -> None:
    with open("/Users"
              "/ruravictor"
              "/PycharmProjects"
              "/pythonProject1"
              "/py-work-with-file"
              "/apples.csv", "r") as bananas:
        supply = []
        buy = []
        for i in bananas.read().split():
            if i[0] == "s":
                supply.append(int(i[7:]))
            if i[0] == "b":
                buy.append(int(i[4:]))
        result = sum(supply) - sum(buy)
        with open("apples_report.csv", "w") as apples_report:
            apples_report.write(f"supply,{sum(supply)}\n"
                                f"buy,{sum(buy)}\n"
                                f"result,{result}\n")

    with open("/Users"
              "/ruravictor"
              "/PycharmProjects"
              "/pythonProject1"
              "/py-work-with-file"
              "/bananas.csv", "r") as bananas:
        supply = []
        buy = []
        for i in bananas.read().split():
            if i[0] == "s":
                supply.append(int(i[7:]))
            if i[0] == "b":
                buy.append(int(i[4:]))
        result = sum(supply) - sum(buy)
        with open("bananas_report.csv", "w") as bananas_report:
            bananas_report.write(f"supply,{sum(supply)}\n"
                                 f"buy,{sum(buy)}\n"
                                 f"result,{result}\n")

    with open("/Users"
              "/ruravictor"
              "/PycharmProjects"
              "/pythonProject1"
              "/py-work-with-file"
              "/grapes.csv", "r") as grapes:
        supply = []
        buy = []
        for i in grapes.read().split():
            if i[0] == "s":
                supply.append(int(i[7:]))
            if i[0] == "b":
                buy.append(int(i[4:]))
        result = sum(supply) - sum(buy)
        with open("grapes_report.csv", "w") as grapes_report:
            grapes_report.write(f"supply,{sum(supply)}\n"
                                f"buy,{sum(buy)}\n"
                                f"result,{result}\n")

    with open("/Users"
              "/ruravictor"
              "/PycharmProjects"
              "/pythonProject1"
              "/py-work-with-file"
              "/oranges.csv", "r") as oranges:
        supply = []
        buy = []
        for i in oranges.read().split():
            if i[0] == "s":
                supply.append(int(i[7:]))
            if i[0] == "b":
                buy.append(int(i[4:]))
        result = sum(supply) - sum(buy)
        with open("oranges_report.csv", "w") as oranges_report:
            oranges_report.write(f"supply,{sum(supply)}\n"
                                 f"buy,{sum(buy)}\n"
                                 f"result,{result}\n")
