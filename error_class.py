"""
a = "the sky is blue"
print(a)

for letter in a:
    print(letter)
"""
def error_try():
    try:
        r = "hello"
        type(r)
        rnew = int(r)
    except ValueError:
        rnew = "a string"
        print(rnew)
        

def main():
    error_try()
    

if __name__ == "__main__":
    main()