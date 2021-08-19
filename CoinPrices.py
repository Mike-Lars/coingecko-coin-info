import requests
from datetime import datetime


coins = {"bitcoin": "BTC",
         "ethereum": "ETH",
         "cardano": "ADA",
         "chiliz": "CHZ",
         "thorchain": "RUNE",
         "chainlink": "LINK",
         "coti": "COTI"
         }

for network, ticker in coins.items():
    

    url = "https://api.coingecko.com/api/v3/simple/price?ids=" + network + "&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true"
    response = requests.get(url)
    coinData = response.json()


    priceRaw = coinData[network]["usd"]
    priceClean = "${:,.2f}".format(priceRaw)

    mktCapRaw = coinData[network]["usd_market_cap"]
    mktCapClean = "${:,.2f}".format(mktCapRaw)

    changeRaw = coinData[network]["usd_24h_change"]
    changeClean = "{:.2f}%".format(changeRaw)

    volRaw = coinData[network]["usd_24h_vol"]
    volClean = "${:,.2f}".format(volRaw)

    timestampRaw = coinData[network]["last_updated_at"]
    timestampClean = datetime.utcfromtimestamp(timestampRaw).strftime('%Y-%m-%d %H:%M:%S UTC')

    volToCapRaw = (volRaw / mktCapRaw) * 100
    volToCapClean = round(volToCapRaw, 2)
    
    coinsInCircRaw = mktCapRaw / priceRaw
    coinsInCircClean = "{:,}".format(round(coinsInCircRaw))

    


    print()
    print("---" + ticker + "---")
    print()

    print("Price: " + str(priceClean))
    print("Market Cap: " + str(mktCapClean))
    print("24hr Change: " + str(changeClean))
    print()

    print("24hr Volume: " + str(volClean))
    print()

    print("Volume / Market Cap: " + str(volToCapClean) + "%")
    print("Circulating Supply: " + str(coinsInCircClean) + " " + ticker)
    print()
      
print("--- Last Updated: " + str(timestampClean) + " ---")
