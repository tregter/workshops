# fetches data from Dynamo
def fetch_data():
    raise Exception("data fetching failed")


def process_data(x):
    return x["a"] + x["b"]


def main():
    print("1. fetch data")
    x = fetch_data()

    # -------------------------------
    # DOES THIS CODE EXECUTE?
    # -------------------------------
    print("2. process and print data")
    processed_data = process_data(x)
    print(processed_data)
    print("3. done")
    # -------------------------------


try:
    main()
except Exception as e:
    print(f"Error: {e}")
