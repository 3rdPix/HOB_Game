from app import Game
import sys

if __name__ == '__main__':
    
    # Delete when finished, exception tracker
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook
    
    # Create instance of app
    app = Game(sys.argv)
    sys.exit(app.exec())