from generateReport import GenerateReport

generator = GenerateReport()
json = generator.generateReport("bitcoin")

print(json)