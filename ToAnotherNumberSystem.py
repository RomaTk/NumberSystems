def toSymbol(integer=0):
	listOfSymbols=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'];
	return listOfSymbols[integer];
def fromSymbol(symbol='1'):
	listOfSymbols=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'];
	return listOfSymbols.index(symbol);

class Integer:
	def __init__(self,number=0):
		self.dictionary={
			'10':str(number)
		}
		self.toSymbol=toSymbol;
		self.fromSymbol=fromSymbol;
		
	def to(self,system=1):
		result='';
		number=int(self.dictionary['10']);
		max_number_len=len(str(number));
		while number>0:
			mod=number%system;
			symbol=self.toSymbol(mod)
			result=symbol+result;
			number_len=len(str(number));
			toAdd='';
			for i in range(max_number_len-number_len):
				toAdd+=' ';
			print(toAdd+str(number)+':'+str(system)+'|'+symbol);
			number=number//system;
		if len(result)==0:
			result='0';
		self.dictionary[str(system)]=result;
		print('=> '+result+'\n');
		return result
	
	def check(self,system=1):
		number=self.dictionary[str(system)];
		index=len(number)-1;
		st='';
		for sym in number:
			st+=str(self.fromSymbol(sym))+'*('+str(system)+'^'+str(index)+')'
			if index!=0:
				st+='+';
			else:
				st+='=';
			index-=1;
		st+=number;
		print('Перевірка цілої частини:  '+st);
		
		
class Fractional:
	def __init__(self,number=0):
		self.dictionary={
			'10':number
		}
		self.toSymbol=toSymbol;
		self.fromSymbol=fromSymbol;
		
	def to(self,system=1):
		result='';
		number=int(self.dictionary['10']);
		max_number_len=len(str(number));
		for j in range(3):
			value=(10**max_number_len)
			integ=number*system//value;
			symbol=self.toSymbol(integ)
			result=result+symbol;
			number_len=len(str(number));
			toAdd='';
			for i in range(max_number_len-number_len):
				toAdd+=' ';
			print(toAdd+'0.'+str(number)+'*'+str(system)+'|'+symbol);
			number=(number*system)%value;
		self.dictionary[str(system)]=result;
		print('=> '+result+'\n');
		return result
	
class Number:
	def __init__(self,numberString=''):
		self.array=numberString.split('.');
		if len(self.array)<2:
			self.array.append('0');
		self.integer=Integer(int(self.array[0]));
		self.fractional=Fractional(int(self.array[1]));
	def to(self,system=0):
	
		print(str(self.array[0])+'.'+str(self.array[1])+'       з 10-ої до '+str(system)+'-ої'+'\n');
		
		integer=self.integer.to(system);
		fractional=self.fractional.to(system);
		
		print('Результат: '+integer+'.'+fractional+' ;');
		self.integer.check(system);
		print();
		print('----------------------------');
		print();
		
"""ch1=Number('891.334');
ch1.to(2);
ch1.to(8);
ch1.to(16);

ch2=Number('567.88');
ch2.to(2);
ch2.to(8);
ch2.to(16);

ch3=Number('277.881');
ch3.to(2);
ch3.to(8);
ch3.to(16);

ch4=Number('8.4');
ch4.to(2);
ch4.to(8);
ch4.to(16);

ch4=Number('4.23');
ch4.to(2);
ch4.to(8);
ch4.to(16);"""


ch1=Number('587.432');
ch1.to(2);
ch1.to(8);
ch1.to(16);

ch2=Number('452.99');
ch2.to(2);
ch2.to(8);
ch2.to(16);

ch3=Number('452.458');
ch3.to(2);
ch3.to(8);
ch3.to(16);

ch4=Number('4.8');
ch4.to(2);
ch4.to(8);
ch4.to(16);

ch4=Number('3.29');
ch4.to(2);
ch4.to(8);
ch4.to(16);


