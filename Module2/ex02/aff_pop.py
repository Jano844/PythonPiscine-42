from load_csv import load
import matplotlib.pyplot as plt


def convert_to_numeric(value):
    if isinstance(value, str) and 'M' in value:
        return float(value.replace('M', ''))
    return value

def plot(path: str):
    dataframe = load(path)

    if dataframe is None:
        return


    # get Data into right format
    germany = dataframe[dataframe['country'] == 'Germany']
    ger = germany.drop(columns=['country']).squeeze()
    ger = ger.apply(convert_to_numeric)
    ger.index = ger.index.astype(int)
    ger = ger.loc[1800:2050]

    belguim = dataframe[dataframe['country'] == 'Belgium']
    bel = belguim.drop(columns=['country']).squeeze()
    bel = bel.apply(convert_to_numeric)
    bel.index = bel.index.astype(int)
    bel = bel.loc[1800:2050]


    # Start Plotting
    plt.clf()
    # plt.figure(figsize=(10, 6))

    plt.plot(ger.index, ger.values, label='Germany')
    plt.plot(bel.index, bel.values, label='Belgium')

    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.legend()

    plt.tight_layout()
    plt.savefig("plot.png")

plot("../Data/population_total.csv")