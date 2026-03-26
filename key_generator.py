from coincurve import *

line = "#######################################################"

smile = """ 
//////////////////////////////////////         
//////////////////////////////////////         
//////////////////////////////////////         
//////////////////////////////////////         
///////        ///////        ////////            
//////////////////////////////////////         
//////////////////////////////////////         
//////////////////////////////////////         
////////   //////////////   //////////          
//////////               /////////////           
//////////////////////////////////////              
//////////////////////////////////////                 
//////////////////////////////////////                     
"""

class Colors:
    # Foreground colors
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    # Styles
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    # Reset color and style to default
    RESET = '\033[0m'

options = f"""\n\n\n\n\n\n\n
{Colors.BOLD}Please select an option below:{Colors.RESET}

{Colors.GREEN}1. Create Key Pair
{Colors.CYAN}2. Verify Signature
{Colors.BLUE}3. Sign Message
{Colors.MAGENTA}4. Display Keys\n
{Colors.RED}5. exit the program
{Colors.RESET}
\n\n\n\n\n\n
 """

def output(message) :
    
    #clear screen
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    
    print(message)
    
    #push text to the middle of screen
    print("\n\n\n\n\n\n")
    
    print(line)
    input(f"Please press {Colors.BOLD}{Colors.RED}enter button{Colors.RESET} to continue")

def create_key():
    private_key = PrivateKey()
    public_key = private_key.public_key
    return private_key, public_key

def sign_message(private_key, message):
    signature = private_key.sign(message.encode())
    return signature

def verify_signature(public_key, message, signature):
    return public_key.verify(signature, message.encode())

def start():
    if __name__ == "__main__":
        while True:

            print(options)
            choice = input("Enter number command: ")
            # Create Key Pair option 1
            if choice == "1":
                private_key, public_key = create_key()
                #print(Colors.YELLOW + "Key pair generated successfully." + Colors.RESET)
                output(Colors.YELLOW + "Key pair generated successfully." + Colors.RESET)                

            # Verify Message option 2
            elif choice == "2":
                Ms = input("Enter message: ")
                Sign_Ms = input("Enter signature(hex): ")
                PubK = input("Enter public key(hex): ")
                
                # convert hex to bytes
                try:
                    Sign_Ms = bytes.fromhex(Sign_Ms)
                    PubK = bytes.fromhex(PubK)    
                
                    verify_signature(PublicKey(PubK), Ms, Sign_Ms)
                    #print(Colors.GREEN + "Signature is valid." + Colors.RESET)
                    output(Colors.GREEN + "Signature is valid." + Colors.RESET)

                except:
                    #print(Colors.RED + "Signature is invalid." + Colors.RESET)
                    output(Colors.RED + "Signature is invalid." + Colors.RESET)

            # Sign Message option 3
            elif choice == "3":
                Ms = input("Enter message: ")
                signature = sign_message(private_key, Ms)
                #print(Colors.CYAN + "Signature:", signature.hex() + Colors.RESET)
                output(signature.hex())
            
            # Display Keys option 4
            elif choice == "4":
                if private_key:
                    pri = private_key.to_hex()
                    pub = public_key.format().hex()
                    output(f"{Colors.MAGENTA}Private:\n{pri}\n\n{Colors.CYAN}Public:\n{pub}{Colors.RESET}")
                else:
                    #print(Colors.RED + "No keys generated yet. Please create a key first." + Colors.RESET)
                    output(Colors.RED + "No keys generated yet. Please create a key first." + Colors.RESET)
            
            # Exit option 5
            elif choice == "5":
                print(Colors.GREEN + "Exiting the program. Goodbye!" + Colors.RESET)
                print(smile)
                break
            
            else:
                print(Colors.RED + "Invalid choice. Please try again." + Colors.RESET)

start()