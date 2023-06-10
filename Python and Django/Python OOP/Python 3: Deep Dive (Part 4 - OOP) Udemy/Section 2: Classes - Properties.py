# Difference between attributes and properties
# Attributes are data stored in an object or instance of a class and can be accessed using dot notation. Properties are attributes that have getter and setter methods. CHECK THIS


# can set property using property class
class MyClass: 
    def __init__ (self, language):
        self._language=language
        
    def get_language(self):
        return self._language

    def set_language(self, value):
        self._language = value

    language = property(fget=get_language, fset=set_language)

# can also use decorators to set property
class MyClass: 
    def __init__ (self, language):
        self._language=language
    
    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        self._language = value

# Caching computed properties so unless the radius changes, the area is not recalculated. This is one application of properties. It makes sense for area to be a property rather than a method. 
class Circle:
    def __init__(self, r):
        self._r=r 
        self._area = None
    
    @property
    def radius(self):
        return self._r
    
    @radius.setter
    def radius(self, r):
        if r<0:
            raise ValueError("Radius must be non-negative")
        self._r=r
        # if radius changes, area must be recalculated so set to None
        self._area=None
        
    @property
    def area(self):
        if self._area is None:
            self._area = math.pi*(self._r**2)
        return self._area
    
    
# Another example of caching computed properties. This time, we are caching the page size and load time.
class WebPage: 
    def __init__(self, url):
        self.url = url 
        self._page = None 
        self._load_time_secs = None
        self._page_size = None
        
    @property
    def url(self):
        return self._url
    
    @url.setter
    def url(self, value):
        if not value.startswith('http'):
            raise ValueError('Invalid URL')
        self._url = value
        self._page = None
        
    @property
    def page(self):
        if self._page is None:
            self.download_page()
        return self._page
    
    @property
    def page_size(self):
        if self._page_size is None:
            self._page_size = len(self.page)
        return self._page_size
    
    @property
    def time_elapsed(self):
        if self._load_time_secs is None:
            self.download_page()
        return self._load_time_secs
    
    def download_page(self):
        self._page_size = None
        self._load_time_secs = None
        start_time = perf_counter()
        with urllib.request.urlopen(self.url) as f:
            self._page = f.read()
        end_time = perf_counter()
        self._page_size = len(self._page)
        self._load_time_secs = end_time - start_time
        
# Deleting properties from an object or instance
# You can use a decorator to delete a property: @property_name.deleter. This will call the deleter method. 

# You can bound methods to a class using a decorator: @classmethod. 

# Static methods are functions that are not bound to anyting: @staticmethod. 

class Timer: 
    tz = timezone.utc
    
    @classmethod 
    def set_tz(cls, offset, name):
        cls.tz = timezone(timedelta(hours=offset), name)
        
    @staticmethod
    def current_dt_utc():
        return datetime.now(timezone.utc)
    
    @classmethod
    def current_dt(cls):
        return datetime.now(cls.tz)
    
    def start(self):   
        self._time_start = self.current_dt_utc()
        self._time_end = None
        
    def stop(self):
        if self._time_start is None:
            raise ValueError('Timer not started')
        self._time_end = self.current_dt_utc()
        
    @property
    def start_time(self):
        if self._time_start is None:
            raise ValueError('Timer not started')
        return self._time_start.astimezone(self.tz)
    
    @property
    def end_time(self):
        if self._time_end is None:
            raise ValueError('Timer not stopped')
        return self._time_end.astimezone(self.tz)
    
    @property
    def elapsed(self):
        if self._time_start is None:
            raise ValueError('Timer not started')
        if self._time_end is None:
            elapsed_time = self.current_dt_utc() - self._time_start
        else:
            elapsed_time = self._time_end - self._time_start
        return elapsed_time.total_seconds()
    
# Example

class Language:
    MAJOR = 3
    MINOR = 7
    REVISION = 4
    FULL = '{}.{}.{}'.format(MAJOR, MINOR, REVISION) 
    # no need to use self since it is a class attribute
    
    @property
    def version(self):
        return '{}.{}.{}'.format(self.MAJOR, self.MINOR, self.REVISION)
    # must use self since it is an instance attribute
    
    @classmethod
    def cls_version(cls):
        return '{}.{}.{}'.format(cls.MAJOR, cls.MINOR, cls.REVISION)
    # must use cls since it is a class method. 
    
    @staticmethod
    def static_version():
        return '{}.{}.{}'.format(Language.MAJOR, Language.MINOR, Language.REVISION)
    # must use Language since it is a static method. 
    