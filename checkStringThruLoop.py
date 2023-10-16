mars_temperature = "The highest temperature on Mars is about 30 C"
for item  in mars_temperature.split():
    if item.isnumeric():
        print(item)
//Like the .isnumeric() method, .isdecimal() can check for strings that look like decimals.
