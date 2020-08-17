import moon_wt_helper as m
# num1 = int(input('Enter a number:'))
# num2 = int(input('Enter a number:'))
earth_wt = eval(input('What is your weight on Earth?'))
years = eval(input('How much years so you wish to stay on the moon?'))
annual_wt_gain = eval(input('How much weight do you gain per year?'))
def calculate_moon_weight(earth_wt,years,annual_wt_gain):
    count = 0
    while count != years:
        earth_wt = m.add(earth_wt,annual_wt_gain)
        moon_weight = m.multiply(earth_wt,0.165)
        m.print_message(count,moon_weight)
        count = count+1
calculate_moon_weight(earth_wt,years,annual_wt_gain)









