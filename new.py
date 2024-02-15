from typing import Dict, Union

def find_lowest_fare(json_data: Dict[str, Dict[str, Union[str, Dict[str, Union[str, int, list]]]]]) -> int:
    """
    Find the lowest fare with key 'GN' from the provided JSON data.

    Args:
        json_data (dict): JSON data containing fare information.

    Returns:
        int: The lowest fare.
    """
    lowest_fare = float('inf')  # Initialize with positive infinity to ensure any fare is lower
    for fare_info in json_data.values():
        gn_fare = fare_info.get("GN")
        if gn_fare and isinstance(gn_fare, int) and gn_fare < lowest_fare:
            lowest_fare = gn_fare
    return lowest_fare

# Example usage:
json_data = {
    "fare": {
        "CC": {
            "GN": 385,
            "TQ": 515,
            "breakup": {
                "GN": [
                    {"text": "Base Charges", "key": "base_fare", "value": 281},
                    {"text": "Reservation Charges", "key": "reservation_charges", "value": 40},
                    {"text": "Superfast Charges", "key": "superfast_charges", "value": 45},
                    {"text": "GST", "key": "service_tax", "value": 19},
                    {"text": "Total Amount", "key": "total", "value": 385}
                ],
                "TQ": [
                    {"text": "Base Charges", "key": "base_fare", "value": 280},
                    {"text": "Reservation Charges", "key": "reservation_charges", "value": 40},
                    {"text": "Superfast Charges", "key": "superfast_charges", "value": 45},
                    {"text": "GST", "key": "service_tax", "value": 25},
                    {"text": "Tatkal Charges", "key": "tatkal_charges", "value": 125},
                    {"text": "Total Amount", "key": "total", "value": 515}
                ]
            }
        },
        "EV": {"GN": "", "TQ": "", "breakup": {}},
        "2S": {
            "GN": 105,
            "TQ": 115,
            "breakup": {
                "GN": [
                    {"text": "Base Charges", "key": "base_fare", "value": 75},
                    {"text": "Reservation Charges", "key": "reservation_charges", "value": 15},
                    {"text": "Superfast Charges", "key": "superfast_charges", "value": 15},
                    {"text": "Total Amount", "key": "total", "value": 105}
                ],
                "TQ": [
                    {"text": "Base Charges", "key": "base_fare", "value": 75},
                    {"text": "Reservation Charges", "key": "reservation_charges", "value": 15},
                    {"text": "Superfast Charges", "key": "superfast_charges", "value": 15},
                    {"text": "Tatkal Charges", "key": "tatkal_charges", "value": 10},
                    {"text": "Total Amount", "key": "total", "value": 115}
                ]
            }
        }
    }
}

lowest_gn_fare = find_lowest_fare(json_data["fare"])
print("Lowest fare with key 'GN':", lowest_gn_fare)