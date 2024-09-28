import python_weather
import asyncio

async def getweather():

    client = python_weather.Client(format=python_weather.IMPERIAL)

    weather = await client.find("Moscow")

    celcius = (weather.current.temperature -32) * 5/9

    print (str(round(celcius)) + "°")

    print(weather.current.sky_text)

    print(weather.location_name)

    await client.close()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(getweather())