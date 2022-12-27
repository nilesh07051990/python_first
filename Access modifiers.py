# pubic,private,protcted access modifiers
class sample:
    a = 100 #public
    _b = 200 #protected
    __c = 300 #private
    def test(self):
        print(sample.a)
        print(sample._b)
        print(sample.__c)

obj=sample()
#obj.test()

print(sample.a)
print(sample._b)
print(obj._sample__c) #name mangling method by which we can access private Access modifier outside the class
