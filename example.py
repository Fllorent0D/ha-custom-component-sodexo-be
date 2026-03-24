import asyncio

from pluxee import PluxeeAsyncClient


async def main():
    username = input("Username: (leave empty to use PLUXEE_USERNAME env variable)")
    password = input("password: (leave empty to use PLUXEE_PASSWORD env variable)")

    pc = PluxeeAsyncClient(username, password)

    balance = await pc.get_balance()
    print(balance)
    # Will return a PluxeeBalance object with those attributes
    # lunch_pass: 89.19
    # eco_pass: 396.16
    # gift_pass: 0.0
    # conso_pass: 0.0


asyncio.get_event_loop().run_until_complete(main())
