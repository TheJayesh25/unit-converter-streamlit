def convert_temperature(temperature: float, from_unit: str, to_unit: str) -> float:
    """This function converts temperature from one unit to another using Celsius as base"""

    ### HELPER FUNCTION 
    def conversion(value_in_celsius, to_unit):
        if to_unit in ['fahrenheit','f']:
            return (value_in_celsius * 9/5) + 32
    
        if to_unit in ['kelvin','k']:
            return value_in_celsius + 273.15

    from_unit = from_unit.lower().strip()
    to_unit = to_unit.lower().strip()

    value_in_celsius = temperature

    if from_unit in ['fahrenheit','f']:
        value_in_celsius = (temperature - 32) * 5/9
    
    if from_unit in ['kelvin','k']:
        value_in_celsius = temperature - 273.15

    converted_value = conversion(value_in_celsius, to_unit)
    return round(converted_value, 6)
