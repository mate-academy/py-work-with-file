def create_report(first_file: str, second_file: str) -> None:

    dict_ = {"supply": 0, "buy": 0}
    with open(first_file, "r") as f:
        data = f.readlines()
        for line in data:
            ls = line.replace("\n", "").split(",")
            dict_[ls[0]] += int(ls[1])

    with open(second_file, "w") as f:
        supply = dict_["supply"]
        buy = dict_["buy"]
        result = supply - buy
        f.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
