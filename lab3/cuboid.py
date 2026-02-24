import threedfigures as tf

l = float(input("Enter length: "))
b = float(input("Enter breadth: "))
h = float(input("Enter height: "))

print("Curved Surface Area =", tf.cuboid_curved_surface_area(l, b, h))
print("Total Surface Area =", tf.cuboid_total_surface_area(l, b, h))
print("Volume =", tf.cuboid_volume(l, b, h))
