import sys
from bot.core import EVEBot

def main():
    try:
        bot = EVEBot()
        
        if '--calibrate' in sys.argv:
            bot.calibrate()
        else:
            bot.start()
            
    except Exception as e:
        print(f"Fatal error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()