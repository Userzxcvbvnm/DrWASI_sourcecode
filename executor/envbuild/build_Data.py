from UnitDir import UnitDir

if __name__ == "__main__":
    data = UnitDir("../staticinfo")
    data.gen_ran_unitdir()
    data2 = data.copy_unitdir("../staticinfo/copy")

    data.print_unitdir()
    data2.print_unitdir()
