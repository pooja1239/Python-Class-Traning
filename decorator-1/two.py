def login_req(func):
    def inner(name, login_status):
        if login_status == False:
            return "Login is required"
        else:
            return func(name, login_status)
    return inner


@login_req
def homepage(name, login_status):
    return "homepage"

@login_req
def productpage(name, login_status):
    return "productpage"

@login_req
def orders(name, login_status):
    return "orders"

@login_req
def profile(name, login_status):
    return "profile"
