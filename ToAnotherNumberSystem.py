"""def multiply(number1=None,number2=None,toSymbol=None,fromSymbol=None,Number=None):
	def to_normal_size_integer(number1_string='',number2_string=''):
		def work_with_biggerString(stringBigger='',stringSmaller=''):
			for index in range(len(stringBigger)-len(stringSmaller)):
				stringSmaller='0'+stringSmaller;
			return stringBigger,stringSmaller
		if len(number1_string)>len(number2_string):
			number1_string,number2_string=work_with_biggerString(number1_string,number2_string);
		elif len(number1_string)<len(number2_string):
			number1_string,number2_string=work_with_biggerString(number2_string,number1_string);
		return number1_string,number2_string
		
	def to_normal_size_fractional(number1_string='',number2_string=''):
		def work_with_biggerString(stringBigger='',stringSmaller=''):
			for index in range(len(stringBigger)-len(stringSmaller)):
				stringSmaller=stringSmaller+'0';
			return stringBigger,stringSmaller
		if len(number1_string)>len(number2_string):
			number1_string,number2_string=work_with_biggerString(number1_string,number2_string);
		elif len(number1_string)<len(number2_string):
			number1_string,number2_string=work_with_biggerString(number2_string,number1_string);
		return number1_string,number2_string
	
	def doMultiply(number1_string='01.12',number2_string='18.12',system=1,toSymbol=None,fromSymbol=None):
		result='';
		discharge_array=[];
		toAdd=0;
		for index in range(len(number1_string)-1,-1,-1):
			if number1_string[index]=='.':
				result='.'+result;
			else:
				summary=toAdd+fromSymbol(number1_string[index])+fromSymbol(number2_string[index]);
				if summary>=system:
					result=toSymbol(summary-system)+result;
					toAdd=(summary)//(system);
				elif summary<system:
					result=toSymbol(summary)+result;
					toAdd=0;
				discharge_array.insert(0,str(toAdd));
		if toAdd!=0:
			result=str(toAdd)+result;
			discharge_array.insert(0,str(toAdd));
		
		print('1 - переноситься розряд, 0 - не переноситься розряд: '+' , '.join(discharge_array));
		
		return result;
		
	return_array=[];
	for system_string in number1.dictionary:
		if (number2.dictionary[system_string]!=None):
			integer_number1,integer_number2=to_normal_size_integer(number1.integer.dictionary[system_string],number2.integer.dictionary[system_string]);
			result=doMultiply(number1_string_full,number2_string_full,int(system_string),toSymbol,fromSymbol);
			if len(result)>len(number1_string_full):
				for index in range(len(result)-len(number1_string_full)):
					number1_string_full=' '+number1_string_full;
					number2_string_full=' '+number2_string_full;
			print(number1_string_full);
			print('+');
			print(number2_string_full);
			st='';
			for index in range(len(result)):
				st+='-';
			print(st);
			print(result);
			print();
			print();
			
			return_array.append(result);
	return return_array;"""






			

def plus(number1=None,number2=None,toSymbol=None,fromSymbol=None,Number=None):
	def to_normal_size_integer(number1_string='',number2_string=''):
		def work_with_biggerString(stringBigger='',stringSmaller=''):
			for index in range(len(stringBigger)-len(stringSmaller)):
				stringSmaller='0'+stringSmaller;
			return stringBigger,stringSmaller
		if len(number1_string)>len(number2_string):
			number1_string,number2_string=work_with_biggerString(number1_string,number2_string);
		elif len(number1_string)<len(number2_string):
			number1_string,number2_string=work_with_biggerString(number2_string,number1_string);
		return number1_string,number2_string
		
	def to_normal_size_fractional(number1_string='',number2_string=''):
		def work_with_biggerString(stringBigger='',stringSmaller=''):
			for index in range(len(stringBigger)-len(stringSmaller)):
				stringSmaller=stringSmaller+'0';
			return stringBigger,stringSmaller
		if len(number1_string)>len(number2_string):
			number1_string,number2_string=work_with_biggerString(number1_string,number2_string);
		elif len(number1_string)<len(number2_string):
			number1_string,number2_string=work_with_biggerString(number2_string,number1_string);
		return number1_string,number2_string
	
	def doAdd(number1_string='01.12',number2_string='18.12',system=1,toSymbol=None,fromSymbol=None):
		result='';
		discharge_array=[];
		toAdd=0;
		for index in range(len(number1_string)-1,-1,-1):
			if number1_string[index]=='.':
				result='.'+result;
			else:
				summary=toAdd+fromSymbol(number1_string[index])+fromSymbol(number2_string[index]);
				if summary>=system:
					result=toSymbol(summary-system)+result;
					toAdd=(summary)//(system);
				elif summary<system:
					result=toSymbol(summary)+result;
					toAdd=0;
				discharge_array.insert(0,str(toAdd));
		if toAdd!=0:
			result=str(toAdd)+result;
			discharge_array.insert(0,str(toAdd));
		
		print('1 - переноситься розряд, 0 - не переноситься розряд: '+' , '.join(discharge_array));
		
		return result;
		
	resultNumber=Number('0');
	for system_string in number1.dictionary:
		if (number2.dictionary[system_string]!=None):
			integer_number1,integer_number2=to_normal_size_integer(number1.integer.dictionary[system_string],number2.integer.dictionary[system_string]);
			fractional_number1,fractional_number2=to_normal_size_integer(number1.fractional.dictionary[system_string],number2.fractional.dictionary[system_string]);
			number1_string_full=integer_number1+'.'+fractional_number1;
			number2_string_full=integer_number2+'.'+fractional_number2;
			result=doAdd(number1_string_full,number2_string_full,int(system_string),toSymbol,fromSymbol);
			if len(result)>len(number1_string_full):
				for index in range(len(result)-len(number1_string_full)):
					number1_string_full=' '+number1_string_full;
					number2_string_full=' '+number2_string_full;
			print(number1_string_full);
			print('+');
			print(number2_string_full);
			st='';
			for index in range(len(result)):
				st+='-';
			print(st);
			print(result);
			print();
			print();
			
			resultNumber.add_number_in_system(result,int(system_string));
	return resultNumber;
	
