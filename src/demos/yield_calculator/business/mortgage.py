def calculate_monthly_mortgage(principal, rate, num_years):
    rate = rate / 12
    num_payments = num_years * 12
    return -1 * principal * (rate * ((1+rate)**num_payments))  / (((1+rate)**num_payments)-1)

if __name__ == "__main__":
    print(calculate_monthly_mortgage(800000, 0.03 / 12, 360))