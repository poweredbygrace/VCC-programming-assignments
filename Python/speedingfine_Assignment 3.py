
def calculate_fine():
    speed_limit = int(input("Enter the speed limit: "))
    clocked_speed = int(input("Enter the clocked speed: "))
    if clocked_speed <= speed_limit:
        print("The speed was legal.")
    else:
        fine = 50 + (clocked_speed - speed_limit) * 5
        if clocked_speed > 90:
            fine += 200
        print(f"The speed was illegal. The speeding fine is ${fine}.")



calculate_fine()
