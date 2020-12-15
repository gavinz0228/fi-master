def calculate_savings(start_amount, monthly_contrib, yld, start_year, num_years):
    years = [start_year]
    compoundedSavings = [start_amount]
    flatSavings =[start_amount]
    last_amount = start_amount
    for i in range(1, num_years):
        years.append(start_year + i)
        compoundedSavings.append(compoundedSavings[-1] * (1+ yld) + monthly_contrib * 12)
        flatSavings.append(flatSavings[-1] + monthly_contrib * 12)
    return {"years": years ,"compoundedSavings": compoundedSavings, "flatSavings": flatSavings}