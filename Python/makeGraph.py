import matplotlib as mpl
import matplotlib.pyplot as plt
from random import randint
from pymongo import MongoClient
plt.style.use("ggplot")

host = "mongodb://localhost:27017"
client = MongoClient(host)
db = client["gw_data"]
col = db["methane_emissions"]


def main():
    years = []
    country = input("Country? ")
    values = []

    q = {"GEO":country}

    doc = col.find(q)

    for x in doc:
        years.append(x["TIME"])
        values.append(float(x["Value"].replace(",","")))



    x_pos=[i for i, _ in enumerate(years)]

    plt.bar(x_pos, values, color="green")
    plt.xlabel("Year")
    plt.ylabel("Mehtane emitted (Thousands of tons)")

    #plt.axis([xmin, xmax, ymin, ymax])
    #By setting the x values to None matplotlib will work it out itself
    plt.axis([None, None, round(min(values)) - 100, round(max(values)) + 50])

    plt.title(country + "'s Methane Emissions")

    plt.xticks(x_pos, years)
    plt.show()



if __name__ == "__main__":
	main()



