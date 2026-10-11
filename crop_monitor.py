"""Crop Yield Monitoring System - PROG211 OOP1 Assignment.

DPG notes: open-source, no personal data stored (farms use IDs and
districts only), simple text interface, modular classes.
"""


class Farm:
    """A farm identified by an ID and district (no personal data)."""

    def __init__(self, farm_id, district):
        self.farm_id = farm_id
        self.district = district

    def display_info(self):
        print(f"Farm {self.farm_id} | District: {self.district}")


class Crop:
    """A crop grown on a farm, with its yield records."""

    total_crops = 0  # class-level counter

    def __init__(self, crop_id, name, farm, area_ha, yield_tonnes, season):
        self.crop_id = crop_id
        self.name = name
        self.farm = farm                  # object interaction: Crop uses Farm
        self.area_ha = area_ha
        self.yield_tonnes = yield_tonnes
        self.season = season              # tuple, e.g. ("Rainy", 2026)
        Crop.total_crops += 1

    # ---- instance methods ----
    def update_yield(self, new_yield):
        self.yield_tonnes = new_yield

    def yield_per_hectare(self):
        return self.yield_tonnes / self.area_ha

    def display_info(self):
        print(f"[{self.crop_id}] {self.name} | Farm {self.farm.farm_id} "
              f"({self.farm.district}) | {self.area_ha} ha | "
              f"{self.yield_tonnes} t | Season: {self.season[0]} {self.season[1]} "
              f"| {self.yield_per_hectare():.2f} t/ha")

    # ---- class method ----
    @classmethod
    def get_total_crops(cls):
        return cls.total_crops


# ---- Data structure: dictionary keyed by crop_id ----
def add_crop(records, crop):
    records[crop.crop_id] = crop
    print(f"Added crop {crop.crop_id}")


def display_crops(records):
    if not records:
        print("No records yet.")
        return
    for crop in records.values():
        crop.display_info()


def main():
    records = {}

    farm1 = Farm("F001", "Waterloo")
    farm2 = Farm("F002", "Jui")
    farm3 = Farm("F003", "Portee")
    farm4 = Farm("F004", "Kingtom")
    farm5 = Farm("F005", "Lumley")
    farm6 = Farm("F006", "UpGun")

    add_crop(records, Crop("C001", "Rice", farm1, 2.5, 6.0, ("Rainy", 2026)))
    add_crop(records, Crop("C002", "Cassava", farm2, 1.8, 9.0, ("Dry", 2026)))
    add_crop(records, Crop("C003", "Maize", farm3, 3.0, 12.0, ("Rainy", 2026)))
    add_crop(records, Crop("C004", "Plantain", farm4, 2.0, 8.0, ("Dry", 2026)))
    add_crop(records, Crop("C005", "Beans", farm5, 1.5, 5.0, ("Rainy", 2026)))
    add_crop(records, Crop("C006", "Potatoes", farm6, 2.5, 10.0, ("Dry", 2026)))

    print("\n--- All records ---")
    display_crops(records)

    print("\n--- Updating C001 yield ---")
    records["C001"].update_yield(7.5)
    records["C001"].display_info()

    print(f"\nTotal crops recorded: {Crop.get_total_crops()}")


if __name__ == "__main__":
    main()