# Create an email using full name and company name using string methods

full_name = input("Enter your full name: ")
# Simon Dahal

company_name = input("Enter your company name: ")
# Dairy Farm

# result = simon.dahal@dairyfarm.com.au

required_full_name_format = full_name.replace(" ", ".") # Simon.Dahal
required_company_name_format = company_name.replace(" ", "") # DairyFarm

print(required_full_name_format)
print(required_company_name_format)

predicted_email = f"{required_full_name_format}@{required_company_name_format}.com.au".lower()

print(predicted_email)