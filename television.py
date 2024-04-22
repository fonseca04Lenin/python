class Television:
    # Class variables
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        Initializes a Television object with default settings.
        """
        # Instance variables
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Toggles the power status of the television.
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Mutes or unmutes the television if it is powered on.
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        Increases the channel by one, wrapping around to MIN_CHANNEL if it reaches MAX_CHANNEL.
        """
        if self.__status:
            self.__channel = (self.__channel + 1) % (Television.MAX_CHANNEL + 1)

    def channel_down(self) -> None:
        """
        Decreases the channel by one, wrapping around to MAX_CHANNEL if it reaches MIN_CHANNEL.
        """
        if self.__status:
            self.__channel = (self.__channel - 1) % (Television.MAX_CHANNEL + 1)

    def volume_up(self) -> None:
        """
        Increases the volume by one, if not muted, up to MAX_VOLUME.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Decreases the volume by one, if not muted, down to MIN_VOLUME.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Returns a string representation of the television's status, channel, and volume.
        """
        volume_str = "Muted" if self.__muted else str(self.__volume)
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {volume_str}"
