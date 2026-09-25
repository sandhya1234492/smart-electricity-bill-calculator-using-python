"""Beginner-friendly electricity bill calculator."""


def get_customer_details():
    """Read and return customer information from the user."""
    customer_name = input("Enter customer name: ")
    customer_id = input("Enter customer ID: ")

    while True:
        try:
            units_consumed = int(input("Enter electricity units consumed: "))
            if units_consumed < 0:
                print("Units cannot be negative. Please try again.")
            else:
                return customer_name, customer_id, units_consumed
        except ValueError:
            print("Please enter a whole number for units.")


def calculate_bill(units_consumed):
    """Calculate the energy charge, service charge, and final amount."""
    if units_consumed <= 100:
        energy_charge = units_consumed * 2
    elif units_consumed <= 200:
        energy_charge = (100 * 2) + ((units_consumed - 100) * 4)
    elif units_consumed <= 500:
        energy_charge = (100 * 2) + (100 * 4) + ((units_consumed - 200) * 6)
    else:
        energy_charge = (100 * 2) + (100 * 4) + (300 * 6) + ((units_consumed - 500) * 8)

    service_charge = 100.0
    final_amount = energy_charge + service_charge
    return float(energy_charge), service_charge, final_amount


def display_bill(customer_name, customer_id, units_consumed, energy_charge, service_charge, final_amount):
    """Display the customer's electricity bill."""
    print("\n" + "=" * 42)
    print("          SMART ELECTRICITY BILL")
    print("=" * 42)
    print(f"Customer name : {customer_name}")
    print(f"Customer ID   : {customer_id}")
    print(f"Units used    : {units_consumed}")
    print("-" * 42)
    print(f"Energy charge : ₹{energy_charge:.2f}")
    print(f"Service charge: ${service_charge:.2f}")
    print(f"Final amount  : ₹{final_amount:.2f}")
    print("=" * 42)


def main():
    """Run the electricity bill calculator."""
    customer_name, customer_id, units_consumed = get_customer_details()
    energy_charge, service_charge, final_amount = calculate_bill(units_consumed)
    display_bill(
        customer_name,
        customer_id,
        units_consumed,
        energy_charge,
        service_charge,
        final_amount,
    )


if __name__ == "__main__":
    main()