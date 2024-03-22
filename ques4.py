import pandas as pd

# Open the existing Excel file
with pd.ExcelWriter("User credentials.xlsx", mode="a", engine="openpyxl") as writer:
    # Create a new sheet named "Order Details"
    df_order_details = pd.DataFrame(columns=["User", "Product", "Quantity", "Total Price"])
    df_order_details.to_excel(writer, sheet_name="Order Details", index=False)

    # Add orders for the "standard_user"
    standard_user_orders = [
        {"User": "standard_user", "Product": "Sauce Labs Backpack", "Quantity": 2, "Total Price": 39.98},
        {"User": "standard_user", "Product": "Sauce Labs Bike Light", "Quantity": 1, "Total Price": 9.99},
        # Add more orders for the "standard_user" if needed
    ]
    df_standard_user_orders = pd.DataFrame(standard_user_orders)
    df_standard_user_orders.to_excel(writer, sheet_name="Order Details", startrow=1, index=False, header=False)

    # Add orders for the "problem_user"
    problem_user_orders = [
        {"User": "problem_user", "Product": "Sauce Labs Bolt T-Shirt", "Quantity": 3, "Total Price": 44.97},
        {"User": "problem_user", "Product": "Sauce Labs Fleece Jacket", "Quantity": 1, "Total Price": 49.99},
        # Add more orders for the "problem_user" if needed
    ]
    df_problem_user_orders = pd.DataFrame(problem_user_orders)
    df_problem_user_orders.to_excel(writer, sheet_name="Order Details", startrow=len(standard_user_orders) + 2, index=False, header=False)