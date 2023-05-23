class DiscountError(Exception):
    pass

def integer_discount(function):

    def wrapper(price: int, discount:int)-> int:
        return function(price , discount / 60)
    
    return wrapper


@integer_discount  #میاد رفتارشو به اون دکوریتورمون دگ تغییر میده
def apply_discount(price: int, discount: float = 0.0)-> int:
    """calculates the final price after discount"""
    final_price = int(price *(1- discount))
    if not 0 <= final_price < price:
        raise ValueError("Invalid Discount")
    
    return final_price


