class Dad:
    def details(self):
        print('He is my dad')

class Me(Dad):
    def m_details(self):
        print('He is me')

class Myson(Me):
    def e_details(self):
        print('He is my son')

ob1 = Dad()
ob2 = Me()
ob3 = Myson()

ob3.details()
# ob3.p_details()
ob2.m_details()


