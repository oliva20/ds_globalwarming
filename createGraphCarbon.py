import matplotlib as mpl
#mpl.use('Agg')
import matplotlib.pyplot as plt
from random import randint
from pymongo import MongoClient
plt.style.use("ggplot")

host = "mongodb://localhost:27017"
client = MongoClient(host)
db = client["gw_data"]
col = db["carbon_emissions"]


def main():
	country="Spain"
	years = []
	values = []

	q = {"GEO":country}

	doc = col.find(q)

	for x in doc:
		years.append(x["TIME"])
		values.append(float(x["Value"].replace(",","")))


	x_pos=[i for i, _ in enumerate(years)]

	plt.bar(x_pos, values, color="green")
	plt.xlabel("Year")
	plt.ylabel("Carbon Dioxide emitted (Thousands of tons)")
	plt.title(country + "'s Carbon Dioxide Emissions")
`
	plt.xticks(x_pos, years)
	plt.savefig("carbon-"+ country + ".png")



if __name__ == "__main__":
	main()


