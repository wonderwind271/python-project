class course:
    def __init__(self, CourseCode, CourseName, credit, grade, Ctype):
        self.CourseCode=CourseCode
        self.CourseName=CourseName
        self.credit=credit
        self.grade=grade
        self.Ctype=Ctype  # E:engineering course  J: JI(non engineering) course  M: MoE/SJTU required course(non JI)
        if grade=='A+' or grade=='A':
            self.GPA=4.0
        elif grade=='A-':
            self.GPA=3.7
        elif grade=='B+':
            self.GPA=3.3
        elif grade=='B':
            self.GPA=3
        elif grade=='B-':
            self.GPA=2.7
        elif grade=='C+':
            self.GPA=2.3
        elif grade=='C':
            self.GPA=2
        elif grade=='C-':
            self.GPA=1.7
        elif grade=='D':
            self.GPA=1
        elif grade=='F':
            self.GPA=0
        else:
            self.GPA='P'
            self.grade='P'
            print("Regarded as Pass, no influence to GPA!")
        self.retakeable=False
        if self.GPA<2:
            self.retakeable=True
        
    def show(self):
        if self.Ctype=='E':
            coursetype="Engineering course"
        elif self.Ctype=='J':
            coursetype="JI non engineering course"
        else:
            coursetype="MoE/SJTU required (non-JI)"
        
        print(f'course code: {self.CourseCode}, name: {self.CourseName}, credit: {self.credit}, grade: {self.grade} (GPA={self.GPA}), type: {coursetype}')
def addin(All): #add course
    print("please input the course Code, Course Name, credit, letter grade, course type(E, J, M).")
    a1=input()
    a2=input()
    a3=float(input())
    a4=input()
    a5=input()
    temp=course(a1,a2,a3,a4,a5)
    All.append(temp)
    templist=[a1,a2,a3,a4,a5]
    return templist

AllCourse=[]

#test
'''
aa=course("Vg101","Introduction to Computer and Programming",4,"A",'E')
bb=course("Vy100","Academic Writing I",4,"B+",'J')
AllCourse.append(aa)
AllCourse.append(bb)
AllCourse.append(course("Vv186","Honor Mathematics II",4,"A+",'E'))
AllCourse.append(course("Vc210","Chemistry",4,"A-",'E'))
'''
# read course information from txt
fr=open('GPA.txt',mode='r')

while 1:
    
    # read 5 lines, save into Allcourse list
    jumpout=0
    temp=[]
    for i in range(5):
        line=fr.readline()
        
        if line==''or line=='\n':
            jumpout=1
            break
        else: # gather 5 "line" and init the class
            line=line[:-1]
            temp.append(line)
    if jumpout==1:
        break
    else:
        initcourse=course(temp[0],temp[1],float(temp[2]),temp[3],temp[4])
        AllCourse.append(initcourse)
            
fr.close()
while True: #get course information from stdin
    print("Add course and save:1\nAdd course(test, not save):0\nDelete course from files:del\nother input:quit")
    print("please input your choice\n> ",end='')
    cin=input()
    if cin=='1':
        fp=open('GPA.txt','a')
        ctemp=addin(AllCourse)
        for i in ctemp:
            fp.write(str(i))
            fp.write('\n')
        #fp.write('NEXT\n')
        fp.close()
    elif cin=='del':
        print("These are the courses, please choose which one to delete")
        for i in AllCourse:
            i.show()
        print('Please input the line of course to delete. Input integers:',end='')
        DelLine=int(input())
        del AllCourse[DelLine-1]  # delete from list
        # delete the course from the file
        fp=open('GPA.txt','w')  # rewrite back and omit the deleted line
        for i in AllCourse:
            ii = [i.CourseCode, i.CourseName, str(i.credit), i.grade, i.Ctype]
            for j in ii:
                fp.write(j+'\n')

        print("course deleted")
        fp.close()
        for i in AllCourse:
            i.show()
        
    elif cin=='0':
        addin(AllCourse)
    else:
        break
        

credit=0;GP=0;Gcredit=0
GPA=0
for i in AllCourse:
    if i.grade=='P':
        credit+=i.credit
    elif i.grade=='F':
        Gcredit+=i.credit
    else:
        credit+=i.credit
        Gcredit+=i.credit
        GP+=i.credit*i.GPA

    i.show()
if Gcredit==0:
    print("No course listed")
else:
    GPA=GP/Gcredit
    print(f'total credit gained: {credit}, GPA: {GPA}')

#cal engineer GPA
EGP=0
EGcridit=0
for i in AllCourse:
    if i.Ctype=='E':
        EGcridit+=i.credit
        EGP+=i.GPA*i.credit
if EGP==0:
    print("No engineer course")
else:
    EGPA=EGP/EGcridit
    print("Engineering GPA=",EGPA)
