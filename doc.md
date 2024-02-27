# Customers
* First name
* Last name
* Email
* Phone
* Address
* Id
* Status (active, inactive)

## What can customer do?
* Make reservation
* Cancel reservation
* Make payment for reservation and other services
* Make reports

# Rooms
* Room number
* Room type
* Room price per night
* Room status / availability
* Amenities

### Navigation of room
* Can have many reservations

# Reservations / Booking
* Id
* Room number
* Customer id
* Check-in date
* Check-out date
* Total amount
* Status (pending, confirmed, cancelled)
* Payment status (pending, paid, refunded)
* Date issued
* Staff id


# Employee
* Name
* Id
* Email
* Position
* Date of employment
* Salary
* Address
* Phone
* Role (admin, receptionist, cleaner, manager)


# Payment
* Id
* Guest id
* Service id
* Amount
* Date

# Products and Services
* Id
* Name
* Price per unit
* Quantity

# Reviews
* Id
* Customer id
* Room id
* Rating
* Comment
* Date


A hotel management system can have a wide range of functionalities. Here are some common ones:

1. **Room Management**: This includes functionalities like adding new rooms, updating room details, checking room availability, and managing room reservations.

2. **Reservation Management**: This includes functionalities like creating new reservations, updating reservation details, cancelling reservations, and viewing reservation history.

3. **Customer Management**: This includes functionalities like adding new customers, updating customer details, managing customer reservations, and viewing customer history.

4. **Employee Management**: This includes functionalities like adding new employees, updating employee details, assigning roles to employees, and managing employee schedules.

5. **Billing and Payment Management**: This includes functionalities like creating new bills, updating bill details, processing payments, and viewing payment history.

6. **Product and Service Management**: This includes functionalities like adding new products or services, updating product or service details, managing product or service inventory, and viewing product or service history.

7. **Reporting**: This includes functionalities like generating reports on room occupancy, revenue, customer demographics, employee performance, and product or service sales.

8. **Inventory Management**: This includes functionalities like tracking the inventory of items in the hotel such as toiletries, towels, food items, etc.

9. **Maintenance Management**: This includes functionalities like scheduling routine maintenance, tracking repair requests, and managing maintenance staff.

10. **Communication**: This includes functionalities like sending emails or SMS notifications to customers about their reservations, payments, and other important information.

These functionalities can be implemented as methods within the respective classes in your hotel management system. For example, the `Room` class can have methods like `add_room()`, `update_room()`, `check_availability()`, and `manage_reservations()`. Similarly, the `Customer` class can have methods like `add_customer()`, `update_customer()`, `manage_reservations()`, and `view_history()`, and so on.
