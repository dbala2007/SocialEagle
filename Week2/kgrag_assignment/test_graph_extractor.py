from graph_extractor import GraphExtractor

document = """
Scheme Name:
Micro Nutrient Spray

Department:
Agriculture

Beneficiaries:
Farmers

Types of Benefits:
Subsidy

Description:
All farmers are eligible.
"""

extractor = GraphExtractor()

graph = extractor.extract(document)

print(graph)