class Record:
    def __init__(self, index, last_name, other_names, voter_id, age, page, station_code, station_name,
                 constituency, district, region):
        self.index = index
        self.voter_id = voter_id
        self.age = age
        self.page = page
        self.station_code = station_code
        self.station_name = station_name
        self.constituency = constituency
        self.district = district
        self.region = region
        self.last_name = last_name
        self.other_names = other_names

    @property
    def index(self):
        return self._index

    @property
    def full_name(self):
        return f'{self._last_name},{self._other_names}'

    @property
    def voter_id(self):
        return self._voter_id

    @property
    def age(self):
        return self._age

    @property
    def station_code(self):
        return self._station_code

    @property
    def station_name(self):
        return self._station_name

    @property
    def constituency(self):
        return self._constituency

    @property
    def district(self):
        return self._district

    @property
    def region(self):
        return self._region

    @property
    def page(self):
        return self._page

    @property
    def last_name(self):
        return self._last_name

    @property
    def other_names(self):
        return self._other_names

    @index.setter
    def index(self, value):
        self._index = value

    @voter_id.setter
    def voter_id(self, value):
        self._voter_id = value

    @age.setter
    def age(self, value):
        self._age = value

    @page.setter
    def page(self, value):
        self._page = value

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @station_code.setter
    def station_code(self, value):
        self._station_code = value

    @station_name.setter
    def station_name(self, value):
        self._station_name = value

    @constituency.setter
    def constituency(self, value):
        self._constituency = value

    @district.setter
    def district(self, value):
        self._district = value

    @region.setter
    def region(self, value):
        self._region = value

    @other_names.setter
    def other_names(self, value):
        self._other_names = value

