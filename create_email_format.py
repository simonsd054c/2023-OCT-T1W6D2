# Create an email using full name and company name using string methods

full_name = input("Enter your full name: ")
# Simon Dahal

company_name = input("Enter your company name: ")
# Dairy Farm

# result = simon.dahal@dairyfarm.com.au

splitted_full_name = full_name.split() # ['Simon', 'Dahal']
joined_full_name_with_dot = ".".join(splitted_full_name) # Simon.Dahal

print(splitted_full_name)
print(joined_full_name_with_dot)

splitted_company_name = company_name.split() # ['Dairy', 'Farm']
joined_company_name = "".join(splitted_company_name) # DairyFarm

print(splitted_company_name)
print(joined_company_name)

predicted_email = f"{joined_full_name_with_dot}@{joined_company_name}.com.au".lower()

print(predicted_email)