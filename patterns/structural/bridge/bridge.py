from abc import ABC, abstractmethod


class DeviceError(Exception):
    pass


class VolumeOutOfRangeError(DeviceError):
    pass


class TvError(DeviceError):
    pass


class ChannelError(TvError):
    pass


class LaptopError(DeviceError):
    pass


class WiFiError(LaptopError):
    pass


class Device(ABC):
    def __init__(self):
        self.__enabled = False
        self.__volume = 0

    def is_enabled(self) -> bool:
        return self.__enabled

    def enable(self):
        self.__enabled = True
        print(f'Enable {self.__class__.__name__}')

    def disable(self):
        self.__enabled = False
        print(f'Disable {self.__class__.__name__}')

    @property
    def volume(self) -> int:
        return self.__volume

    @volume.setter
    def volume(self, value: int):
        if self.is_enabled():
            if 0 <= value <= 100:
                if isinstance(value, int):
                    self.__volume = value
                    print(f'{self.__class__.__name__} volume set to {self.volume}')
                else:
                    raise TypeError('Volume value must be integer.')
            else:
                raise VolumeOutOfRangeError('Volume value must be between 0 and 100')
        else:
            raise DeviceError(f'{self.__class__.__name__} must be enabled')

    @property
    @abstractmethod
    def channel(self):
        pass

    @channel.setter
    @abstractmethod
    def channel(self, value):
        pass

    @abstractmethod
    def enable_wifi(self):
        pass

    @abstractmethod
    def disable_wifi(self):
        pass

    @property
    @abstractmethod
    def wifi(self):
        pass


class Tv(Device):
    def __init__(self):
        super().__init__()
        self.__channel = None

    def enable(self):
        super().enable()
        if self.__channel is None:
            self.__channel = 0

    @property
    def channel(self) -> int:
        if self.__channel is not None and self.is_enabled():
            return self.__channel
        else:
            raise ChannelError(f'You must enable {self.__class__.__name__} before getting channel')

    @channel.setter
    def channel(self, value: int):
        if self.is_enabled():
            if isinstance(value, int):
                self.__channel = value
                print(f'Channel changed to {self.__channel}')
            else:
                raise TypeError('Channel must be integer')
        else:
            raise ChannelError(f'You must enable {self.__class__.__name__} before setting channel')

    @property
    def wifi(self):
        raise TvError(f'{self.__class__.__name__} is not smart')

    def enable_wifi(self):
        raise TvError(f'{self.__class__.__name__} is not smart')

    def disable_wifi(self):
        raise TvError(f'{self.__class__.__name__} is not smart')


class Laptop(Device):
    def __init__(self):
        super().__init__()
        self.__wifi = False

    @property
    def wifi(self):
        if self.is_enabled():
            return self.__wifi
        else:
            raise WiFiError(f'You must enable {self.__class__.__name__} before getting wifi position')

    def enable_wifi(self):
        if self.is_enabled():
            self.__wifi = True
            print(f'Wi-Fi enabled on {self.__class__.__name__}')
        else:
            raise WiFiError(f'You must enable {self.__class__.__name__} before setting wifi position')

    def disable_wifi(self):
        if self.is_enabled():
            self.__wifi = False
            print(f'Wi-Fi enabled on {self.__class__.__name__}')

        else:
            raise WiFiError(f'You must enable {self.__class__.__name__} before setting wifi position')

    @property
    def channel(self):
        raise LaptopError(f"{self.__class__.__name__} doesn't have any channels")

    @channel.setter
    def channel(self, value):
        raise LaptopError(f"{self.__class__.__name__} doesn't have any channels")


class RemoteControl:
    def __init__(self, device: Device):
        self._device = device

    def toggle_power(self):
        if self._device.is_enabled():
            self._device.disable()
        else:
            self._device.enable()

    def volume_up(self):
        self._device.volume += 1

    def volume_down(self):
        self._device.volume -= 1

    @property
    def volume(self):
        return self._device.volume

    @volume.setter
    def volume(self, value: int):
        self._device.volume = value

    def mute(self):
        self._device.volume = 0


class AdvancedRemoteControl(RemoteControl):

    @property
    def channel(self) -> int:
        return self._device.channel

    @channel.setter
    def channel(self, value: int):
        self._device.channel = value

    @property
    def wifi(self) -> bool:
        return self._device.wifi

    def enable_wifi(self):
        self._device.enable_wifi()

    def disable_wifi(self):
        self._device.disable_wifi()


if __name__ == '__main__':
    laptop = Laptop()
    control = AdvancedRemoteControl(laptop)
    control.toggle_power()
    control.volume = 25
    control.mute()
