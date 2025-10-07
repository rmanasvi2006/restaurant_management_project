import string , secrets
from .models import Coupon

def generate_coupon_code(length = 10):
    char = string.ascii_uppercase + string.digits
    while True:
        code = ''.join(secrets.choice(chars) for _ in range (length))
        if not
        Coupon.objects.filter(code=code).exists(  ):
        return code