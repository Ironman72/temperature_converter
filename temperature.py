# program to convert temperature 
# celcius formula = (celcius * 1.8) + 32
# farhrenheit formula = ((50°F - 32) x .5556

# user_input = float(input('Enter temperature: '))
# c_f_converter = (user_input * 1.8) + 32
# print('The Converted Temperature from Celcius to Farhenheit is: ',c_f_converter,'F')

user_input = float(input('Please Enter Farhenheit: '))
f_c_converter = ((user_input - 32)) * 0.5556
print('The converted Temperature from Farhenheit to Celcius is: ',f_c_converter,'C')