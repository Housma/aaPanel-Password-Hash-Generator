import hashlib
import argparse

def aapanel_hash(password, salt):
    """Calculate aaPanel's 3-step MD5 hash"""
    # Step 1: MD5 of raw password
    step1 = hashlib.md5(password.encode()).hexdigest()
    
    # Step 2: MD5(step1 + "_bt.cn")
    step2 = hashlib.md5(f"{step1}_bt.cn".encode()).hexdigest()
    
    # Step 3: MD5(step2 + salt)
    final_hash = hashlib.md5(f"{step2}{salt}".encode()).hexdigest()
    
    return final_hash

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="aaPanel Password Hash Generator")
    parser.add_argument("-p", "--password", required=True, help="Plain password")
    parser.add_argument("-s", "--salt", required=True, help="Salt to use")

    args = parser.parse_args()

    hashed = aapanel_hash(args.password, args.salt)
    
    print(f"""
    aaPanel Password Hash Generator
    -------------------------------
    Plain Password : {args.password}
    Salt           : {args.salt}
    Generated Hash : {hashed}
    """)
