# Multiple inheritance
# this isn’t supported in TS, you can only extend one class


class Computer:
    def __init__(self, brand):
        self.brand = brand

    def browse_internet(self):
        print(f"Using {self.brand}'s default internet browser.")


class Telephone:
    def __init__(self, phone_number):
        self.phone_number = phone_number

    def make_call(self, recipient):
        print(f"Calling {recipient} from {self.phone_number}")


# Smartphone class that inherits from Computer and Telephone classes
class Smartphone(Computer, Telephone):
    def __init__(self, brand, phone_number, music_app):
        # Call the constructor for the Computer and Telephone
        # class, define the music_app instance-level attribute
        Computer.__init__(self, brand)
        Telephone.__init__(self, phone_number)
        self.music_app = music_app

    def play_music(self, song):
        print(f"Playing {song} using {self.music_app}")


personal_phone = Smartphone("Macrosung", "801-932-7629", "Dotify")

personal_phone.browse_internet()
personal_phone.make_call("Alex")
personal_phone.play_music("Creeks and Highways")

# Multi level inheritance


class Tablet(Computer):
    def __init__(self, brand, apps):
        Computer.__init__(self, brand)
        self.apps = apps

    def uninstall_app(self, app):
        if app in self.apps:
            self.apps.remove(app)


# Smartphone2 class that inherits from Tablet, which inherits from computer
class Smartphone2(Tablet):
    def __init__(self, brand, apps, phone_number):
        Tablet.__init__(self, brand, apps)
        self.phone_number = phone_number

    # Create send_text to send a message to a recipient
    def send_text(self, message, recipient):
        print(f"Sending {message} to {recipient} from {self.phone_number}")


personal_phone = Smartphone2("Macrosung", ["Weather", "Camera"], "801-932-7629")
personal_phone.browse_internet()
personal_phone.uninstall_app("Weather")
personal_phone.send_text("Time for a new mission!", "Chuck")
