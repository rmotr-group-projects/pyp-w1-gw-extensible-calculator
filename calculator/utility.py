from datetime import datetime

def get_current_time_str():
   now = datetime.utcnow()
   string_rep = get_date_str(now) + " " + get_time_str(now)
   print("#",string_rep)
   return string_rep

def get_date_str(date_time):
    return date_time.date().__str__()

def get_time_str(d):
    string = d.time().__str__()
    print("S: " , string)
    millisecond_index = string.find(".")
    if "." in string:
        millisecond_index = string.find(".")
    else:
        millisecond_index = len (string)
    print("x: ", millisecond_index)
    return string[:millisecond_index].__str__();

def validate(instance, type_, ex, message):
    if type(instance) is not type_:
        raise ex(message)

def validate_params(params, type_, exception, message):
    validate(params, type_, exception, message)
    for item in params:
        try:
            float(item)
        except ValueError:
            raise exception(message)