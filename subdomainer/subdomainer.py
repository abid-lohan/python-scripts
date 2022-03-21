import dns.resolver, sys

def bruteforce_subdomains():
    '''Tries to discover subdomains from a DNS using a wordlist'''

    target = sys.argv[1]
    wordlist = open(sys.argv[2], "r")

    lista = wordlist.read().splitlines()

    response = dns.resolver.Resolver()
    results = response.resolve(target, "A")

    print("---------------------------")

    print("Target IPs:\n")
    for ip in results:
        print(target, "->", ip)

    print("---------------------------")
    print("Discovering subdomains of", target, "...")

    for sub in lista:
        subdomain = sub+"."+target
        try:
            results = response.resolve(subdomain, "A")
            print("\n"+subdomain, "found!")
            for ip in results:
                print(subdomain, "->", ip)
        except:
            pass

    print("---------------------------")
    print("Finished!")

def welcome():
    '''Prints a welcome message'''

    print("---------------------------")
    print("This is a simple subdomain discover made by Abid Lohan.")
    print("It bruteforces from a wordlist.")

def help():
    '''Returns a help with an example of how to use the script'''

    return '''---------------------------
You can use the script passing a domain and a wordlist as parameters:
python3 subdomainer.py domain.com wordlist.txt'''


welcome()
help_called = False

if len(sys.argv) == 1:
    print(help())
    help_called = True

for arg in sys.argv:
    if arg == "-h" or arg == "--help":
        print(help())
        help_called = True

if help_called == False:
    try:
        bruteforce_subdomains()
    except:
        print(help())
        help_called = True