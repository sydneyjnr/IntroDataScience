import marimo

__generated_with = "0.19.6"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Exercise 2: Data Wrangling

    **Practice Polars!**

    **What you'll do:**

    - Load and explore real datasets
    - Filter and transform data
    - Answer questions with data

    **Instructions:**

    - Complete each TODO section
    - Run cells to see your results

    ---
    """)
    return


@app.cell
def _():
    import polars as pl
    import plotly.express as px
    import plotly.graph_objects as go
    from datetime import datetime
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 1: Load and Explore Data
    """)
    return


@app.cell
def _():
    # TODO: Load the students.csv file using Polars
    # The file is at: ../data/raw/students.csv
    import polars as pl
    students = pl.read_csv("../data/raw/students.csv")  # Replace with pl.read_csv(...)

    # TODO: Display the first 10 rows
    print(students.head(10))
    return students


@app.cell
def _(students):
    # TODO: Display basic information about the students dataset
    # - How many rows and columns?
    # - What are the column names?
    # - What are the data types?

    # Hint: Use students.shape, students.columns, students.dtypes, or students.describe()
    print(f"Shape: {students.shape}")
    print(f"Columns: {students.columns}")
    print(f"Data Types:\n{students.dtypes}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 2: Filtering Practice
    """)
    return


@app.cell
def _(students):
    import polars as pl
    # TODO: Filter to find students who scored above 85 on their test

    high_scorers = students.filter(pl.col("test_score") > 85)  # Use students.filter(...)

    print(f"Number of high scorers: {len(high_scorers) if high_scorers is not None else 0}")
    return


@app.cell
def _(students):
    import polars as pl
    # TODO: Filter to find students in grade_level 10 with attendance_rate > 90%

    grade_10_good_attendance = students.filter((pl.col("grade_level") == 10) & (pl.col("attendance_rate") > 0.9))  # Use multiple conditions with &
    print(f"Number of grade 10 students with good attendance: {len(grade_10_good_attendance) if grade_10_good_attendance is not None else 0}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 3: Selecting and Creating Columns
    """)
    return


@app.cell
def _(students):
    import polars as pl
    # TODO: Select only the name, grade_level, and test_score columns

    subset = students.select("name", "grade_level", "test_score")  # Use students.select(...)
    print(subset.head())
    return


@app.cell
def _(students):
    import polars as pl
    # TODO: Create a new column "performance_category" that categorizes students:
    # - "Excellent" if test_score >= 90
    # - "Good" if test_score >= 75
    # - "Needs Improvement" if test_score < 75
    # - Handle null values appropriately

    # Hint: Use pl.when().then().otherwise() chains

    students_categorized = students.with_columns(
        pl.when(pl.col("test_score") >= 90)
        .then(pl.lit("Excellent"))
        .when(pl.col("test_score") >= 75)
        .then(pl.lit("Good"))
        .otherwise(pl.lit("Needs Improvement"))
        .alias("performance_category")
    )
    print(students_categorized.select("name", "test_score", "performance_category").head())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 4: Working with Sales Data
    """)
    return


@app.cell
def _():
    import polars as pl
    # TODO: Load the sales.json file
    # The file is at: ../data/raw/sales.json

    sales = pl.read_json("../data/raw/sales.json")  # Replace with pl.read_json(...)
    # print(f"Shape: {sales.shape}")
    return sales


@app.cell
def _(sales):
    import polars as pl
    # TODO: Display basic info about the sales dataset
    # How many transactions? What's the date range?
    print(f"Number of transactions: {sales.shape[0]}")
    print(f"Date range: {sales.select(pl.col('date').min()).item()} to {sales.select(pl.col('date').max()).item()}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 5: Aggregations and Grouping
    """)
    return


@app.cell
def _(sales):
    import polars as pl
    # TODO: Calculate total sales by product_category
    # Sum up the total_amount for each category
    # Sort by total sales descending

    category_sales = sales.group_by("product_category").agg(pl.sum("total_amount").alias("total_sales")).sort("total_sales", descending=True)
    print(f"Total sales by product category:\n{category_sales}")
    return


@app.cell
def _(sales):
    import polars as pl
    # TODO: Find the average transaction amount by payment_method

    avg_by_payment = sales.group_by("payment_method").agg(pl.mean("total_amount").alias("avg_transaction_amount"))

    print(f"Average transaction amount by payment method:\n{avg_by_payment}")
    return


@app.cell
def _(sales):
    import polars as pl
    # TODO: Count how many transactions each region had
    # Also calculate the total revenue per region

    region_summary = sales.group_by("region").agg(
        pl.count().alias("transaction_count"),
        pl.sum("total_amount").alias("total_revenue")
    )
    print(f"Transaction count and total revenue by region:\n{region_summary}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 6: Date Operations
    """)
    return


@app.cell
def _(sales):
    import polars as pl
    # TODO: Convert the date column to datetime type
    # Then extract the month and create a new column "month"

    sales_with_month = sales.with_columns(pl.col("date").str.to_date().alias("date"))
    sales_with_month = sales_with_month.with_columns(pl.col("date").dt.month().alias("month"))
    print(sales_with_month.select("date", "month").head())
    return


@app.cell
def _(sales):
    # TODO: Calculate total sales by month
    # Show which month had the highest revenue

    monthly_sales = sales.group_by("month").agg(pl.sum("total_amount").alias("total_sales")).sort("total_sales", descending=True)
    print(f"Total sales by month:\n{monthly_sales}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🎉 Excellent Work!

    You've completed the data wrangling exercises!

    **What you practiced:**

    - ✅ Loading CSV and JSON data with Polars
    - ✅ Filtering and selecting data
    - ✅ Creating calculated columns
    - ✅ Grouping and aggregating
    - ✅ Date operations

    **What's next?**

    - Move on to Exercise 3: Plot

    **Pro Tips:**

    - Chain Polars operations for cleaner code
    - Always explore your data before plotting
    """)
    return


if __name__ == "__main__":
    app.run()
