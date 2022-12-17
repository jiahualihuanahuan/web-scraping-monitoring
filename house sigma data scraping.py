from bs4 import BeautifulSoup
import os
import pandas as pd
import numpy as np

# set up dataframe header
column_header = ["address",
                "city",
                "house_type",
                "list_price",
                "sold_price",
                 "sold_date",
                "estimate_price",
                "estimate_date",
                "tax",
                "tax_year",
                "building_age",
                "size",
                "lot_size",
                "parking",
                "basement",
                "listing_num",
                "data_source",
                "days_on_market",
                "listed_on",
                "updated_on",
                "property_type",
                "style",
                "fronting_on",
                "community",
                "municipality",
                "bedrooms",
                "bathrooms",
                "basement_type",
                "kitchens",
                "rooms",
                "central_vac",
                "fireplace",
                "water",
                "cooling",
                "heating_type",
                "feating_fuel",
                "construction",
                "driveway",
                "garage_type",
                "garage",
                "parking_spaces",
                "total_parking_space",
                "park",
                "public_transit",
                "school",
                "sewer",
                "frontage",
                "depth",
                "lot_size_code",
                "cross_street",
                "family_room",
                "zoning"]
# set up dataframes
house_df = pd.DataFrame(columns = column_header)
new_df = pd.DataFrame(columns = column_header)

# set you data path
path = "your/data/path/house_sigma_html"

