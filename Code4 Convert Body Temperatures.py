#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Celcius to Fahrenheit
def celcius_to_fahrenheit(celcius):
    return(celcius * 9/5) + 32


# In[2]:


# Fahrenheit to Celcius
def fahrenheit_to_celcius(fahrenheit):
    return(fahrenheit - 32) * 5/9


# In[ ]:


# setting dictionary to mapping the user input to the function
conversion_features ={
    'c': celcius_to_fahrenheit,
    'f': fahrenheit_to_celcius
}

print("choose the conversion direction.")
print("put C for celcius to fahrenheit or F for fahrenheit to celcius")

choice = input("enter your choice:").strip().lower()

if choice in conversion_features:
    temperature = float(input("Enter the temperature:"))


# In[ ]:


# Conversion
converted_temperature = conversion_features[choice](temperature)

print(f"{temperature}degrees{'celcius'if choice == 'c'else 'fahrenheit'}is{converted_temperature}degrees{'Fahrenheit'if choice == 'c'else 'celcius'}")
      
else:
    print("This is not a valid input. Please enter a C or an F")
      


# In[ ]:




