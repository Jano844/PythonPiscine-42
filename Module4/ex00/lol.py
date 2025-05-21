import statistics
import math


# def ft_statistics(*args: any, **kwargs: any) -> None:
# 	for i in args:
# 		print(i)

# 	for key, values in kwargs.items():
# 		print(f"{key}, {values}")


def ft_mean(list):
	mean = sum(list) / len(list)
	return mean

def ft_median(list):
	sort_list = sorted(list)
	mid = len(sort_list) // 2

	if len(sort_list) % 2 == 0:
		return (sort_list[mid - 1] + sort_list[mid]) / 2
	return sort_list[mid]

def ft_quartile(data, percents):
	sorted_data = sorted(data)
	n = len(sorted_data)
	results = []

	for percent in percents:
		pos = percent * (n - 1)
		low = int(pos)
		high = min(low + 1, n - 1)
		fraction = pos - low
		quantile = sorted_data[low] + fraction * (sorted_data[high] - sorted_data[low])
		results.append(quantile)

	return results


def ft_std_deviation(list):
	std_dev = ft_variance(list) ** 0.5 # sqrt notmal math.sqrt
	return std_dev



def ft_variance(list):
	new_list = [i - ft_mean(list) for i in list]
	variance = sum([i * i for i in new_list]) / (len(list) - 1)
	return variance



def ft_statistics(*args: any, **kwargs: any) -> None:
	for key, value in kwargs.items():
		if len(args) == 0:
			print("Error")
		elif value == "mean":
			print(ft_mean(args))
		elif value == "median":
			print(ft_median(args))
		elif value == "quartile":
			print(ft_quartile(args, [0.25, 0.75]))
		elif value == "std":
			print(ft_std_deviation(args))
		elif value == "var":
			print(ft_variance(args))


if __name__ == '__main__':
	test : list[float] = [1, 42, 360, 11, 64]
	print(ft_std_deviation(test))
	print(statistics.stdev(test))
