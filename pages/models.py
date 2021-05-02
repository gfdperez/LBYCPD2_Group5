from django.db import models


class Drink:
    id: int
    name: str
    subname: str
    price_medium: int
    price_large: int
    image: str
    bgcolor: str
