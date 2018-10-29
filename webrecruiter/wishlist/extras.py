import random
import string
from datetime import date
import datetime

from wishlist.models import WishlistItem,Wishlist


def generate_wishlist_item_id():
    print("ENTRYYY")
    date_str = date.today().strftime('%Y%m%d')[2:] + str(datetime.datetime.now().second)
    rand_str = "".join([random.choice(string.digits) for count in range(3)])
    return 'WL{0}{1}'.format(date_str, rand_str)
