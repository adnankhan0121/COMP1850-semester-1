# Week 1.2, Session 2: Task 6
temperature = int(input("Enter the machine's temperature in Celsius "))
pressure = int(input("Enter the machine's pressure in PSI "))
status = int(input("The machine's operational status (1. for operating, 2. 0 for stopped): "))


if temperature > 80 :
    print(f"Temperature too high; recommend shutting down")
elif 50 <= temperature <=80 :
    print(f"Temperature within safe limits") 
else:
    print(f"temperature is low; no action needed")


if pressure > 100 :
    print("High pressure detected; recommend maintenance")
elif 70 <= pressure <= 100 :
    print("Pressure is stable")
else: 
    print("pressure is low; system operating normally")


if status == 1:
    if temperature > 80 or pressure > 100 :
        print("the machine is running in unsafe conditions and recommending that it be shut down.")
    else: 
        print("The machine is running normally")
else: 
    print("the machine is stopped;" \
    " no immediate action is needed,")    
  