import polars as pl

def main():
    df = pl.DataFrame({
        "name": ["Alice", "Bob", "Charlie"],
        "age": [24, 32, 45]
    })

    print(df)


if __name__ == "__main__":
    main()
