
class Login(object):
    
    banner = "//h2[contains(text(),'Please Login')]"
    user = "//input[@id='username']"
    password = "//input[@id='password']"
    login_button = "//span[contains(text(),'Log In')]"
    register_button = "//span[contains(text(),'Register')]"
    user_register = "//input[@id='register-username']"
    password_register = "//input[@id='register-password']"
    button_register = "/html/body/div[2]/div[3]/div/div[3]/button/span[1]"
    banner_register = "//h2[contains(text(),'Thank you!')]"
    message_register = "//p[contains(text(),'Please insert Username and Password')]"