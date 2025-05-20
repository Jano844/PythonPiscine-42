from load_csv import load
import matplotlib.pyplot as plt



def plot_life(path: str):

    dataframe = load(path)
    if dataframe is None:
        return
    germany_df = dataframe[dataframe['country'] == 'Germany']
    ger_row = germany_df.drop(columns=['country']).squeeze()
    print(ger_row)

    ger_row.index = ger_row.index.astype(int)
    plt.plot(ger_row.index, ger_row.values)
    plt.title("Life Expectancy in Germany (1800–2100)")
    plt.xlabel("Year")
    plt.ylabel("Life Expectancy")
    plt.grid(True)
    #plt.show() to print in Terminal
    plt.savefig("Germany_plot", dpi=300)
    return



plot_life("../Data/life_expectancy_years.csv")