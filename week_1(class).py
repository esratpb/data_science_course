class Worker_Group():
    worker_list=[]
    salary=0
    
    def __init__(self,name="default",surname="default",email="default",salary=0,age=25):
        self.name=name
        self.surname=surname
        self.email=name+surname+"@gmail.com"
        self.salary=salary
        self.age=age
        self.worker_list.append(self)
        
    def __str__(self):
        self.view=self.name+" "+self.surname
        return self.view
    
    def raise_salary(self,rate):
        self.salary=(self.salary*rate)/100+self.salary    
        return self.salary

    
               
calisan1=Worker_Group("ayse","ak",salary=2100,age=26)
calisan2=Worker_Group("ali riza","demir",salary=2500,age=26)
calisan3=Worker_Group("nuri","ozturk",salary=1800,age=27)
calisan4=Worker_Group("fahri","karapinar",salary=2200,age=30)
calisan5=Worker_Group("ali","kara",salary=2000,age=25)
calisan6=Worker_Group("mehmet","sahin",salary=3000,age=25)
calisan7=Worker_Group("recep","semiz",salary=2600,age=24)
calisan8=Worker_Group("ahmet","sari",salary=3000,age=28)
calisan9=Worker_Group("ersan","yavuz",salary=2600,age=40)
calisan10=Worker_Group("ibrahim","akin",salary=2800,age=45)
calisan11=Worker_Group("recep","gunes",salary=2500,age=42)
calisan12=Worker_Group("sami","elibol",salary=2300,age=44)
calisan13=Worker_Group("seyfettin","koyun",salary=2400,age=38)
calisan14=Worker_Group("davut","kabasakal",salary=2200,age=35)
calisan15=Worker_Group("faruk","deniz",salary=3150,age=38)
calisan16=Worker_Group("cemil","akcay",salary=2800,age=33)
calisan17=Worker_Group("fatma","gunes",salary=2500,age=35)
calisan18=Worker_Group("elif","kansu",salary=2300,age=43)
calisan19=Worker_Group("cansu","cerez",salary=2400,age=48)
calisan20=Worker_Group("havva","gedik",salary=2200,age=40)
calisan21=Worker_Group("nesibe","kocak",salary=3150,age=45)

def raise_for_all(rate):
    print("----------------------------------------")
    sum_salary=0
    for person in Worker_Group.worker_list:
        sum_salary+=person.salary
    print("##Sum of the workers' salary : {}".format(sum_salary))

    new_sumsalary=sum_salary*((rate+100)/100)
    difference=sum_salary*rate/100
    print("""## New Sum of the workers' salary : {}
              ##Difference : {}""".format(new_sumsalary,difference))        
    for person in Worker_Group.worker_list:
        person.raise_salary(rate)
        print(str(person.salary)+" "+person.name+" "+person.surname)
    print("----------------------------------------")   
    return Worker_Group.worker_list



def sort_by_name():
    print("----------------------------------------")
    namesorted=[]
    for person in Worker_Group.worker_list:
        namesorted.append(person.name+" "+person.surname)
    namesorted.sort()
    for i in namesorted:
        print(i)
    print("----------------------------------------")
    return namesorted



def sort_by_salary():
    print("----------------------------------------")
    salarysorted=[]
    for person in Worker_Group.worker_list:
        salarysorted.append(str(person.salary)+" "+person.name+" "+person.surname)
    salarysorted.sort()
    for i in salarysorted:
        print(i)
    print("----------------------------------------")
    return salarysorted
    
        
        
    

raise_for_all(20)

sort_by_name()
sort_by_salary()

