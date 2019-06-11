from schematics.models import Model
from schematics.types import URLType, StringType, NumberType
# from schematics.types import URLType, StringType, IntType

class Product(Model):
    year = NumberType(min_value=2018, max_value=2021, strict=False)
    # year = IntType()
    name = StringType(required=True)
    link = URLType(required=True)
