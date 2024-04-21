# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass

# Them so 1,2 vao duoi c,l
def add_1_2_in_pi_l_section(name):
    print(name)
    if name[0] == name[1]:
        return [name[0]+"1",name[1]+"2",name[2]]
    elif name[0] == name[2]:
        return [name[0]+"1",name[1],name[2]+"2"]
    else:
        return [name[0],name[1]+"1",name[2]+"2"]

# Chuyen GHz, MHz, Khz -> Hz
def convert_f_unit(f, unit):
    match unit:
        case "Hz":
            return f
        case "KHz":
            return f * 1e3
        case "MHz":
            return f * 1e6
        case "GHz":
            return f * 1e9

# Chuyen du lieu sang dang hien thi (mach l)
def l_section_convert_to_ui(data):
    if not data:
        return []
    else:
        for i in range(len(data)):
            data[i][0] = "🔹 Q Value: " + str(round(data[i][0],4))
            data[i][1] = "🔹 L Value: " + str(round(data[i][1],4)) + " nH"
            data[i][2] = "🔹 C Value: " + str(round(data[i][2],4)) + " pF"
        return data

# Chuyen du lieu sang dang hien thi (mach t, pi)
def pi_l_section_convert_to_ui(data):
    if not data:
        return []
    else:
        for i in range(len(data)):
            print(data)
            name_of_value = add_1_2_in_pi_l_section(data[i][3])
            data[i][0] = f"🔹 {name_of_value[0]} Value: " + str(round(data[i][0],4)) + (" nH" if name_of_value[0][0] == "L" else " pF")
            data[i][1] = f"🔹 {name_of_value[1]} Value: " + str(round(data[i][1],4)) + (" nH" if name_of_value[1][0] == "L" else " pF")
            data[i][2] = f"🔹 {name_of_value[2]} Value: " + str(round(data[i][2],4)) + (" nH" if name_of_value[2][0] == "L" else " pF")
        return data
