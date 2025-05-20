import matplotlib.pyplot as plt
from load_csv import load

def plot(path1: str, path2: str):
	life_expect = load(path1)
	gdp = load(path2)

	if life_expect is None or gdp is None:
		return

	# Format Data:
	life_1900 = life_expect[['country', '1900']]
	life_1900 = life_1900.drop(columns=['country']).squeeze()

	gdp_1900 = gdp[['country', '1900']]
	gdp_1900 = gdp_1900.drop(columns=['country']).squeeze()

	# non_int_values = gdp_1900[~gdp_1900.apply(lambda x: isinstance(x, int))]
	# print(non_int_values) --> all integers

	plt.figure(figsize=(8, 6))
	plt.scatter(gdp_1900, life_1900, color='blue')

	# Achsenbeschriftungen und Titel
	plt.title('1900')
	plt.xlabel('GDP')
	plt.ylabel('Life Expectancy')

	plt.grid(True)
	plt.savefig("plot.png")

	return


plot("../Data/life_expectancy_years.csv", "../Data/income_per_person_gdppercapita_ppp_inflation_adjusted.csv")