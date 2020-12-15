import time

def main():
    killer = GracefulKiller()
    while not killer.kill_now:
        
        print("Hello world!")
        time.sleep(1)

if __name__ == "__main__":
    main()