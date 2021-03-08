import matplotlib.pyplot as plt
from tkinter import *
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


def red_green(amount):
    if amount >= 0:
        return "green"
    else:
        return "red"


root = Tk()
root.title("Crypto Currency Portfolio Application")

header_name = Label(root, text="Name", bg="white", font="Verdana 8 bold")
header_name.grid(row=0, column=0, sticky=N + S + E + W)

header_rank = Label(root, text="Rank", bg="silver", font="Verdana 8 bold")
header_rank.grid(row=0, column=1, sticky=N + S + E + W)

header_current_price = Label(root, text="Current Price", bg="white", font="Verdana 8 bold")
header_current_price.grid(row=0, column=2, sticky=N + S + E + W)

header_price_paid = Label(root, text="Price Paid", bg="silver", font="Verdana 8 bold")
header_price_paid.grid(row=0, column=3, sticky=N + S + E + W)

header_profit_loss_per = Label(root, text="Profit/Loss Per", bg="white", font="Verdana 8 bold")
header_profit_loss_per.grid(row=0, column=4, sticky=N + S + E + W)

header_1_hr_change = Label(root, text="1 Hour % Change", bg="silver", font="Verdana 8 bold")
header_1_hr_change.grid(row=0, column=5, sticky=N + S + E + W)

header_24_hr_change = Label(root, text="24 Hour % Change", bg="white", font="Verdana 8 bold")
header_24_hr_change.grid(row=0, column=6, sticky=N + S + E + W)

header_7_day_change = Label(root, text="7 Day % Change", bg="silver", font="Verdana 8 bold")
header_7_day_change.grid(row=0, column=7, sticky=N + S + E + W)

header_current_value = Label(root, text="Current Value", bg="white", font="Verdana 8 bold")
header_current_value.grid(row=0, column=8, sticky=N + S + E + W)

header_profit_loss_total = Label(root, text="Profit/Loss Total", bg="silver", font="Verdana 8 bold")
header_profit_loss_total.grid(row=0, column=9, sticky=N + S + E + W)

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start': '1',
    'limit': '5000',
    'convert': 'USD'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '6fd2b6d4-4b29-4fb9-8e06-bc21f9df8587',
}

session = Session()
session.headers.update(headers)

