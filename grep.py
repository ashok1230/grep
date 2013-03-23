class grep:
    def read1(self,file):
	self.f=file
	fd=open(self.f,'r')
	txt=fd.read()
	return txt
class main(grep):
    def method(self,name,line):
	data=grep.read1(self,name)
	self.line=line
	s=''
	for i in data:
	    if i!='\n':
		s=s+i
	    else:
		a=s.find(self.line)
		if a!=-1:
		    print s
		s=''

a=main()
a.method('text.txt','ashok')