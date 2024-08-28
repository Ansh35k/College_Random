Mlamb_avg = 0
a=eval(input("Enter the number of readings u are taking"))
for i in range(a):
    Mstart_reading = float(input("Enter start reading: "))
    Mstop_reading = float(input("Enter stop reading: "))
    Mlamb = (Mstop_reading - Mstart_reading) * 2 / (11 - 1)
    Mlamb_avg += Mlamb
Mlamb_avg /= a
print(Mlamb_avg/2)
M1lamb_avg=0
for i in range(a):
    M1start_reading = float(input("Enter start reading: "))
    M1stop_reading = float(input("Enter stop reading: "))
    M1lamb = (M1stop_reading - M1start_reading) * 2 / (11 - 1)
    M1lamb_avg += M1lamb
M1lamb_avg /= a
print(M1lamb_avg/2)
Wavelenght=(Mlamb_avg/2)+(M1lamb_avg/2)
Velocity=2*Wavelenght*1000000
print(Velocity)
