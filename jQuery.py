import time
import random
class Constant:
    jQuery_Version = "1.1.2"

def get_current_timestamp() -> int:
    return int(round(time.time() * 1000))

def jquery_mock_callback() -> str:
    random_number_str = ''.join(random.choices('0123456789', k=18))
    return "jQuery" + (Constant.jQuery_Version + random_number_str).replace(".", "") + "_" + str(get_current_timestamp())
    