class animals():
    a = "tamable animals"

class pets(animals):
    b = "big pets"


class dogs(pets):
    c = "bulldog"
    @staticmethod
    def bark():
        print("mai tumhare baap ka naukar nhi")


d = dogs
d.bark()