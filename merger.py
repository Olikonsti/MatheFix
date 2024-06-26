import os
from pypdf import PdfWriter

"""
renames the files the correct way and puts them in a single file
"""

for file in os.listdir("in"):
    f_ = file.split("_")
    f_[3] = f_[3].split(".")[0]
    new_filename = f_[3] + "_" + f_[2] + "_" + f_[1] + "_" + f_[0] + ".pdf"
    print(new_filename)
    os.rename(f"in/{file}", f"in/{new_filename}")


merger = PdfWriter()

for file in os.listdir("in"):
    merger.append("in/" + file)
merger.write("out/Mathe_Skript_komplett.pdf")
merger.close()