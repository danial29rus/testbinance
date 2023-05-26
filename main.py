import random

from binance.client import Client

api_key = '##############59399490d7a59e3b50c041df356e47#######################'
api_secret = '############e7d9b4a0c0e82173096e19a60be#########################'
symbol = 'BTCUSDT'


def create_orders(client, data):
    volume = float(data['volume'])
    number = data['number']
    amount_dif = float(data['amountDif'])
    side = data['side'].upper()
    price_min = float(data['priceMin'])
    price_max = float(data['priceMax'])

    ticker = client.futures_symbol_ticker(symbol=symbol)
    buy_price = float(ticker['price'])
    print(f"Рынночная цена  ({symbol}): {buy_price}")

    quantity_for_sale = (volume / number) / 20

    try:
        for i in range(number):
            order_price = round(random.uniform(price_min, price_max))

            order_quantity = round(random.uniform(quantity_for_sale + amount_dif, quantity_for_sale - amount_dif), 2)
            print(f'Доля покупки BTC/USDT: {order_quantity}')
            print(f'Цена за которую выставляем order: {order_price}')

            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=client.ORDER_TYPE_LIMIT,
                quantity=order_quantity,
                price=order_price,
                timeInForce=client.TIME_IN_FORCE_GTC
            )

            print(order)
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def main():
    data = {
        "volume": 10,
        "number": 5,
        "amountDif": 0.05,
        "side": "SELL",
        "priceMin": 26000,
        "priceMax": 27500
    }

    client = Client(
        api_key,
        api_secret,
        testnet=True,
    )

    create_orders(client, data)


if __name__ == "__main__":
    main()
