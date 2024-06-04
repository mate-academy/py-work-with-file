def create_report(data_file_name: str, report_file_name: str) -> None:
    file = open("data_file_name", "r")
    file.read()
    file.close()

    with open("report_file_name", "w") as report_file:
        for line in file:
            report_file.write(line + "\n")

    if __name__ == "__main__":
        main()
