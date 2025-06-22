def convert_distance(distance: float, from_unit: str, to_unit: str) -> float:
    """Converts distance from one unit to another using meters as base."""
    unit_aliases = {
        # Metric
        "millimeter": "mm", "millimetre": "mm", "millimeters": "mm", "millimetres": "mm", "mm": "mm",
        "centimeter": "cm", "centimetre": "cm", "centimeters": "cm", "centimetres": "cm", "cm": "cm",
        "meter": "m", "metre": "m", "meters": "m", "metres": "m", "m": "m",
        "kilometer": "km", "kilometre": "km", "kilometers": "km", "kilometres": "km", "km": "km", "kms": "km",

        # Imperial
        "inch": "inch", "inches": "inch", "in": "inch",
        "foot": "foot", "feet": "foot", "ft": "foot",
        "yard": "yard", "yards": "yard", "yd": "yard",
        "mile": "mile", "miles": "mile", "mi": "mile"
    }

    from_unit = unit_aliases.get(from_unit.lower().strip(), from_unit.lower().strip())
    to_unit = unit_aliases.get(to_unit.lower().strip(), to_unit.lower().strip())

    unit_to_meter = {
        "mm": 1e-3,
        "cm": 1e-2,
        "m": 1,
        "km": 1e3,
        "inch": 0.0254,
        "foot": 0.3048,
        "yard": 0.9144,
        "mile": 1609.34
    }

    if from_unit not in unit_to_meter or to_unit not in unit_to_meter:
        return f"Sorry, conversion from {from_unit} to {to_unit} is not supported yet."

    # Convert from source unit to meters
    value_in_meters = distance * unit_to_meter[from_unit]

    # Convert from meters to target unit
    converted_value = value_in_meters / unit_to_meter[to_unit]

    return round(converted_value, 6)  # rounded for neatness