from example import keylog
def check_keylog():
        keylog()
        final2=''
        print("log created")
        f1=open("log.txt","r")
        f2=open("exambank.txt","r")
        nonempty_lines = [line.strip("\n") for line in f1 if line != "\n"]
        line_countf1 = len(nonempty_lines)
        nonempty_lines1 = [line.strip("\n") for line in f2 if line != "\n"]
        line_countf2 = len(nonempty_lines1)
        print(line_countf1,line_countf2)
        f1=open("log.txt","r")
        lst=[]
        for i in range(line_countf1):
            s1=f1.readline().lower()
            f2=open("exambank.txt","r")
            for j in range(line_countf2):
                s2=f2.readline().lower().strip('\n')
                print(s1,s2)
                if s2 in s1:
                    lst.append(s2)
            final2="you are cheating with {}".format(lst)

        return final2               
     