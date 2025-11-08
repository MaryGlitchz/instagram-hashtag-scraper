thondef clean_data(data):
"""
Helper function to clean and validate extracted data
"""
cleaned_data = [item.strip() for item in data if item.strip()]
return cleaned_data