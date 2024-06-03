def main():
    n = 1260 
    count = 0 

    array = [500,100,50,10]

    for coin in array:
        count += n // coin # count = 2
        n %= coin # n = 260 
        
    return count 

if __name__ == "__main__":
    result = main()
    print(result)