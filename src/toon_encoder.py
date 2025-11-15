from toon_format import encode, estimate_savings

def toon_encode_data(data: dict) -> dict:
    """
    Encodes the given data dictionary using the toon format encoder.

    Args:
        data (dict): The input data to be encoded.

    Returns:
        dict: The encoded data in toon format.
    """
    encoded_data, savings = encode(data), estimate_savings(data)
    print("-----------------------------------")
    print(f"Estimated savings: {savings:.2f}%")
    print("-----------------------------------")
    return encoded_data