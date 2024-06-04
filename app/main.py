def create_report(data_file_name: str, report_file_name: str) -> None:
    with open("data_file_name", "r") as file:
        content = file.read()

    with open("report_file_name", "w") as report_file:
        for line in content:
            report_file.write(line + "\n")

    # if __name__ == "__main__":
    #     main()
