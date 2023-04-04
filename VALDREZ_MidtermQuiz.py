class TempConversion:
    def __init__(self,temp):
        self.__temp = temp

    def __fahrenheit_to_celsius(self):
        return (self.__temp - 32) * 5/9

    def __celsius_to_fahrenheit(self):
        return self.__temp * 9/5 + 32

    def __kelvin_to_fahrenheit(self):
        return (self.__temp - 273.15) * 9/5 +32

    def __celsius_to_kelvin(self):
        return self.__temp + 273.15

    def __fahrenheit_to_kelvin(self):
        return (self.__temp - 32) * 5/9 + 273.15

    def get_results(self):
        print(f"Fahrenheit: {self.__temp}")
        print(f"Celsius: {self.__fahrenheit_to_celsius()}")
        print(f"Kelvin: {self.__fahrenheit_to_kelvin()}")

temp_f = float(input("Enter temperature in Fahrenheit: "))

tc = TempConversion(temp_f)

tc.get_results()