in_arr = input()

print(len(in_arr) - (
        in_arr.count("c=")
      + in_arr.count("c-")
      + in_arr.count("dz=")
      + in_arr.count("d-")
      + in_arr.count("lj")
      + in_arr.count("nj")
      + in_arr.count("s=")
      + in_arr.count("z="))
)
