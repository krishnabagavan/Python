# surcharges(extra charges)
# units:1-120 chrage:5.45
# units:120-240 chrage:6.7
# units:240-above chrage:7.7
units=int(input("please enter the units"))
if units<=120:
      charge=units*5.45
      surcharge=15
      money=charge+surcharge
      print(money)
elif units<=240:
      charge=654+(units-120)*6.7
      surcharge=30
      money=charge+surcharge
      print(money)
else:
    charge=654+(units-240)*7.7
    surcharge=45
    money=charge+surcharge
    print(money)