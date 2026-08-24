class hello:
    def messege(self):
        print("Hello EveryOne");
        
a = hello();

a.messege()
a.messege()
a.messege()





class hello:
    def messege(self):
        print("Hello EveryOne");

    def bye(self):
        print("Bye EveryOne");
        
a = hello();
b = hello();

a.messege()
b.bye()





class hello:
    test = "-----Test------"
    def messege(self,name):
        print("Hello EveryOne",name);
        print(self.test)

    def bye(self,fname):
        print("Bye EveryOne",fname);
        
a = hello();
b = hello();

a.messege("salman")
b.bye("khan")