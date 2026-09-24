def add_setting(dict_setting,key_val_tuple):
    key,value = key_val_tuple
    key = key.lower()
    value = value.lower()
    if key in dict_setting:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else: 
        dict_setting[key]=value
        return f"Setting '{key}' added with value '{value}' successfully!"
def update_setting(dict_setting,key_val_tuple):
    key,value = key_val_tuple
    key = key.lower()
    value = value.lower()
    if key in dict_setting:
        dict_setting[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
def delete_setting(dict_setting,key_val_tuple):
    key = key_val_tuple[0] if isinstance(key_val_tuple, tuple) else key_val_tuple
    key = key.lower()
    if key in dict_setting:
        del dict_setting[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"
def view_settings(dict_setting):
    if dict_setting == {}:
        return "No settings available."
    result = ["Current User Settings:"]
    for key, value in dict_setting.items():
        result.append(f"{key.capitalize()}: {value}")
    return "\n".join(result) +"\n" 
test_settings ={'theme':'light', 
                 'volume':'high'}
