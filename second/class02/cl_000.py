

class Phone:
    mobile_type = 'Common Phone'
    def __init__(self, model, imei):
        self._model = model
        self._imei = imei

    def call(self, to):
        self._connect_to_other_device(to)
        print(f'okey, i am calling {to} from {self._model}')

    def _connect_to_other_device(self,to):
        print('COnnection magic')

    def get_model(self):
        return self._model

    def set_model(self):
        return self._model

    def get_imei(self):
            return self._imei

    def set_imei(self):
        return self._imei

# print(Phone.mobile_type)
# phone  = Phone('Nokia', 'EZ12345678')
# phone.call("+38095791234")
# print(phone.imei)
# phone.phone_number = "+38095791234"
# print(phone.phone_number)
#
# print(phone.mobile_type)
#
# phone2  = Phone('Siemens', 'EZ12345678')
# phone2.call("+38095791234")
# print(phone2.imei)

# phone.mobile_type = "SMARTPHONE"
# print(Phone.mobile_type)
# print(phone.mobile_type)

# phone  = Phone('Nokia', 'EZ12345678')
# phone.call()
# phone._model
class MobilePhone(Phone):
    def seld_message(self, message_text, to ):
        print(f'sending message {message_text} to {to}')

class SatelitePhone(Phone):
    def call(self, satelite_coordinates, to):
        print(f'Calling {to} from {self.get_model()} satelite: {satelite_coordinates}')

class SmartPhone (Phone):
    def play_audio(self):
            print ("Playing audio")

    def play_video(self):
        print ("Playing video")

    def download_app(self, app_name, market_place):
        app = Application(app_name, market_place)
        app.download()
        self._app = app

    def start_app(self, app_obj):
        app_obj.start()

class Application:
    def __init__(self, name, marketplace):
        self._name = name
        self._marketplace = marketplace
        self._downloaded = False

    def start(self):
        if self._downloaded:
            print(f'Starting the {self._name} application')

    def download(self):
        print(f'Downloading {self._name} from {self._marketplace}')

#
#
# mobile_phone = MobilePhone('model', 'PPPZZZZ')
# mobile_phone.call('+380686800351')
# print(mobile_phone.get_model())
#
# satelite_phone = SatelitePhone('saturn', "+38094323588")
# satelite_phone.call('60.5/23.5', "+38094323588")

smartphone= SmartPhone('Apple', '777777')
#smartphone.download_app('Player','PlayMarket')
#smartphone.start_app()

app = Application('Player','PlayMarket')
app.download()
smartphone.start_app(app)

class Cat:
    def __init__(self, name, weight):
        self._name = name
        self._weight  =3

    def __add__(self,other):
        return Cat(self._name  + other._name, self._weight  + other._weight)

        return len(self) + len(other)
    def __len__(self):
        return 1

class ColeredCat(Cat):
    def __init__(self, name, weight,color):
        self._color = color
        super().__init__(name, weight)


cat1 = Cat('kitty', 3)
cat2 = Cat('cat', 4)
cat3 = cat1 +cat2
print (cat3._name, cat3._weight)