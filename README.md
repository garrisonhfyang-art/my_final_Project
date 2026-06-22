mport numpy as pd
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class House:
    def __init__(self, house_id, block, bedrooms, price, status="Available"):
        self.house_id = house_id
        self.block = block
        self.bedrooms = bedrooms
        self.price = price
        self.status = status  # Available, Sold, or Rented

class HousingEstate:
    def __init__(self, name):
        self.name = name
        self.properties = []

    def add_house(self, house):
        self.properties.append(house)

    def update_status(self, house_id, new_status):
        for house in self.properties:
            if house.house_id == house_id:
                house.status = new_status
                print(f"House {house_id} updated to {new_status}.\n")
                return
        print("House ID not found.")

    def display_estate(self):
        # Convert objects to a dictionary list for a clean Pandas DataFrame view
        data = [vars(h) for h in self.properties]
        df = pd.DataFrame(data)
        print(f"--- {self.name} Status Report ---")
        print(df.to_string(index=False))
        print("-" * 35)

# --- Quick Demonstration ---
if __name__ == "__main__":
    # Create the estate
    my_estate = HousingEstate("Greenwood Estates")

    # Add sample properties (ID, Block, Bedrooms, Price)
    my_estate.add_house(House("H101", "Block A", 3, 250000))
    my_estate.add_house(House("H102", "Block A", 4, 310000))
    my_estate.add_house(House("H201", "Block B", 2, 195000))

    # Show initial state
    my_estate.display_estate()

    # Simulate selling a house
    my_estate.update_status("H101", "Sold")

    # Show updated estate layout
    my_estate.display_estate()
