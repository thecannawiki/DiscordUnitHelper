import unitconversion

tests = []
tests.append("6 gallons and 60 ounces and 3 yards")
tests.append("I use 6 gallons and then feed about 26 oz of cheese")
tests.append("I use 6 gallons and then feed about 26 oz of cheese with like 2 acres")
tests.append("30000 yards")



for t in tests:
    conversion_result = unitconversion.process(t)
    if conversion_result:
        print(t)
        print(conversion_result)


