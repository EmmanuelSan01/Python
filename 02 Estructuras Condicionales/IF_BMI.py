lb=float(input("Enter weight in pounds\n"))
inch=float(input("\nEnter height in inches \n"))

if lb>0 and inch>0:
    kl=lb*0.45359237
    mt=inch*0.0254

    bmi=kl/mt**2

    print(f"\nBMI is {bmi:.2f}")
    if bmi>=30:
        print("Obese")
    elif bmi>=25:
        print("Overweight")
    elif bmi>=18.5:
        print("Normal")
    else:
        print("Underweight")
else:
    print("\n>>ERROR. Wrong Input")