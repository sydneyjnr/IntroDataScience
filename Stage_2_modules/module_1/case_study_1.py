import marimo

__generated_with = "0.20.2"
app = marimo.App(width="medium")


@app.cell
def _():
    return


@app.cell
def _():
    import marimo as mo

    mo.md("# Case Study 1")
    return (mo,)


@app.cell
def _(mo):
    mo.md("""
    ## Visualization 1: GPU Prices & Cryptocurrency Mining

    [View Article](https://priceonomics.com/how-has-cryptocurrency-mining-influenced-gpu-prices/)

    ![GPU Visualization](https://etzq49yfnmd.exactdn.com/wp-content/uploads/2022/03/image2-13.jpg?strip=all)
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    This visualization explores how cryptocurrency mining has influenced GPU prices over time, particularly during periods of high demand such as early 2021. It effectively connects real-world events, like the pandemic and crypto booms, to spikes in GPU prices, helping the reader understand the relationship between supply, demand, and pricing. The narrative style combined with the data makes the visualization engaging and easy to follow, especially for readers unfamiliar with the topic. The inclusion of historical context adds depth to the analysis. Overall, the visualization clearly answers the question, though it relies heavily on text rather than precise visual clarity.

    **What’s good:**
    - Strong storytelling
    - Real-world context
    - Clear trend emphasis

    **Issue:**
    - Visualization lacks detailed labeling and precision
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Visualization 2: Your New iPhone Is Late

    [View Article](https://priceonomics.com/your-new-iphone-is-late/)

    ![iPhone Supply Chain](https://etzq49yfnmd.exactdn.com/wp-content/uploads/2022/03/iPhone-Birthplaces-32122_smaller.jpg?strip=all&w=2560)

    This visualization shows the global supply chain of iPhone components.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    This visualization explores how global supply chain disruptions—particularly COVID-19 lockdowns in major Chinese port cities—affect iPhone production and delivery times. It clearly shows how iPhone components are sourced from multiple countries and must arrive at assembly facilities in perfect coordination. By linking real-world events like port congestion and manufacturing slowdowns to delays in consumer products, the visualization helps readers understand the complexity and fragility of global supply chains. The combination of a world map and production flow makes the explanation intuitive and engaging, especially for readers unfamiliar with logistics systems. Overall, the visualization effectively answers the question, though it focuses more on illustrating the process than providing precise quantitative data.

    **What’s good:**
    - Clear visualization of global supply chain
    - Strong connection between real-world events and impact
    - Easy-to-understand flow of production

    **Issue:**
    - Lacks detailed quantitative data (e.g., exact volumes or timelines)
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Visualization 3: Senior Mental Health by Gender

    [View Article](https://priceonomics.com/senior-citizens-face-mental-and-financial-stress/)

    ![Mental Health Visualization](https://etzq49yfnmd.exactdn.com/wp-content/uploads/2022/03/Womenhealth.png?strip=all&resize=640%2C480)
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    This visualization highlights the disparity in mental health between male and female seniors, showing that women are more than twice as likely as men to report not feeling mentally healthy. The chart is simple and immediately communicates the key insight through clear percentage comparisons, making it easy for readers to grasp the gender gap. It aligns well with the broader narrative of the article, reinforcing the theme that women experience more stress in later life. The minimalistic design helps focus attention on the core message without unnecessary distractions.

    **What’s good:**
    - Clear and easy-to-understand comparison
    - Strong alignment with the article’s narrative
    - Effective use of percentages to emphasize disparity

    **Issue:**
    - Lacks additional context (e.g., sample size or timeframe) which could improve interpretation
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Visualization 4: Life Expectancy by Age in England and Wales

    [View Article](https://ourworldindata.org/life-expectancy)

    ![Life Expectancy Visualization](https://ourworldindata.org/cdn-cgi/imagedelivery/qLq-8BTgXU8yG0N6HnOy8g/10a0ca12-415d-41c8-f6b8-0fcdd9fac900/w=1350)
    """)

    return


@app.cell
def _(mo):
    mo.md("""
    This visualization illustrates how life expectancy has increased across all age groups in England and Wales from 1700 to 2013, challenging the common belief that improvements are solely due to reductions in child mortality. By using multiple colored lines to represent different age groups, it effectively shows that gains in longevity occurred at every stage of life. The historical context, including events like the 1918 Spanish flu, adds depth and helps explain fluctuations in the data. Overall, the chart communicates a complex, long-term trend in a compelling and informative way.

    **What’s good:**
    - Displays multiple age groups simultaneously for deeper insight
    - Strong historical context enhances understanding of trends
    - Clearly challenges a common misconception with data

    **Issue:**
    - The chart is visually dense and may be difficult for beginners to interpret
    """)
    return


if __name__ == "__main__":
    app.run()
