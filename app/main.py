import csv


def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    data = {"supply": 0, "buy": 0}

    with open(
        data_file_name,
        mode="r",
        newline=""
    ) as r_file, open(
        report_file_name,
        mode="w",
        newline=""
    ) as w_file:
        reader = csv.reader(r_file)

        for row in reader:
            if not row or len(row) < 2:
                continue

            try:
                if row[0] == "supply":
                    data["supply"] = data.get("supply", 0) + int(row[1])
                elif row[0] == "buy":
                    data["buy"] = data.get("buy", 0) + int(row[1])
            except ValueError:
                print("Value error")
        data = [
            ["supply", data["supply"]],
            ["buy", data["buy"]],
            ["result", str(data["supply"] - data["buy"])]
        ]
        writer = csv.writer(w_file)
        writer.writerows(data)
