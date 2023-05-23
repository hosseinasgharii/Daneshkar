def apply_discount(price: int, discount: float = 0.0)-> int:
    """calculate"""
    final_price = int(price *(1- discount))
    if not 0 <= final_price < price:
        raise ValueError("Invalid Discount")
    
    return final_price