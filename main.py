def calculate_chargeable_weight(length, width, height, dimensional_factor):
    return (length * width * height) / dimensional_factor

def main():
    num_boxes = int(input("Enter the number of boxes: "))

    # Dimensional factors
    truck_factor = 3000
    air_factor = 6000
    sea_factor = 1000
    express_courier_factor = 5000

    # Choose transport method for the entire shipment
    transport_method = input("Choose transport method (TRUCK/AIR/SEA/EXPRESS_COURIER): ").upper()

    # Validate transport method
    if transport_method not in ["TRUCK", "AIR", "SEA", "EXPRESS_COURIER"]:
        print("Invalid transport method. Please choose from TRUCK, AIR, SEA, or EXPRESS_COURIER.")
        return

    chargeable_weights = []
    original_weights = []

    for box_number in range(1, num_boxes + 1):
        print(f"\nBox {box_number}:")

        b_length = float(input("Length(cm): "))
        b_width = float(input("Width(cm): "))
        b_height = float(input("Height(cm): "))
        original_weight = float(input("Weight(kg): "))

        # Determine the appropriate dimensional factor based on the chosen transport method
        if transport_method == "TRUCK":
            dimensional_factor = truck_factor
        elif transport_method == "AIR":
            dimensional_factor = air_factor
        elif transport_method == "SEA":
            dimensional_factor = sea_factor
        else:
            dimensional_factor = express_courier_factor

        # Calculate chargeable weight for each box
        chargeable_weight = calculate_chargeable_weight(b_length, b_width, b_height, dimensional_factor)

        # Store chargeable weight and original weight for each box
        chargeable_weights.append(chargeable_weight)
        original_weights.append(original_weight)

    # Calculate total chargeable weight for all boxes
    total_chargeable_weight = sum(chargeable_weights)
    total_orginal_weight = sum(original_weights)
    # Display total results and comparison messages
    
    for i in range(num_boxes):
        print(f"\nBox {i + 1}:")
        print(f"Chargeable Weight: {chargeable_weights[i]}")
        print(f"Original Weight: {original_weights[i]}")

        

    print(f"\nTotal Chargeable Weight for all boxes: {total_chargeable_weight}")
    # Compare chargeable weight with original weight
    if chargeable_weights[i] > original_weights[i]:
        print("Chargeable weight is higher than real weight. Use", total_chargeable_weight, "for cost calculation.")
    elif chargeable_weights[i] < original_weights[i]:
        print("Chargeable weight is lower than real weight. Use", total_orginal_weight, "for cost calculation.")
    else:
        print("Chargeable weight is equal to real weight.")
if __name__ == "__main__":
    main()
