import getpass

password = input('What is your Password ::')
#by using the above, the password is visible while entering. 
#better way to handle this is to use getpass liberary.

password = getpass.getpass('What is your Password ::')
#by using the above, the password is invisible while entering - a secured way to send the information.