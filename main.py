import sys

def calculate_chargeable_weight(length, width, height, dimensional_factor):
    return (length * width * height) / dimensional_factor

def main(transport_method, num_boxes, length, width, height, original_weight, dimensional_factor):
    num_boxes = int(num_boxes)

    # Dimensional factors
    truck_factor = 3000
    air_factor = 6000
    sea_factor = 1000
    express_courier_factor = 5000

    # Validate transport method
    if transport_method not in ["TRUCK", "AIR", "SEA", "EXPRESS_COURIER"]:
        print("Invalid transport method. Please choose from TRUCK, AIR, SEA, or EXPRESS_COURIER.")
        return

    chargeable_weights = []
    original_weights = []

    for box_number in range(1, num_boxes + 1):
        print(f"\nBox {box_number}:")

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
        chargeable_weight = calculate_chargeable_weight(length, width, height, dimensional_factor)

        # Store chargeable weight and original weight for each box
        chargeable_weights.append(chargeable_weight)
        original_weights.append(original_weight)

    # Calculate total chargeable weight for all boxes
    total_chargeable_weight = sum(chargeable_weights)
    total_original_weight = sum(original_weights)

    # Display total results and comparison messages
    for i in range(num_boxes):
        print(f"\nBox {i + 1}:")
        print(f"Chargeable Weight: {chargeable_weights[i]}")
        print(f"Original Weight: {original_weights[i]}")

    print(f"\nTotal Chargeable Weight for all boxes: {total_chargeable_weight}")

    # Compare total chargeable weight with total original weight
    if total_chargeable_weight > total_original_weight:
        print("Total chargeable weight is higher than total real weight. Use", total_chargeable_weight, "for cost calculation.")
    elif total_chargeable_weight < total_original_weight:
        print("Total chargeable weight is lower than total real weight. Use", total_original_weight, "for cost calculation.")
    else:
        print("Total chargeable weight is equal to total real weight.")

if __name__ == "__main__":
    if len(sys.argv) != 8:
        print("Usage: python main.py transport_method num_boxes length width height original_weight dimensional_factor")
        sys.exit(1)
    
    transport_method = str(sys.argv[1])
    num_boxes = int(sys.argv[2])
    length = float(sys.argv[3])
    width = float(sys.argv[4])
    height = float(sys.argv[5])
    original_weight = float(sys.argv[6])
    dimensional_factor = float(sys.argv[7])
    main(transport_method, num_boxes, length, width, height, original_weight, dimensional_factor)
