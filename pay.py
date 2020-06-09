print ('PAYMENT COMPUTATION FOR EMPLOYEES')
print ('---------------------------------')

def payment(hours, rate):
    if hours > 10:
        return str((hours*rate)+200)
    else:
        return str(hours*rate)

hoursinp = int(input ('Enter hours: '))
rateinp = int(input ('Enter rate: '))
results = payment(hoursinp,rateinp)
print ('Pay: ' + results)