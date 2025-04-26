import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Ellipse

def draw_entity(ax, x, y, name):
    rect = Rectangle((x-1.5, y-0.5), 3, 1, fill=False)
    ax.add_patch(rect)
    ax.text(x, y, name, ha='center', va='center', fontsize=12, weight='bold')

def draw_attribute(ax, x, y, name, key=False):
    ellipse = Ellipse((x, y), width=2.5, height=0.8, fill=False)
    ax.add_patch(ellipse)
    ax.text(x, y, name, ha='center', va='center', fontsize=10, weight='bold' if key else 'normal')

def draw_line(ax, x1, y1, x2, y2):
    ax.plot([x1, x2], [y1, y2], 'k-', linewidth=1)

# Create a figure with three subplots
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Common subplot setup
for ax in axes:
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

# Left: Customer & Payments
ax = axes[0]
draw_entity(ax, 5, 8, "Customer")
for x, y, n, k in [(3,9,"CustomerID",True),(5,9,"Name",False),(7,9,"ContactInfo",False)]:
    draw_attribute(ax, x, y, n, key=k)
    draw_line(ax, 5, 8, x, y)

draw_entity(ax, 5, 5, "CustomerAddress")
for x, y, n, k in [(3,6,"AddressID",True),(5,6,"CustomerID",False),(7,6,"Street",False),
                   (3,4,"City",False),(5,4,"State",False),(7,4,"ZipCode",False)]:
    draw_attribute(ax, x, y, n, key=k)
    draw_line(ax, 5, 5, x, y)
draw_line(ax, 5, 7.5, 5, 6.5)

draw_entity(ax, 2, 5, "PaymentMethod")
for x, y, n, k in [(0.5,6,"PaymentMethodID",True),(2,6,"CustomerID",False),
                   (3.5,6,"Type",False),(0.5,4,"Provider",False),
                   (2,4,"AccountMasked",False),(3.5,4,"ExpirationDate",False)]:
    draw_attribute(ax, x, y, n, key=k)
    draw_line(ax, 2, 5, x, y)
draw_line(ax, 5, 7.5, 2, 5.5)

ax.set_title("Customer / Payments", fontsize=14)

# Middle: Order & Fulfillment
ax = axes[1]
draw_entity(ax, 5, 8, "Order")
for x, y, n, k in [(3,9,"OrderID",True),(3,7,"CustomerID",False),(7,7,"RestaurantID",False),
                   (5,9,"OrderDate",False),(7,5,"EstimatedDeliveryTime",False),(5,5,"DeliveryFee",False),
                   (3,5,"TaxAmount",False),(5,3,"TotalAmount",False),(3,3,"PaymentStatus",False),
                   (7,3,"DeliveryStatus",False),(5,1,"DeliveryPersonID",False)]:
    draw_attribute(ax, x, y, n, key=k)
    draw_line(ax, 5, 8, x, y)

draw_entity(ax, 8, 4, "OrderItem")
for x, y, n, k in [(6,5,"OrderItemID",True),(6,3,"OrderID",False),(8,5,"MenuItemID",False),
                   (10,3,"Quantity",False),(8,1,"SpecialInstructions",False)]:
    draw_attribute(ax, x, y, n, key=k)
    draw_line(ax, 8, 4, x, y)
draw_line(ax, 5, 2, 6, 3)
draw_line(ax, 5, 2, 0, 3.5)

draw_entity(ax, 2, 4, "OrderTracking")
for x, y, n, k in [(0,5,"TrackingID",True),(0,3,"OrderID",False),
                   (2,5,"Timestamp",False),(4,4,"Latitude",False),(2,3,"Longitude",False)]:
    draw_attribute(ax, x, y, n, key=k)
    draw_line(ax, 2, 4, x, y)

draw_entity(ax, 5, 1, "DeliveryPerson")
for x, y, n, k in [(3,2,"DeliveryPersonID",True),(5,3,"Name",False),
                   (7,2,"ContactInfo",False),(5,0,"AvailabilityStatus",False)]:
    draw_attribute(ax, x, y, n, key=k)
    draw_line(ax, 5, 1, x, y)
draw_line(ax, 5, 2, 5, 8)

ax.set_title("Order / Fulfillment", fontsize=14)

# Right: Restaurant & Menu
ax = axes[2]
draw_entity(ax, 5, 8, "Restaurant")
for x, y, n, k in [(3,9,"RestaurantID",True),(5,9,"Name",False),(7,9,"Street",False),
                   (7,8,"City",False),(5,7,"State",False),(7,7,"ZipCode",False),(3,7,"ContactInfo",False)]:
    draw_attribute(ax, x, y, n, key=k)
    draw_line(ax, 5, 8, x, y)

draw_entity(ax, 8, 10, "CuisineCategory")
for x, y, n, k in [(6,11,"CategoryID",True),(10,11,"Name",False)]:
    draw_attribute(ax, x, y, n, key=k)
    draw_line(ax, 8, 10, x, y)

draw_entity(ax, 8, 6, "RestaurantCuisine")
for x, y, n, k in [(6,7,"RestaurantID",False),(10,7,"CategoryID",False)]:
    draw_attribute(ax, x, y, n, key=k)
    draw_line(ax, 8, 6, x, y)
draw_line(ax, 5, 7.5, 6.5, 7)

draw_entity(ax, 5, 4, "MenuItem")
for x, y, n, k in [(3,5,"MenuItemID",True),(5,5,"RestaurantID",False),
                   (7,5,"Name",False),(7,4,"Description",False),(3,3,"Price",False),
                   (5,3,"IsAvailable",False)]:
    draw_attribute(ax, x, y, n, key=k)
    draw_line(ax, 5, 4, x, y)
draw_line(ax, 5, 7.5, 5, 5)

ax.set_title("Restaurant / Menu", fontsize=14)

plt.tight_layout()
plt.show()
