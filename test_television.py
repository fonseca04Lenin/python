import pytest
from television import Television

# Unit tests for Television class methods
class TestTelevision:
    def test_init(self):
        tv = Television()
        assert tv._Television__status == False
        assert tv._Television__muted == False
        assert tv._Television__volume == Television.MIN_VOLUME
        assert tv._Television__channel == Television.MIN_CHANNEL

    def test_power(self):
        tv = Television()
        tv.power()
        assert tv._Television__status == True
        tv.power()
        assert tv._Television__status == False

    def test_mute(self):
        tv = Television()
        tv.mute()
        assert tv._Television__muted == False  # Mute should not work when TV is off
        tv.power()
        tv.mute()
        assert tv._Television__muted == True
        tv.mute()
        assert tv._Television__muted == False

    def test_channel_up(self):
        tv = Television()
        tv.channel_up()
        assert tv._Television__channel == 1
        tv._Television__channel = Television.MAX_CHANNEL
        tv.channel_up()  # should reset to MIN_CHANNEL
        assert tv._Television__channel == Television.MIN_CHANNEL

    def test_channel_down(self):
        tv = Television()
        tv.channel_down()
        assert tv._Television__channel == Television.MAX_CHANNEL
        tv._Television__channel = Television.MIN_CHANNEL
        tv.channel_down()  # should reset to MAX_CHANNEL
        assert tv._Television__channel == Television.MAX_CHANNEL

    def test_volume_up(self):
        tv = Television()
        tv.volume_up()
        assert tv._Television__volume == 1
        tv._Television__volume = Television.MAX_VOLUME
        tv.volume_up()  # should remain at MAX_VOLUME
        assert tv._Television__volume == Television.MAX_VOLUME

    def test_volume_down(self):
        tv = Television()
        tv.volume_down()
        assert tv._Television__volume == Television.MIN_VOLUME
        tv._Television__volume = Television.MAX_VOLUME
        tv.volume_down()
        assert tv._Television__volume == Television.MAX_VOLUME - 1

if __name__ == "__main__":
    pytest.main()

      
