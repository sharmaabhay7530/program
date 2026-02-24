import threedfigures as tf

r = float(input("Enter radius: "))
h = float(input("Enter height: "))

print("Curved Surface Area =", tf.cylinder_curved_surface_area(r, h))
print("Total Surface Area =", tf.cylinder_total_surface_area(r, h))
print("Volume =", tf.cylinder_volume(r, h))