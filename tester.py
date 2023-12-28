from datetime import datetime

def get_user_birthdate():
    birthdate_str =  input("Enter your date of birth in the form YYYY-MM-DD \n")
    return datetime.strptime(birthdate_str, '%Y-%m-%d')

def get_age_in_days(birthdate):
     current_date = datetime.now()
     age_in_days = (current_date - birthdate).days
     return age_in_days

def main():
    user_birth_date = get_user_birthdate()
    age_in_days = get_age_in_days(user_birth_date)
    print(age_in_days)
    
 
if __name__ == "__main__":
    main()