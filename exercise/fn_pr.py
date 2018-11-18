############################
# Cameron Kimber
# 2018-09-19
# Class: 
# Assignment: 
############################
 

def maxer(a=1,b=2,c=3):
    if a > b and a > c:
        return a
    elif b>c:
        return b
    else:
        return c
    
def main(): 
    print(maxer(10,12,15))

if __name__ == "__main__":
	main()
