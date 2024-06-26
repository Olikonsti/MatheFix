import os

for file in os.listdir("in"):
    f_ = file.split("_")
    f_[3] = f_[3].split(".")[0]
    new_filename = f_[3] + "_" + f_[2] + "_" + f_[1] + "_" + f_[0] + ".pdf"
    os.rename(f"in/{file}", f"in/{new_filename}")
