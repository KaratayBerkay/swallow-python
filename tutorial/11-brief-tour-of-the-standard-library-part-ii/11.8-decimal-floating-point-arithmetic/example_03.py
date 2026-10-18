from decimal import Decimal, getcontext

getcontext().prec = 36
Decimal(1) / Decimal(7)
