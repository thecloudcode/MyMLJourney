import matplotlib.pyplot as plt
exp_vals = [1400,600,300,410,250]
exp_labels = ["Home Rent","Food","Phone/Internet Bill","Car","Other Utilities"]
plt.pie(exp_vals,labels=exp_labels, radius=1.5, autopct='%0.0f%%', shadow=True, explode=[0,0.2,0,0,0])
plt.axis("equal")

plt.savefig("piechart4.png",bbox_inches="tight", pad_inches=2, transparent=True)
plt.show()
