def check_premium(gender, year, smoker):
    if gender == 'male' and 1990 <= year <= 2000:
        premium_price = 35000
        if smoker == 'y':
            return f"Your annual premium is Rs {premium_price}"
        else:
            discounted_price = int((premium_price) - (premium_price * 0.1))
            return f"Your annual premium is Rs {discounted_price}"
        
    if gender == 'male' and 1970 <= year <= 1990:
        premium_price = 40000
        if smoker == 'y':
            return f"Your annual premium is Rs {premium_price}"
        else:
            discounted_price = int((premium_price) - (premium_price * 0.05))
            return f"Your annual premium is Rs {discounted_price}"
        
    if gender == 'female' and 1990 <= year <= 2000:
        premium_price = 30000
        if smoker == 'y':
            return f"Your annual premium is Rs {premium_price}"
        else:
            discounted_price = int((premium_price) - (premium_price * 0.1))
            return f"Your annual premium is Rs {discounted_price}"
        
    if gender == 'female' and 1970 <= year <= 1990:
        premium_price = 35000
        if smoker == 'y':
            return f"Your annual premium is Rs {premium_price}"
        else:
            discounted_price = int((premium_price) - (premium_price * 0.05))
            return f"Your annual premium is Rs {discounted_price}"
        
    return "Required information according to Year of birth not available..."


def main():
    while True:
        try:
            user_gender = input("Enter your gender (male or female): ")
            if user_gender.lower() == 'exit':
                break
            if user_gender.lower() != 'male' and user_gender.lower() != 'female':
                raise ValueError("Only 'male' or 'female' allowed...")
            
            user_dob = input("Enter your Year of birth (no date no month)\nExample: 20/05/1998 -> 1998: ")
            year = int(user_dob)
            if len(user_dob) < 4 or len(user_dob) > 4:
                raise ValueError("Enter correct year format")

            user_smoker = input("Press 'y' if you smoke, else 'n': ")
            if user_smoker.lower() != 'n' and user_smoker.lower() != 'y':
                raise ValueError("Only accepted 'y' or 'n'")
            
            result = check_premium(user_gender, year, user_smoker)

            print(result)
                
        except ValueError as e:
            print(e)



if __name__ == "__main__":
    main()
