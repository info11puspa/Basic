'''No third party library'''

'''Syntax:  
   if (any condition):
       command to do
   else:
       command to do'''

acceleration = 2.0 #m/s
mass = 20.0 #kg
Force_required = mass*acceleration
applied_force = 50.0 #Newton
#If condition begins here
if applied_force >= Force_required: #identation is required. I am leaving four spaces here
    print 'Yes, we can move the mass of 20 kg with some acceleration'
else:
    print 'Sorry, No motion'

#more nested version
print '---------------------------------------------------------------'
print 'more precisely ..'
print ''
if applied_force == Force_required:
   acceleration = 2.0
   print 'acceleration of the mass is ',acceleration
elif applied_force > Force_required:
   acceleration = applied_force/mass
   print 'acceleration of the mass is %.2f m/s'%acceleration
else:
   print 'Sorry, No motion'



