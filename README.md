
# Crop Yield Monitoring System

This is my PROG211 (Object-Oriented Programming 1) individual assignment 1 at Limkokwing University, Sierra Leone. It's a small Python program that keeps track of crops on farms and how much each one yields.

Name: [Osman Abdul Salam Sesay]
Student ID: [905005700]
Class: BSEM1201

## What the program does
- Stores farms and the crops grown on them
- Saves the area, yield and season for each crop
- Works out the yield per hectare
- Lets you update a crop's yield and print all records

## How I built it
- **Farm class:** holds the farm ID and the district
- **Crop class:** holds the crop details and is linked to a Farm
- **Instance methods:** `update_yield()`, `yield_per_hectare()` and `display_info()`
- **Class method:** `get_total_crops()`, which counts how many crops were created
- **Dictionary:** stores all the crops, using the crop ID as the key
- **Tuple:** used for the season, like ("Rainy", 2026)

## How to run it
1. I Install Python
2. I opened the project folder in VS Code
3. I then open 'crop_monitor.py' and then clicked the Run button
4. The crop records print in the terminal

## Sample output
(Added crop C001
Added crop C002
Added crop C003
Added crop C004
Added crop C005
Added crop C006

--- All records ---
[C001] Rice | Farm F001 (Waterloo) | 2.5 ha | 6.0 t | Season: Rainy 2026 | 2.40 t/ha
[C002] Cassava | Farm F002 (Jui) | 1.8 ha | 9.0 t | Season: Dry 2026 | 5.00 t/ha
[C003] Maize | Farm F003 (Portee) | 3.0 ha | 12.0 t | Season: Rainy 2026 | 4.00 t/ha
[C004] Plantain | Farm F004 (Kingtom) | 2.0 ha | 8.0 t | Season: Dry 2026 | 4.00 t/ha
[C005] Beans | Farm F005 (Lumley) | 1.5 ha | 5.0 t | Season: Rainy 2026 | 3.33 t/ha
[C006] Potatoes | Farm F006 (UpGun) | 2.5 ha | 10.0 t | Season: Dry 2026 | 4.00 t/ha

--- Updating C001 yield ---
[C001] Rice | Farm F001 (Waterloo) | 2.5 ha | 7.5 t | Season: Rainy 2026 | 3.00 t/ha

Total crops recorded: 6
PS C:\Users\dell\Desktop\oop prog> 



)

## DPG standards
- **Open-source:** the code is public on GitHub under the MIT License
- **Inclusive and accessible:** it's plain text, so it runs on any computer without internet
- **Privacy-respecting:** I don't store anyone's personal data. Farms only have an ID and a district
- **Modular and reusable:** the classes and functions are separate, so more crops or features can be added later
