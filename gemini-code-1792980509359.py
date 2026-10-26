import os
import glob
print(os.listdir("."))
print(glob.glob("*.jpg") + glob.glob("*.png"))