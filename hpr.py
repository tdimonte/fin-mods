#Holding period return is the total return received from holding an asset or portfolio of assets over a period of time, known as the holding period, generally expressed as a percentage (Investopedia).

init_val = float(input("Enter Initial Value: "))
end_val = float(input("Enter Ending Value: "))
div_y1 = float(input("Enter Divident in Year 1: "))
div_y2 = float(input("Enter Divident in Year 2: "))
div_y3 = float(input("Enter Divident in Year 3: "))

#Calculate income generated
div_yeild = div_y1 + div_y2 + div_y3

#Calculate HPR
def calc_hpr(div_yeild, init_val, end_val):
    hpr = (div_yeild + (end_val - init_val)) / init_val
    hpr = str((hpr*100)) + '%'
    return(hpr)

print(calc_hpr(div_yeild, init_val, end_val))

