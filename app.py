# Subsystem components
class DVDPlayer:
    def on(self):
        print("DVD Player is on")

    def play(self, movie):
        print(f"Playing {movie}")

    def off(self):
        print("DVD Player is off")


class Projector:
    def on(self):
        print("Projector is on")

    def setInput(self, source):
        print(f"Setting input to {source}")

    def off(self):
        print("Projector is off")


class SoundSystem:
    def on(self):
        print("Sound System is on")

    def setVolume(self, volume):
        print(f"Setting volume to {volume}")

    def off(self):
        print("Sound System is off")


# Facade
class HomeTheaterFacade:
    def __init__(self, dvd_player, projector, sound_system):
        self.dvd_player = dvd_player
        self.projector = projector
        self.sound_system = sound_system

    def watchMovie(self, movie):
        print("Get ready to watch a movie...")
        self.dvd_player.on()
        self.projector.on()
        self.projector.setInput("DVD")
        self.sound_system.on()
        self.sound_system.setVolume(10)
        self.dvd_player.play(movie)

    def endMovie(self):
        print("Shutting down the home theater...")
        self.dvd_player.off()
        self.projector.off()
        self.sound_system.off()


# Client code
def main():
    dvd_player = DVDPlayer()
    projector = Projector()
    sound_system = SoundSystem()

    home_theater = HomeTheaterFacade(dvd_player, projector, sound_system)

    home_theater.watchMovie("Inception")
    print("\nMovie's over, time to clean up...")
    home_theater.endMovie()


if __name__ == "__main__":
    main()
