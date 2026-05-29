import statistics

try:
    # Open and read the file
    with open("sales.txt", "r") as file:
        sales_data = []

        for line in file:
            # Convert each line into a number
            sales_data.append(float(line.strip()))

    # Calculate statistics
    mean_value = statistics.mean(sales_data)
    median_value = statistics.median(sales_data)

    # Print statistics summary
    print("Sales Statistics Summary")
    print("------------------------")
    print("Total Entries:", len(sales_data))
    print("Mean Sales:", mean_value)
    print("Median Sales:", median_value)

except FileNotFoundError:
    print("Error: sales.txt file not found.")

except ValueError:
    print("Error: File contains invalid data.")

except statistics.StatisticsError as error:
    print("Statistics Error:", error)