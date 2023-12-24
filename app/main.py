def create_report(data_file_name: str,
                  report_file_name: str
                  ) -> None:
    with (open(data_file_name) as from_file,
          open(report_file_name, "w") as to_file):
        supply = 0
        buy = 0
        for line in from_file.read().split("\n"):
            if line:
                item, value = line.split(",")
                if item == "supply":
                    supply += int(value)
                elif item == "buy":
                    buy += int(value)
        to_file.write("supply," + str(supply)
                      + "\nbuy," + str(buy)
                      + "\nresult," + f"{supply - buy}\n")


if __name__ == "__main__":
    create_report("example.csv", "test.csv")
