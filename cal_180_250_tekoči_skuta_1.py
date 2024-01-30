import datetime

#def ask_for_yogurt(taste, size):
#    print(f"Vpiši koliko {size}g lončkov {taste} jogurta želiš narediti.")
#    return float(input())

def ask_for_yogurt(taste, size):
    if size == 500:  # Check if the size is 500g (liquid yogurt)
        print(f"Vpiši koliko 0,5L steklenic {taste} tekočega jogurta želiš narediti.")
    elif size == 1000:  # Check if the size is 1000g (larger liquid yogurt)
        print(f"Vpiši koliko 1L steklenic {taste} tekočega jogurta želiš narediti.")    
    else:
        print(f"Vpiši koliko {size}g lončkov {taste} jogurta želiš narediti.")
    return float(input())

sizes = [180, 250, 500]  # Added 500g for liquid yogurt
tastes_180 = ['jagodnega', 'borovničevega', 'vanilijevega', 'mareličnega', 'zimskega', 'navadnega']
tastes_250 = ['jagodnega', 'borovničevega', 's čokoladnimi kroglicami', 'mareličnega', 'zimskega', 'navadnega']
tastes_500 = ['borovničevega', 'vanilijevega', 'stracciatella', 'navadnega']  # New list for liquid yogurt
tastes_1000 = ['navadnega']  # New list for 1000g liquid yogurt

total_milk_180 = 0
total_milk_250 = 0
total_milk_500 = 0  # Added for liquid yogurt
total_milk_1000 = 0  # Added for 1000g liquid yogurt
total_milk_500_cheese = 0  # New total for 500g cottage cheese
total_milk = 0  # Added for total milk

for taste in tastes_180:
    total_milk_180 += ask_for_yogurt(taste, 180) * 180

for taste in tastes_250:
    total_milk_250 += ask_for_yogurt(taste, 250) * 250

for taste in tastes_500:  # Added for liquid yogurt
    total_milk_500 += ask_for_yogurt(taste, 500) * 500

for taste in tastes_1000:  # Added for 1000g liquid yogurt
    total_milk_1000 += ask_for_yogurt(taste, 1000) * 1000

total_milk_180_in_liters = total_milk_180 / 1000
total_milk_250_in_liters = total_milk_250 / 1000
total_milk_500_in_liters = total_milk_500 / 1000  # Added for liquid yogurt
total_milk_1000_in_liters = total_milk_1000 / 1000  # Added for 1000g liquid yogurt

# Ask if user will produce cottage cheese
print("Ali boš proizvajal skuto? (da/ne)")
produce_cottage_cheese = input()

total_milk_cottage_cheese = 0
if produce_cottage_cheese.lower() == 'da':
    # Ask how many liters of milk will be used for cottage cheese
    print("Koliko litrov mleka potrebuješ za skuto?")
    total_milk_cottage_cheese = float(input())

# Add the milk used for cottage cheese to the total milk
total_milk += total_milk_cottage_cheese * 1000  # convert liters to grams
total_milk_in_liters = total_milk / 1000

print(f"Potrebuješ {total_milk_180_in_liters}L mleka za vse 180g jogurte.")
print(f"Potrebuješ {total_milk_250_in_liters}L mleka za vse 250g jogurte.")
print(f"Potrebuješ {total_milk_500_in_liters}L mleka za vse 0,5L tekoči jogurt.")  # Added for liquid yogurt
print(f"Potrebuješ {total_milk_1000_in_liters}L mleka za vse 1L tekoči jogurt.")
print(f"Potrebuješ {total_milk_cottage_cheese}L litrov mleka za skuto.")

total_milk = total_milk_180 + total_milk_250 + total_milk_500 + total_milk_1000 + total_milk # Added total_milk_500
total_milk_in_liters = total_milk / 1000
print(f"Skupaj potrebuješ {total_milk_in_liters}L mleka za vse jogurte.")

# Ask for the production date
print("Vpiši datum proizvodnje (format: dd-mm-yyyy).")
production_date = datetime.datetime.strptime(input(), "%d-%m-%Y").date()

# Calculate the expiry date
expiry_date = production_date + datetime.timedelta(weeks=3, days=3)
print(f"Rok uporabe za jogurte proizvedene na {production_date} je {expiry_date}.")