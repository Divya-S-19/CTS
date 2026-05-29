import statistics

def process_sales():
    try:
        with open("sales.txt", "r") as f:
            data = [float(x.strip()) for x in f.readlines()]

        print("Mean:", statistics.mean(data))
        print("Median:", statistics.median(data))

    except FileNotFoundError:
        print("File not found")
    except ValueError:
        print("Invalid data in file")


process_sales()