def minus(number1=None,number2=None,toSymbol=None,fromSymbol=None,Number=None):
	def to_normal_size_integer(number1_string='',number2_string=''):
		def work_with_biggerString(stringBigger='',stringSmaller=''):
			for index in range(len(stringBigger)-len(stringSmaller)):
				stringSmaller='0'+stringSmaller;
			return stringBigger,stringSmaller
		if len(number1_string)>len(number2_string):
			number1_string,number2_string=work_with_biggerString(number1_string,number2_string);
		elif len(number1_string)<len(number2_string):
			number1_string,number2_string=work_with_biggerString(number2_string,number1_string);
		return number1_string,number2_string
		
	def to_normal_size_fractional(number1_string='',number2_string=''):
		def work_with_biggerString(stringBigger='',stringSmaller=''):
			for index in range(len(stringBigger)-len(stringSmaller)):
				stringSmaller=stringSmaller+'0';
			return stringBigger,stringSmaller
		if len(number1_string)>len(number2_string):
			number1_string,number2_string=work_with_biggerString(number1_string,number2_string);
		elif len(number1_string)<len(number2_string):
			number1_string,number2_string=work_with_biggerString(number2_string,number1_string);
		return number1_string,number2_string
	
	def doMinus(number1_string='01.12',number2_string='18.12',system=1,toSymbol=None,fromSymbol=None):
		result='';
		discharge_array=[];
		toMinus=0;
		for index in range(len(number1_string)-1,-1,-1):
			if number1_string[index]=='.':
				result='.'+result;
			else:
				summary=fromSymbol(number1_string[index])-fromSymbol(number2_string[index])-toMinus;
				if summary<0:
					result=toSymbol(summary+system)+result;
					toMinus=1;
				else:
					result=toSymbol(summary)+result;
					toMinus=0;

				discharge_array.insert(0,str(toMinus));
		print('1 - переноситься розряд, 0 - не переноситься розряд: '+' , '.join(discharge_array));
		
		return result;
		
	resultNumber=Number('0');
	for system_string in number1.dictionary:
		if (number2.dictionary[system_string]!=None):
			integer_number1,integer_number2=to_normal_size_integer(number1.integer.dictionary[system_string],number2.integer.dictionary[system_string]);
			fractional_number1,fractional_number2=to_normal_size_integer(number1.fractional.dictionary[system_string],number2.fractional.dictionary[system_string]);
			number1_string_full=integer_number1+'.'+fractional_number1;
			number2_string_full=integer_number2+'.'+fractional_number2;
			result=doMinus(number1_string_full,number2_string_full,int(system_string),toSymbol,fromSymbol);
			resultNumber.add_number_in_system(result,int(system_string));
			if len(number1_string_full)>len(result):
				for index in range(len(number1_string_full)-len(result)):
					result=' '+result;
					result=' '+result;
			print(number1_string_full);
			print('-');
			print(number2_string_full);
			st='';
			for index in range(len(result)):
				st+='-';
			print(st);
			print(result);
			print();
			print();
			
	return resultNumber;
				


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
		st+=self.dictionary['10'];
		print('Перевірка цілої частини:  '+st);
		
		
class Fractional:
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
		for j in range(10):
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
		
	def check(self,system=1):
		number=self.dictionary[str(system)];
		index=1;
		result=0;
		st='';
		for sym in number:
			stepResult=self.fromSymbol(sym)*(system**(-index));
			result+=stepResult;
			st+=str(self.fromSymbol(sym))+'*('+str(system)+'^(-'+str(index)+'))'
			if index!=len(number):
				st+='+';
			else:
				st+='=';
			index+=1;
		st+=str(result);
		print('Перевірка частини після коми:  '+st);
	
	
class Number:
	def __init__(self,numberString='0'):
		self.array=numberString.split('.');
		if len(self.array)<2:
			self.array.append('0');
		self.integer=Integer(int(self.array[0]));
		self.fractional=Fractional(int(self.array[1]));
		
		self.dictionary={};
		for system in self.integer.dictionary:
			self.dictionary[system]=self.integer.dictionary[system]+'.'+self.fractional.dictionary[system];
	def to(self,system=0):
	
		print(str(self.array[0])+'.'+str(self.array[1])+'       з 10-ої до '+str(system)+'-ої'+'\n');
		
		integer=self.integer.to(system);
		fractional=self.fractional.to(system);
		
		print('Результат: '+integer+'.'+fractional+' ;');
		self.integer.check(system);
		self.fractional.check(system);
		print();
		print('----------------------------');
		print();
		
		self.dictionary[str(system)]=self.integer.dictionary[str(system)]+'.'+self.fractional.dictionary[str(system)];
		
	def add_number_in_system(self,numberString='',system=1):
		self.dictionary[str(system)]=numberString;
		numberString_array=numberString.split('.');
		self.integer.dictionary[str(system)]=numberString_array[0];
		self.fractional.dictionary[str(system)]=numberString_array[1];

ch1=Number('891.334');
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

ch5=Number('4.23');
ch5.to(2);
ch5.to(8);
ch5.to(16);

minus(plus(ch1,ch2,toSymbol,fromSymbol,Number),ch3,toSymbol,fromSymbol,Number);