# main scraping section
for file in os.listdir(path):
    if file[-5:] == ".html":
        # initialize all variables with NAN
        address = np.nan
        city = np.nan
        house_type = np.nan
        list_price = np.nan
        sold_price = np.nan
        sold_date = np.nan
        estimate_price = np.nan
        estimate_date = np.nan
        tax = np.nan
        tax_year = np.nan
        building_age = np.nan
        lot_size = np.nan
        size = np.nan
        lot_size = np.nan
        parking = np.nan
        basement = np.nan
        listing_num = np.nan
        data_source = np.nan
        days_on_market = np.nan
        listed_on = np.nan
        updated_on = np.nan
        property_type = np.nan
        style = np.nan
        fronting_on = np.nan
        community = np.nan
        municipality = np.nan
        bedrooms = np.nan
        bathrooms = np.nan
        basement_type = np.nan
        kitchens = np.nan
        rooms = np.nan
        central_vac = np.nan
        fireplace = np.nan
        water = np.nan
        cooling = np.nan
        heating_type = np.nan
        feating_fuel = np.nan
        construction = np.nan
        driveway = np.nan
        garage_type = np.nan
        garage = np.nan
        parking_spaces = np.nan
        total_parking_space = np.nan
        park = np.nan
        public_transit = np.nan
        school = np.nan
        sewer = np.nan
        frontage = np.nan
        depth = np.nan
        lot_size_code = np.nan
        cross_street = np.nan
        family_room = np.nan
        zoning = np.nan
        with open(f"{path}/{file}", "r", encoding='utf-8') as f:
            html= f.read()
        soup = BeautifulSoup(html, 'html.parser')
        address = soup.find("div", {"class": "address"}).get_text()
        i = len(address)
        try:
            city = soup.find_all("div", {"class": "city_name"})[-1].get_text()
        except:
            print(f"city for {address} is not available")
        try:
            house_type = soup.find_all("div", {"class": "house_type"})[-1].get_text()
        except:
            print(f"house_type for {address} is not available")
        try:
            list_price = soup.find_all("div", {"class": "price_listing"})[-1].get_text().replace("Listed for:  $", "").replace(",", "").strip()
        except:
            print(f"list_price for {address} is not available")
        try:
            sold_price = soup.find_all("div", {"class": "price_sold"})[-1].get_text().replace("Sold for: $", "").replace(",", "").strip()
        except:
            print(f"sold_price for {address} is not available")
        try:
            sold_date = soup.find_all("span", {"class": "list_days"})[-1].get_text().replace("Sold in ", "")
        except:
            print(f"sold_date for {address} is not available")
        try:
            estimate_price = soup.find_all("div", {"class": "estimate_price"})[-1].get_text().replace("Estimated value $", "").replace(",", "").split(" ")[0]
        except:
            print(f"estimate_price for {address} is not available")
        try:
            estimate_date = soup.find_all("div", {"class": "estimate_price"})[-1].get_text().replace("Estimated value $", "").split(" ")[-1]
        except:
            print(f"estimate_date for {address} is not available")
        # key facts
        for div in soup.find_all("div", {"class": "each_column_container el-col el-col-12"}):
            for item in div.find_all("div", {"class": "item"}):
                if 'Tax:' in item.get_text():
                    tax = item.find("span").get_text().replace("$", "").replace(" ", "").replace(",", "").split("/")[0]
                    tax_year = item.find("span").get_text().replace("$", "").replace(" ", "").split("/")[1]
                elif 'Building Age:' in item.get_text():
                    building_age = item.find("span").get_text()
                elif 'Lot Size:' in item.get_text():
                    lot_size = item.find("span").get_text()
                elif ('Size:' in item.get_text()) & ('Lot Size:' not in item.get_text()):
                    size = item.find("span").get_text()
                elif 'Parking:' in item.get_text():
                    parking = item.find("span").get_text()
                elif 'Listing #:' in item.get_text():
                    listing_num = item.find("span").get_text()
                elif 'Data Source:' in item.get_text():
                    data_source = item.find("span").get_text()
                elif 'Days on Market:' in item.get_text():
                    days_on_market = item.find("span").get_text()
                elif 'Listed on:' in item.get_text():
                    listed_on = item.find("span").get_text()
                elif 'Updated on:' in item.get_text():
                    updated_on = item.find("span").get_text()
                else:
                    pass
        # property details
        for div in soup.find_all("div", {"class": "property_details_body two_column_data el-row"}):
            for item in div.find_all("div", {"class": "item"}):
                if 'Property Type:' in item.get_text():
                        property_type = item.find("span").get_text()
                elif 'Style:' in item.get_text():
                        style = item.find("span").get_text()
                elif 'Fronting on:' in item.get_text():
                        fronting_on = item.find("span").get_text()
                elif 'Community:' in item.get_text():
                        community = item.find("span").get_text()
                elif 'Municipality:' in item.get_text():
                        municipality = item.find("span").get_text()
                elif 'Bedrooms:' in item.get_text():
                        bedrooms = item.find("span").get_text()
                elif 'Bathrooms:' in item.get_text():
                        bathrooms = item.find("span").get_text()
                elif 'Basement Type:' in item.get_text():
                        basement_type = item.find("span").get_text()
                elif 'Kitchens:' in item.get_text():
                        kitchens = item.find("span").get_text()
                elif 'Rooms:' in item.get_text():
                        rooms = item.find("span").get_text()
                elif 'Family Room:' in item.get_text():
                        family_room = item.find("span").get_text()
                elif 'Central Vac:' in item.get_text():
                        central_vac = item.find("span").get_text()
                elif 'Fireplace:' in item.get_text():
                        fireplace = item.find("span").get_text()
                elif 'Water:' in item.get_text():
                        water = item.find("span").get_text()
                elif 'Cooling:' in item.get_text():
                        cooling = item.find("span").get_text()
                elif 'Heating Type:' in item.get_text():
                        heating_type = item.find("span").get_text()
                elif 'Heating Fuel:' in item.get_text():
                        feating_fuel = item.find("span").get_text()
                elif 'Construction:' in item.get_text():
                        construction = item.find("span").get_text()
                elif 'Driveway:' in item.get_text():
                        driveway = item.find("span").get_text()
                elif 'Garage Type:' in item.get_text():
                        garage_type = item.find("span").get_text()
                elif 'Garage:' in item.get_text():
                        garage = item.find("span").get_text()
                elif 'Parking Places:' in item.get_text():
                        parking_spaces = item.find("span").get_text()
                elif 'Total Parking Space:' in item.get_text():
                        total_parking_space = item.find("span").get_text()
                elif 'Park:' in item.get_text():
                        park = item.find("span").get_text()
                elif 'Public Transit:' in item.get_text():
                        public_transit = item.find("span").get_text()
                elif 'School:' in item.get_text():
                        school = item.find("span").get_text()
                elif 'Sewer:' in item.get_text():
                        sewer = item.find("span").get_text()
                elif 'Frontage:' in item.get_text():
                        frontage = item.find("span").get_text()
                elif 'Depth:' in item.get_text():
                        depth = item.find("span").get_text()
                elif 'Zoning:' in item.get_text():
                        zoning = item.find("span").get_text()
                elif 'Lot Size Code:' in item.get_text():
                        lot_size_code = item.find("span").get_text()
                elif 'Cross Street:' in item.get_text():
                        cross_street = item.find("span").get_text()
                else:
                    pass
        new_df.loc[0] = [address,
                        city,
                        house_type,
                        list_price,
                        sold_price,
                        sold_date,
                        estimate_price,
                        estimate_date,
                        tax,
                        tax_year,
                        building_age,
                        size,
                        lot_size,
                        parking,
                        basement,
                        listing_num,
                        data_source,
                        days_on_market,
                        listed_on,
                        updated_on,
                        property_type,
                        style,
                        fronting_on,
                        community,
                        municipality,
                        bedrooms,
                        bathrooms,
                        basement_type,
                        kitchens,
                        rooms,
                        central_vac,
                        fireplace,
                        water,
                        cooling,
                        heating_type,
                        feating_fuel,
                        construction,
                        driveway,
                        garage_type,
                        garage,
                        parking_spaces,
                        total_parking_space,
                        park,
                        public_transit,
                        school,
                        sewer,
                        frontage,
                        depth,
                        lot_size_code,
                        cross_street,
                        family_room,
                        zoning]
        house_df = pd.concat([house_df, new_df], ignore_index = True)
# check data
house_df.info()

house_df.describe()

# write on disk
house_df.to_csv("house_data.csv")  