try:

    def cryptdata():
        row_count = 1
        pie=[]
        pie_size=[]
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        price00 = data['data'][0]['name']
        price01 = data['data'][0]['cmc_rank']
        price02 = data['data'][0]['quote']['USD']['price']
        price03 = data['data'][0]['symbol']
        price04 = data['data'][0]['quote']['USD']['percent_change_1h']
        price05 = data['data'][0]['quote']['USD']['percent_change_24h']
        price06 = data['data'][0]['quote']['USD']['percent_change_7d']
        amount_owned_00 = 1
        price_paid_per_00 = 12000
        total_paid_00 = float(amount_owned_00) * float(price_paid_per_00)
        current_price_00 = float(amount_owned_00) * float(price02)
        profit_loss_00 = current_price_00 - total_paid_00
        profit_loss_per_coin_00 = float(price02) - float(price_paid_per_00)
        pie.append(price00)
        pie_size.append(current_price_00)

        print("---------------------------------------------------------------")
        print(price00)
        print("Rank : {0:.0f}".format(float(price01)))
        print("Current Price = ${0:.2f}".format(float(price02)))
        print("Profit/Loss per coin = ${0:.2f}".format(float(profit_loss_per_coin_00)))
        print(price03)
        print("1 Hour % Change : ${0:.2f}".format(float(price04)))
        print("24 Hour % Change : ${0:.2f}".format(float(price05)))
        print("7 Days % Change : ${0:.2f}".format(float(price06)))
        print("Total Paid : ${0:.2f}".format(float(total_paid_00)))
        print("Current Value : ${0:.2f}".format(float(current_price_00)))
        print("Profit/Loss : ${0:.2f}".format(float(profit_loss_00)))
        name = Label(root, text=price00, bg="white")
        name.grid(row=row_count, column=0, sticky=N + S + E + W)

        rank = Label(root, text=price01, bg="silver")
        rank.grid(row=row_count, column=1, sticky=N + S + E + W)

        current_price = Label(root, text="${0:.2f}".format(float(price02)), bg="white")
        current_price.grid(row=row_count, column=2, sticky=N + S + E + W)

        price_paid = Label(root, text="${0:.2f}".format(float(total_paid_00)), bg="silver")
        price_paid.grid(row=row_count, column=3, sticky=N + S + E + W)

        profit_loss_per = Label(root, text="${0:.2f}".format(float(profit_loss_per_coin_00)), bg="white", fg = red_green(profit_loss_per_coin_00))
        profit_loss_per.grid(row=row_count, column=4, sticky=N + S + E + W)

        one_hr_change = Label(root, text="${0:.2f}".format(float(price04)), bg="silver",fg=red_green(price04))
        one_hr_change.grid(row=row_count, column=5, sticky=N + S + E + W)

        tf_hr_change = Label(root, text="${0:.2f}".format(float(price05)), bg="white",fg=red_green(price05))
        tf_hr_change.grid(row=row_count, column=6, sticky=N + S + E + W)

        seven_day_change = Label(root, text="${0:.2f}".format(float(price06)), bg="silver",fg=red_green(price06))
        seven_day_change.grid(row=row_count, column=7, sticky=N + S + E + W)

        current_value = Label(root, text=" ${0:.2f}".format(float(current_price_00)), bg="white")
        current_value.grid(row=row_count, column=8, sticky=N + S + E + W)

        profit_loss_total = Label(root, text="${0:.2f}".format(float(profit_loss_00)), bg="silver", fg = red_green(profit_loss_00))
        profit_loss_total.grid(row=row_count, column=9, sticky=N + S + E + W)
        row_count += 1
        print("----------------------------------------------------------------")
        price10 = data['data'][1]['name']
        price11 = data['data'][1]['cmc_rank']
        price12 = data['data'][1]['quote']['USD']['price']
        price13 = data['data'][1]['symbol']
        price14 = data['data'][1]['quote']['USD']['percent_change_1h']
        price15 = data['data'][1]['quote']['USD']['percent_change_24h']
        price16 = data['data'][1]['quote']['USD']['percent_change_7d']
        amount_owned_10 = 30
        price_paid_per_10 = 11
        total_paid_10 = float(amount_owned_10) * float(price_paid_per_10)
        current_price_10 = float(amount_owned_10) * float(price12)
        profit_loss_10 = current_price_10 - total_paid_10
        profit_loss_per_coin_10 = float(price12) - float(price_paid_per_10)
        pie.append(price10)
        pie_size.append(current_price_10)
        print(price10)
        print("Rank : {0:.0f}".format(float(price11)))
        print("Current Price = ${0:.2f}".format(float(price12)))
        print("Profit/Loss per coin = ${0:.2f}".format(float(profit_loss_per_coin_10)))
        print(price13)
        print("1 Hour % Change : ${0:.2f}".format(float(price14)))
        print("24 Hour % Change : ${0:.2f}".format(float(price15)))
        print("7 Days % Change : ${0:.2f}".format(float(price16)))
        print("Total Paid : ${0:.2f}".format(float(total_paid_10)))
        print("Current Value : ${0:.2f}".format(float(current_price_10)))
        print("Profit/Loss : ${0:.2f}".format(float(profit_loss_10)))
        name = Label(root, text=price10, bg="white")
        name.grid(row=row_count, column=0, sticky=N + S + E + W)

        rank = Label(root, text=price11, bg="silver")
        rank.grid(row=row_count, column=1, sticky=N + S + E + W)

        current_price = Label(root, text="${0:.2f}".format(float(price12)), bg="white")
        current_price.grid(row=row_count, column=2, sticky=N + S + E + W)

        price_paid = Label(root, text="${0:.2f}".format(float(total_paid_10)), bg="silver")
        price_paid.grid(row=row_count, column=3, sticky=N + S + E + W)

        profit_loss_per = Label(root, text="${0:.2f}".format(float(profit_loss_per_coin_10)), bg="white", fg = red_green(profit_loss_per_coin_10))
        profit_loss_per.grid(row=row_count, column=4, sticky=N + S + E + W)

        one_hr_change = Label(root, text="${0:.2f}".format(float(price14)), bg="silver",fg=red_green(price14))
        one_hr_change.grid(row=row_count, column=5, sticky=N + S + E + W)

        tf_hr_change = Label(root, text="${0:.2f}".format(float(price15)), bg="white",fg=red_green(price15))
        tf_hr_change.grid(row=row_count, column=6, sticky=N + S + E + W)

        seven_day_change = Label(root, text="${0:.2f}".format(float(price16)), bg="silver",fg=red_green(price16))
        seven_day_change.grid(row=row_count, column=7, sticky=N + S + E + W)

        current_value = Label(root, text=" ${0:.2f}".format(float(current_price_10)), bg="white")
        current_value.grid(row=row_count, column=8, sticky=N + S + E + W)

        profit_loss_total = Label(root, text="${0:.2f}".format(float(profit_loss_10)), bg="silver", fg = red_green(profit_loss_10))
        profit_loss_total.grid(row=row_count, column=9, sticky=N + S + E + W)
        row_count += 1
        print("----------------------------------------------------------------")
        price20 = data['data'][2]['name']
        price21 = data['data'][2]['cmc_rank']
        price22 = data['data'][2]['quote']['USD']['price']
        price23 = data['data'][2]['symbol']
        price24 = data['data'][2]['quote']['USD']['percent_change_1h']
        price25 = data['data'][2]['quote']['USD']['percent_change_24h']
        price26 = data['data'][2]['quote']['USD']['percent_change_7d']
        amount_owned_20 = 1773
        price_paid_per_20 = 16.23
        total_paid_20 = float(amount_owned_20) * float(price_paid_per_20)
        current_price_20 = float(amount_owned_20) * float(price22)
        profit_loss_20 = current_price_20 - total_paid_20
        profit_loss_per_coin_20 = float(price22) - float(price_paid_per_20)
        pie.append(price20)
        pie_size.append(current_price_20)
        print(price20)
        print("Rank : {0:.0f}".format(float(price21)))
        print("Current Price = ${0:.2f}".format(float(price22)))
        print("Profit/Loss per coin = ${0:.2f}".format(float(profit_loss_per_coin_20)))
        print(price23)
        print("1 Hour % Change : ${0:.2f}".format(float(price24)))
        print("24 Hour % Change : ${0:.2f}".format(float(price25)))
        print("7 Days % Change : ${0:.2f}".format(float(price26)))
        print("Total Paid : ${0:.2f}".format(float(total_paid_20)))
        print("Current Value : ${0:.2f}".format(float(current_price_20)))
        print("Profit/Loss : ${0:.2f}".format(float(profit_loss_20)))
        name = Label(root, text=price20, bg="white")
        name.grid(row=row_count, column=0, sticky=N + S + E + W)

        rank = Label(root, text=price21, bg="silver")
        rank.grid(row=row_count, column=1, sticky=N + S + E + W)

        current_price = Label(root, text="${0:.2f}".format(float(price22)), bg="white")
        current_price.grid(row=row_count, column=2, sticky=N + S + E + W)

        price_paid = Label(root, text="${0:.2f}".format(float(total_paid_20)), bg="silver")
        price_paid.grid(row=row_count, column=3, sticky=N + S + E + W)

        profit_loss_per = Label(root, text="${0:.2f}".format(float(profit_loss_per_coin_20)), bg="white",fg = red_green(profit_loss_per_coin_20))
        profit_loss_per.grid(row=row_count, column=4, sticky=N + S + E + W)

        one_hr_change = Label(root, text="${0:.2f}".format(float(price24)), bg="silver",fg=red_green(price24))
        one_hr_change.grid(row=row_count, column=5, sticky=N + S + E + W)

        tf_hr_change = Label(root, text="${0:.2f}".format(float(price25)), bg="white",fg=red_green(price25))
        tf_hr_change.grid(row=row_count, column=6, sticky=N + S + E + W)

        seven_day_change = Label(root, text="${0:.2f}".format(float(price26)), bg="silver",fg=red_green(price26))
        seven_day_change.grid(row=row_count, column=7, sticky=N + S + E + W)

        current_value = Label(root, text=" ${0:.2f}".format(float(current_price_20)), bg="white")
        current_value.grid(row=row_count, column=8, sticky=N + S + E + W)

        profit_loss_total = Label(root, text="${0:.2f}".format(float(profit_loss_20)), bg="silver",fg = red_green(profit_loss_20))
        profit_loss_total.grid(row=row_count, column=9, sticky=N + S + E + W)
        row_count += 1
        print("----------------------------------------------------------------")
        price30 = data['data'][3]['name']
        price31 = data['data'][3]['cmc_rank']
        price32 = data['data'][3]['quote']['USD']['price']
        price33 = data['data'][3]['symbol']
        price34 = data['data'][3]['quote']['USD']['percent_change_1h']
        price35 = data['data'][3]['quote']['USD']['percent_change_24h']
        price36 = data['data'][3]['quote']['USD']['percent_change_7d']
        amount_owned_30 = 33000
        price_paid_per_30 = 0.45
        total_paid_30 = float(amount_owned_30) * float(price_paid_per_30)
        current_price_30 = float(amount_owned_30) * float(price32)
        profit_loss_30 = current_price_30 - total_paid_30
        profit_loss_per_coin_30 = float(price32) - float(price_paid_per_30)
        pie.append(price30)
        pie_size.append(current_price_30)
        print(price30)
        print("Rank : {0:.0f}".format(float(price31)))
        print("Current Price = ${0:.2f}".format(float(price32)))
        print("Profit/Loss per coin = ${0:.2f}".format(float(profit_loss_per_coin_30)))
        print(price33)
        print("1 Hour % Change : ${0:.2f}".format(float(price34)))
        print("24 Hour % Change : ${0:.2f}".format(float(price35)))
        print("7 Days % Change : ${0:.2f}".format(float(price36)))
        print("Total Paid : ${0:.2f}".format(float(total_paid_30)))
        print("Current Value : ${0:.2f}".format(float(current_price_30)))
        print("Profit/Loss : ${0:.2f}".format(float(profit_loss_30)))
        name = Label(root, text=price30, bg="white")
        name.grid(row=row_count, column=0, sticky=N + S + E + W)

        rank = Label(root, text=price31, bg="silver")
        rank.grid(row=row_count, column=1, sticky=N + S + E + W)

        current_price = Label(root, text="${0:.2f}".format(float(price32)), bg="white")
        current_price.grid(row=row_count, column=2, sticky=N + S + E + W)

        price_paid = Label(root, text="${0:.2f}".format(float(total_paid_30)), bg="silver")
        price_paid.grid(row=row_count, column=3, sticky=N + S + E + W)

        profit_loss_per = Label(root, text="${0:.2f}".format(float(profit_loss_per_coin_30)), bg="white",fg = red_green(profit_loss_per_coin_30))
        profit_loss_per.grid(row=row_count, column=4, sticky=N + S + E + W)

        one_hr_change = Label(root, text="${0:.2f}".format(float(price34)), bg="silver",fg=red_green(price34))
        one_hr_change.grid(row=row_count, column=5, sticky=N + S + E + W)

        tf_hr_change = Label(root, text="${0:.2f}".format(float(price35)), bg="white",fg=red_green(price35))
        tf_hr_change.grid(row=row_count, column=6, sticky=N + S + E + W)

        seven_day_change = Label(root, text="${0:.2f}".format(float(price36)), bg="silver",fg=red_green(price36))
        seven_day_change.grid(row=row_count, column=7, sticky=N + S + E + W)

        current_value = Label(root, text=" ${0:.2f}".format(float(current_price_30)), bg="white")
        current_value.grid(row=row_count, column=8, sticky=N + S + E + W)

        profit_loss_total = Label(root, text="${0:.2f}".format(float(profit_loss_30)), bg="silver", fg = red_green(profit_loss_30))
        profit_loss_total.grid(row=row_count, column=9, sticky=N + S + E + W)
        row_count += 1
        print("----------------------------------------------------------------")
        price40 = data['data'][4]['name']
        price41 = data['data'][4]['cmc_rank']
        price42 = data['data'][4]['quote']['USD']['price']
        price43 = data['data'][4]['symbol']
        price44 = data['data'][4]['quote']['USD']['percent_change_1h']
        price45 = data['data'][4]['quote']['USD']['percent_change_24h']
        price46 = data['data'][4]['quote']['USD']['percent_change_7d']
        amount_owned_40 = 600
        price_paid_per_40 = 0.33
        total_paid_40 = float(amount_owned_40) * float(price_paid_per_40)
        current_price_40 = float(amount_owned_40) * float(price42)
        profit_loss_40 = current_price_40 - total_paid_40
        profit_loss_per_coin_40 = float(price42) - float(price_paid_per_40)
        pie.append(price40)
        pie_size.append(current_price_40)
        print(price40)
        print("Rank : {0:.0f}".format(float(price41)))
        print("Current Price = ${0:.2f}".format(float(price42)))
        print("Profit/Loss per coin = ${0:.2f}".format(float(profit_loss_per_coin_40)))
        print(price43)
        print("1 Hour % Change : ${0:.2f}".format(float(price44)))
        print("24 Hour % Change : ${0:.2f}".format(float(price45)))
        print("7 Days % Change : ${0:.2f}".format(float(price46)))
        print("Total Paid : ${0:.2f}".format(float(total_paid_40)))
        print("Current Value : ${0:.2f}".format(float(current_price_40)))
        print("Profit/Loss : ${0:.2f}".format(float(profit_loss_40)))
        name = Label(root, text=price40, bg="white")
        name.grid(row=row_count, column=0, sticky=N + S + E + W)

        rank = Label(root, text=price41, bg="silver")
        rank.grid(row=row_count, column=1, sticky=N + S + E + W)

        current_price = Label(root, text="${0:.2f}".format(float(price42)), bg="white")
        current_price.grid(row=row_count, column=2, sticky=N + S + E + W)

        price_paid = Label(root, text="${0:.2f}".format(float(total_paid_40)), bg="silver")
        price_paid.grid(row=row_count, column=3, sticky=N + S + E + W)

        profit_loss_per = Label(root, text="${0:.2f}".format(float(profit_loss_per_coin_40)), bg="white", fg = red_green(profit_loss_per_coin_40))
        profit_loss_per.grid(row=row_count, column=4, sticky=N + S + E + W)

        one_hr_change = Label(root, text="${0:.2f}".format(float(price44)), bg="silver",fg=red_green(price44))
        one_hr_change.grid(row=row_count, column=5, sticky=N + S + E + W)

        tf_hr_change = Label(root, text="${0:.2f}".format(float(price45)), bg="white",fg=red_green(price45))
        tf_hr_change.grid(row=row_count, column=6, sticky=N + S + E + W)

        seven_day_change = Label(root, text="${0:.2f}".format(float(price46)), bg="silver",fg=red_green(price46))
        seven_day_change.grid(row=row_count, column=7, sticky=N + S + E + W)

        current_value = Label(root, text=" ${0:.2f}".format(float(current_price_40)), bg="white")
        current_value.grid(row=row_count, column=8, sticky=N + S + E + W)

        profit_loss_total = Label(root, text="${0:.2f}".format(float(profit_loss_40)), bg="silver",fg=red_green(profit_loss_40))
        profit_loss_total.grid(row=row_count, column=9, sticky=N + S + E + W)
        row_count += 1
        print("----------------------------------------------------------------")

        total_current_value = current_price_00 + current_price_10 + current_price_20 + current_price_30 + current_price_40
        root.title("Crypto Currency Portfolio Application - Portfolio Value : ${0:.2f}".format(float(total_current_value)))

        portfolio_profit_loss = profit_loss_00 + profit_loss_10 + profit_loss_20 + profit_loss_30 + profit_loss_40
        print("Portfolio Profit/Loss : ${0:.2f}".format(float(portfolio_profit_loss)))
        portfolio_profit_loss = Label(root, text="Portfolio Profit/Loss : $ {0:.2f}".format(float(portfolio_profit_loss)),font="Verdana 8 bold", fg=red_green(portfolio_profit_loss))
        portfolio_profit_loss.grid(row=row_count, column=0, sticky=W, padx=10,pady=10)

        data = ""
        update_button = Button(root, text="Update Prices",command=cryptdata)
        update_button.grid(row=row_count, column=9, sticky=E+S, padx=10, pady=10)


        def graph(pie,pie_size):
            labels = pie
            sizes = pie_size
            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
            #ax1.axis('equal')
            plt.show()

        graph_button = Button(root, text="Pie Chart", command=graph(pie,pie_size))
        graph_button.grid(row=row_count, column=8, sticky=E + S, padx=10, pady=10)


except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)


cryptdata()
root.mainloop()
