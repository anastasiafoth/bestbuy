# Best Buy Store Application

A Python-based command-line application for managing an electronics store's inventory and processing customer orders.

## Features

- **Product Management**
  - Add products with name, price, and quantity
  - Track product inventory
  - Activate/deactivate products
  - Input validation for all fields
  - Stock level checks

- **Store Operations**
  - View all available products
  - Check total inventory quantity
  - Process customer orders
  - Handle stock management automatically

- **User Interface**
  - Interactive command-line interface
  - Clear menu system
  - Informative error messages

## Getting Started

### Prerequisites
- Python 3.7 or higher

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/anastasiafoth/bestbuy.git
   cd Best_buy

2. Run the application:
    ```bash
    python -m bestbuy.main
    
### How to Use
1. Main Menu
    ```bash
   1. List all products in store
   2. Show total amount in store
   3. Make an order
   4. Quit
2. Making an Order
   - Select products by number
   - Enter desired quantities
   - Complete the order to see the total price
   
### Project Structure
   ```
   Best_buy/
   ├── bestbuy/
   │   ├── __init__.py
   │   ├── main.py          # Main application and UI
   │   ├── products.py      # Product class and logic
   │   └── store.py         # Store and inventory management
   └── README.md
   ```

### Error Handling
The application includes comprehensive error handling for:

- Invalid menu choices
- Non-numeric input
- Negative values
- Insufficient stock
- Empty product names

### Example
```plaintext
   Store Menu
   ----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit

Please choose a number: 1

1. MacBook Air M2, Price: 1450, Quantity: 100
2. Bose QuietComfort Earbuds, Price: 250, Quantity: 500
3. Google Pixel 7, Price: 500, Quantity: 250
```
### Contributing
Contributions are welcome! Please feel free to submit a Pull Request.