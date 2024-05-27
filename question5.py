# Question 5 Task 1 

def merge_catalogs(*catalogs):
    combined_catalog = ()
    for catalog in catalogs:
        combined_catalog += catalog
    return combined_catalog

# Example Catalogs
catalog1 = (("Laptop", 1000), ("Camera", 500))
catalog2 = (("Smartphone", 800), ("Tablet", 450))
catalog3 = (("Headphones", 200), ("Monitor", 300))

# Example usage
combined_catalog = merge_catalogs(catalog1, catalog2, catalog3)
print(combined_catalog)
