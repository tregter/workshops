# fetches data from Dynamo
def fetch_data():
    raise Exception("data fetching failed")


def process_data(x):
    return x["a"] + x["b"]


def main():
    x = None
    try:
        x = fetch_data()
    except Exception as e:
        print(f"Error: {e}")

    processed_data = process_data(x)
    print(processed_data)


main()
