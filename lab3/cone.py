import threedfigures as tf

r = float(input("Enter radius: "))
h = float(input("Enter height: "))

print("Curved Surface Area =", tf.cone_curved_surface_area(r, h))
print("Total Surface Area =", tf.cone_total_surface_area(r, h))
print("Volume =", tf.cone_volume(r, h))