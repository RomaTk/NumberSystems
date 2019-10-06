def cut_fractional_zeros(fractional_string='120'):
	index=len(fractional_string)-1;
	while (fractional_string[index]=='0')and(index>=0):
		index-=1;
	fractional_string=fractional_string[0:index+1];
	return fractional_string

def cut_integer_zeros(integer_string='0121'):
	index=0;
	while (integer_string[index]=='0')and(index<len(integer_string)-1):
		index+=1;
	integer_string=integer_string[index:len(integer_string)];
	return integer_string

def multiply_main(number1=None,number2=None,toSymbol=None,fromSymbol=None,Number=None,plus=None,cut_fractional_zeros=None,show=True):
	def multiplyStrings(number1_string='1323.2323',number2_string='32323.2323',number2=None,numbers_after_dot=0,system=1):
		if show:
			print('МНОЖЕННЯ в системі числення '+str(system)+' : '+number1_string+'*'+number2_string);
			print("###########################################################");
			print("Дії підчас нього:");
		number1_string=number1_string.replace('.','');
		number2_string=number2_string.replace('.','');
		toShow_strings=[];
		result=Number('0');
		result.add_number_in_system('0',system);
		nulls_string='';
		for index2 in range(len(number2_string)-1,-1,-1):
			toNext='0';
			step_1_result='';
			for index1 in range(len(number1_string)-1,-1,-1):
				toNext_number=Number(str(fromSymbol(toNext)));
				toNext_number.add_number_in_system(toNext,system);
				step_2_result,toNext=multiplyTwoSymbols(number1_string[index1],number2_string[index2],system);
				newNumber_0=Number(str((fromSymbol(number1_string[index1])*fromSymbol(number2_string[index2]))%10));
				newNumber_0.add_number_in_system(toNext+step_2_result,system);
				newNumber=plus(newNumber_0,toNext_number,toSymbol,fromSymbol,Number,False);
				if len(newNumber.integer.dictionary[str(system)])>1:
					toNext=newNumber.integer.dictionary[str(system)][0];
					step_2_result=newNumber.integer.dictionary[str(system)][1];
				else:
					toNext='0';
					step_2_result=newNumber.integer.dictionary[str(system)][0];
				step_1_result=step_2_result+step_1_result;
			if toNext!='0':
				step_1_result=toNext+step_1_result;
			step_1_result=step_1_result+nulls_string;
			newNumber=Number(str(fromSymbol(number1_string[index1])*float(number2.dictionary['10'])*(system**len(nulls_string))));
			newNumber.add_number_in_system(step_1_result,system);
			result=plus(result,newNumber,toSymbol,fromSymbol,Number);
			toShow_strings.append(newNumber.integer.dictionary[str(system)]);
			nulls_string+='0';
		if show:
			print("Саме множення:");
		number1_string=" "*(len(result.integer.dictionary[str(system)])-len(number1_string))+number1_string;
		number2_string=" "*(len(result.integer.dictionary[str(system)])-len(number2_string))+number2_string;
		if show:
			print(number1_string);
			print('x');
			print(number2_string);
			print('-'*len(result.integer.dictionary[str(system)]));
		k=len(toShow_strings);
		for string in toShow_strings:
			if show:
				print(' '*(len(result.integer.dictionary[str(system)])-len(string))+string);
			k-=1;
			if k>0:
				if show:
					print('+');
		if show:
			print('-'*len(result.integer.dictionary[str(system)]));
		moment_string=result.integer.dictionary[str(system)];
		result.integer.dictionary[str(system)]=moment_string[0:len(moment_string)-numbers_after_dot];
		result.fractional.dictionary[str(system)]=moment_string[len(moment_string)-numbers_after_dot:len(moment_string)];
		if show:
			print(moment_string+' => '+result.integer.dictionary[str(system)]+'.'+result.fractional.dictionary[str(system)]);
		result.integer.check(system);
		result.fractional.check(system);
		result.dictionary[str(system)]=result.integer.dictionary[str(system)]+'.'+result.fractional.dictionary[str(system)];
		if show:
			print("###########################################################");
			print();
			print();
		return result
	def multiplyTwoSymbols(symbol1='1',symbol2='2',system=1):
		int1=fromSymbol(symbol1);
		int2=fromSymbol(symbol2);
		result=toSymbol((int1*int2)%system);
		to_next=toSymbol((int1*int2)//system);
		print();
		print('множення двох цифр в '+str(system)+'-ій системі числення: '+symbol1+'*'+symbol2+'='+to_next+result);
		print();
		return result,to_next
	def make_number_string_for_multiply(integer_string='0',fractional_string='0'):
		if fractional_string!='':
			number_string=integer_string+'.'+fractional_string;
		else:
			number_string=integer_string;
		return number_string;
	return_number=Number('0');
	for system_string in number1.dictionary:
		if (system_string in number2.dictionary):
			number1_fractional_string,number2_fractional_string=cut_fractional_zeros(number1.fractional.dictionary[system_string]),cut_fractional_zeros(number2.fractional.dictionary[system_string]);
			numbers_after_dot=len(number1_fractional_string)+len(number2_fractional_string);
			result=multiplyStrings(make_number_string_for_multiply(number1.integer.dictionary[system_string],number1_fractional_string),make_number_string_for_multiply(number2.integer.dictionary[system_string],number2_fractional_string),number2,numbers_after_dot,int(system_string));
			return_number.add_number_in_system(result.dictionary[system_string],system_string);
	return return_number;

def compare(number1_string='12.3',number2_string='18.5'):
	def to_normal_size_integer(number1_string='',number2_string=''):
		def work_with_biggerString(stringBigger='',stringSmaller=''):
			for index in range(len(stringBigger)-len(stringSmaller)):
				stringSmaller='0'+stringSmaller;
			return stringBigger,stringSmaller
		if len(number1_string)>len(number2_string):
			number1_string,number2_string=work_with_biggerString(number1_string,number2_string);
		elif len(number1_string)<len(number2_string):
			number2_string,number1_string=work_with_biggerString(number2_string,number1_string);
		return number1_string,number2_string

	def to_normal_size_fractional(number1_string='',number2_string=''):
		def work_with_biggerString(stringBigger='',stringSmaller=''):
			for index in range(len(stringBigger)-len(stringSmaller)):
				stringSmaller=stringSmaller+'0';
			return stringBigger,stringSmaller
		if len(number1_string)>len(number2_string):
			number1_string,number2_string=work_with_biggerString(number1_string,number2_string);
		elif len(number1_string)<len(number2_string):
			number2_string,number1_string=work_with_biggerString(number2_string,number1_string);
		return number1_string,number2_string
	number1_array=number1_string.split('.');
	number2_array=number2_string.split('.');
	number1_array[0]=cut_integer_zeros(number1_array[0]);
	number1_array[1]=cut_fractional_zeros(number1_array[1]);
	number2_array[0]=cut_integer_zeros(number2_array[0]);
	number2_array[1]=cut_fractional_zeros(number2_array[1]);
	number1_array[0],number2_array[0]=to_normal_size_integer(number1_array[0],number2_array[0]);
	number1_array[1],number2_array[1]=to_normal_size_fractional(number1_array[1],number2_array[1]);
	if number1_array[0]>number2_array[0]:
		return '>'
	elif number1_array[0]<number2_array[0]:
		return '<'
	elif number1_array[1]>number2_array[1]:
		return '>';
	elif number1_array[1]<number2_array[1]:
		return '<';
	else:
		return '='
		
	
def create_number_from_string(number_string='12.12',system=3):
	number_array=number_string.split('.');
	if len(number_array)<2:
		number_array.append('0');
	k=len(number_array[0]);
	number_to_minus_10=0;
	for i in range(k):
		number_to_minus_10+=fromSymbol(number_array[0][i])*(system**(k-1-i));
	k=len(number_array[1]);
	for i in range(k):
		number_to_minus_10+=fromSymbol(number_array[1][i])*(system**(-i-1));
	number_to_Minus=Number(str('{:0.9f}'.format(number_to_minus_10)));
	number_to_Minus.add_number_in_system(number_string,system);
	return number_to_Minus
		

def divide_main(number1=None,number2=None,toSymbol=None,fromSymbol=None,Number=None,minus=None,plus=None,compare=None,cut_fractional_zeros=None,cut_integer_zeros=None,show=True,numbersAfterDot=10):
	def to_normal_size_integer(number1_string='',number2_string=''):
		def work_with_biggerString(stringBigger='',stringSmaller=''):
			for index in range(len(stringBigger)-len(stringSmaller)):
				stringSmaller='0'+stringSmaller;
			return stringBigger,stringSmaller
		if len(number1_string)>len(number2_string):
			number1_string,number2_string=work_with_biggerString(number1_string,number2_string);
		elif len(number1_string)<len(number2_string):
			number2_string,number1_string=work_with_biggerString(number2_string,number1_string);
		return number1_string,number2_string
	def create_integer_number_from_string(number_integer_string='1212',system=1):
		k=len(number_integer_string);
		number_to_minus_10=0;
		for i in range(k):
			number_to_minus_10+=fromSymbol(number_integer_string[i])*(system**(k-1-i));
		number_to_Minus=Number(str(number_to_minus_10));
		number_to_Minus.add_number_in_system(number_integer_string,system);
		return number_to_Minus
	def create_number_from_string(number_string='12.12',system=1):
		number_array=number_string.split('.');
		if len(number_array)<2:
			number_array.append('0');
		k=len(number_array[0]);
		number_to_minus_10=0;
		for i in range(k):
			number_to_minus_10+=fromSymbol(number_array[0][i])*(system**(k-1-i));
		k=len(number_array[1]);
		for i in range(k):
			number_to_minus_10+=fromSymbol(number_array[1][i])*(system**(-i-1));
		number_to_Minus=Number(str('{:0.9f}'.format(number_to_minus_10)));
		number_to_Minus.add_number_in_system(number_string,system);
		return number_to_Minus
	def minusFunctions(number1_to_Minus_integer_string='0',number1_to_Minus=None,number2_to_Minus=None,resultString='',number2_string='0',system_string='1',strings_to_show=[]):
		to_resultString=0;
		while compare(number1_to_Minus_integer_string+'.0',number2_string+'.0')!='<':
			number1_to_Minus=minus(number1_to_Minus,number2_to_Minus,toSymbol,fromSymbol,Number);
			number1_to_Minus_integer_string=cut_integer_zeros(number1_to_Minus.integer.dictionary[system_string]);
			to_resultString+=1;
		strings_to_show[len(strings_to_show)-1][1]=to_resultString;
		toSymbols_number=Number(str(to_resultString));
		toSymbols_number.to(int(system_string),False);
		
		
		resultString=resultString+toSymbols_number.integer.dictionary[system_string];
		return number1_to_Minus,number1_to_Minus_integer_string,resultString,strings_to_show
	resultNumber=Number('0');
	for system_string in number1.dictionary:
		if (system_string in number2.dictionary):
			if show:
				print('ДІЛЕННЯ в системі числення '+system_string+' : '+number1.dictionary[system_string]+'/'+number2.dictionary[system_string]);
				print("###########################################################");
				print("Дії підчас нього:");
				print();
			number1_integer_string=cut_integer_zeros(number1.integer.dictionary[system_string]);
			number2_integer_string=cut_integer_zeros(number2.integer.dictionary[system_string]);
			number1_fractional_string=cut_fractional_zeros(number1.fractional.dictionary[system_string]);
			number2_fractional_string=cut_fractional_zeros(number2.fractional.dictionary[system_string]);
			if len(number1_fractional_string)>len(number2_fractional_string):
				number2_fractional_string=number2_fractional_string+'0'*(len(number1_fractional_string)-len(number2_fractional_string));
			elif len(number2_fractional_string)>len(number1_fractional_string):
				number1_fractional_string=number1_fractional_string+'0'*(len(number2_fractional_string)-len(number1_fractional_string));
			number1_string=cut_integer_zeros(number1_integer_string+number1_fractional_string);
			number2_string=cut_integer_zeros(number2_integer_string+number2_fractional_string);
			resultString='';
			
			strings_to_show=[];
			lenString=len(number2_string);
			with_dot=False;
			after_dot=0;
			addZero=False;
			wasSmallerNumber=False;
			zeros='';
			
			number1_to_Minus=create_integer_number_from_string(number1_string[0:lenString],int(system_string));
			number1_to_Minus_integer_string=cut_integer_zeros(number1_to_Minus.integer.dictionary[system_string]);
			number2_to_Minus=create_integer_number_from_string(number2_string,int(system_string));
			while (after_dot<numbersAfterDot):
				if compare(number1_to_Minus_integer_string+'.0',number2_string+'.0')!='<':
					if with_dot:
						after_dot+=1;
					print(number1_to_Minus_integer_string);
					strings_to_show.append([zeros[0:len(zeros)//2]+number1_to_Minus_integer_string,'','']);
					number1_to_Minus,number1_to_Minus_integer_string,resultString,strings_to_show=minusFunctions(number1_to_Minus_integer_string,number1_to_Minus,number2_to_Minus,resultString,number2_string,system_string,strings_to_show);
					number1_to_Minus_integer_string=cut_integer_zeros(number1_to_Minus.integer.dictionary[system_string]);
					strings_to_show[len(strings_to_show)-1][2]=number1_to_Minus_integer_string;
					wasSmallerNumber=False;
					zeros='';
				elif compare(number1_to_Minus_integer_string+'.0',number2_string+'.0')=='<':
					if wasSmallerNumber==True:  
						resultString+='0';
						if with_dot:
							after_dot+=1;
					if lenString<len(number1_string):
						lenString+=1;
						number1_to_Minus=create_integer_number_from_string(number1_to_Minus_integer_string+number1_string[lenString-1],int(system_string));
						number1_to_Minus_integer_string=cut_integer_zeros(number1_to_Minus.integer.dictionary[system_string]);
						wasSmallerNumber=True;
						zeros+='0';
					elif lenString>=len(number1_string):
						if with_dot==False:
							if (resultString==''):
								resultString+='0';
							with_dot=True;
							resultString+='.';
							wasSmallerNumber=False;
						else:
							number1_to_Minus=create_integer_number_from_string(number1_to_Minus_integer_string+'0',int(system_string));
							number1_to_Minus_integer_string=cut_integer_zeros(number1_to_Minus.integer.dictionary[system_string]);
							wasSmallerNumber=True;
			resultNumber_step=create_number_from_string(resultString,int(system_string));
			resultNumber.add_number_in_system(resultString,int(system_string));
			if show:
				print('Саме ділення: ')
				print(number1_string+'|'+number2_string);
				k=0;
				len_before=0;
				to_len_before=0;
				to_len_before1=0;
				to_resultString='';
				for array in strings_to_show:
					number_minus_string=array[0];
					count_number_minus=array[1];
					result_string=array[2];
					number_minus=create_integer_number_from_string(number2_string,int(system_string));
					number_minus_2=create_integer_number_from_string('0',int(system_string));
					for i in range(count_number_minus):
						number_minus_2=plus(number_minus_2,number_minus,toSymbol,fromSymbol,Number,False);
					number_minus_string_new=number_minus_2.integer.dictionary[system_string];
					number_minus_string_new,number_minus_string=to_normal_size_integer(number_minus_string_new,to_resultString+number_minus_string);
					if k==0:
						print('-'+' '*(len(number1_string)-1)+'----');
						st=' '*(len_before+len(number_minus_string)-len(number_minus_string_new))+number_minus_string_new;
						print(st+' '*(len(number1_string)-len(st))+'|'+resultString);
					else:
						print('-');
						print(' '*(len_before+len(number_minus_string)-len(number_minus_string_new))+number_minus_string_new);
					print(' '*len_before+'-'*(len(number_minus_string)));
					k+=1;
					if k<len(strings_to_show):
						if result_string.count('0')==len(result_string):
							print(' '*(len_before+len(number_minus_string)-len(result_string))+result_string+strings_to_show[k][0]);
							len_before+=len(number_minus_string)-len(result_string);
							to_resultString=result_string;
						else:
							print(' '*(len_before+len(number_minus_string)-len(result_string))+strings_to_show[k][0]);
							len_before+=len(number_minus_string)-len(result_string);
							to_resultString='';
					else:
						print(' '*(len_before+len(number_minus_string)-len(result_string))+result_string);
						print();
						resultNumber.integer.check(int(system_string),show);
						resultNumber.fractional.check(int(system_string),show);
						print("###########################################################");
						print();
	return resultNumber;

def plus_main(number1=None,number2=None,toSymbol=None,fromSymbol=None,Number=None,show=True):
	def to_normal_size_integer(number1_string='',number2_string=''):
		def work_with_biggerString(stringBigger='',stringSmaller=''):
			for index in range(len(stringBigger)-len(stringSmaller)):
				stringSmaller='0'+stringSmaller;
			return stringBigger,stringSmaller
		if len(number1_string)>len(number2_string):
			number1_string,number2_string=work_with_biggerString(number1_string,number2_string);
		elif len(number1_string)<len(number2_string):
			number2_string,number1_string=work_with_biggerString(number2_string,number1_string);
		return number1_string,number2_string
		
	def to_normal_size_fractional(number1_string='',number2_string=''):
		def work_with_biggerString(stringBigger='',stringSmaller=''):
			for index in range(len(stringBigger)-len(stringSmaller)):
				stringSmaller=stringSmaller+'0';
			return stringBigger,stringSmaller
		if len(number1_string)>len(number2_string):
			number1_string,number2_string=work_with_biggerString(number1_string,number2_string);
		elif len(number1_string)<len(number2_string):
			number2_string,number1_string=work_with_biggerString(number2_string,number1_string);
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
		if show:
			print('1 - переноситься розряд, 0 - не переноситься розряд: '+' , '.join(discharge_array));
		
		return result;
		
	resultNumber=Number('0');
	for system_string in number1.dictionary:
		if (system_string in number2.dictionary):
			integer_number1,integer_number2=to_normal_size_integer(number1.integer.dictionary[system_string],number2.integer.dictionary[system_string]);
			fractional_number1,fractional_number2=to_normal_size_fractional(number1.fractional.dictionary[system_string],number2.fractional.dictionary[system_string]);
			number1_string_full=integer_number1+'.'+fractional_number1;
			number2_string_full=integer_number2+'.'+fractional_number2;
			result=doAdd(number1_string_full,number2_string_full,int(system_string),toSymbol,fromSymbol);
			if len(result)>len(number1_string_full):
				for index in range(len(result)-len(number1_string_full)):
					number1_string_full=' '+number1_string_full;
					number2_string_full=' '+number2_string_full;
			if show:
				print('Система числення: '+system_string)
				print(number1_string_full);
				print('+');
				print(number2_string_full);
			st='';
			for index in range(len(result)):
				st+='-';
			if show:
				print(st);
				print(result);
				print();
			resultNumber.add_number_in_system(result,int(system_string));
			resultNumber.integer.check(int(system_string),show);
			resultNumber.fractional.check(int(system_string),show);
			if show:
				print();
				print();
			
	return resultNumber;
	
def minus_main(number1=None,number2=None,toSymbol=None,fromSymbol=None,Number=None,show=True):
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
		if show:
			print('1 - переноситься розряд, 0 - не переноситься розряд: '+' , '.join(discharge_array));
		
		return result;
		
	resultNumber=Number('0');
	for system_string in number1.dictionary:
		if (system_string in number2.dictionary):
			integer_number1,integer_number2=to_normal_size_integer(number1.integer.dictionary[system_string],number2.integer.dictionary[system_string]);
			fractional_number1,fractional_number2=to_normal_size_fractional(number1.fractional.dictionary[system_string],number2.fractional.dictionary[system_string]);
			number1_string_full=integer_number1+'.'+fractional_number1;
			number2_string_full=integer_number2+'.'+fractional_number2;
			result=doMinus(number1_string_full,number2_string_full,int(system_string),toSymbol,fromSymbol);
			resultNumber.add_number_in_system(result,int(system_string));
			if len(number1_string_full)>len(result):
				for index in range(len(number1_string_full)-len(result)):
					result=' '+result;
					result=' '+result;
			if show:
				print('Система числення: '+system_string)
				print(number1_string_full);
				print('-');
				print(number2_string_full);
			st='';
			for index in range(len(result)):
				st+='-';
			if show:
				print(st);
				print(result);
				print();
			resultNumber.integer.check(int(system_string),show);
			resultNumber.fractional.check(int(system_string),show);
			if show:
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
		
	def to(self,system=1,  show=True):
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
			if show:
				print(toAdd+str(number)+':'+str(system)+'|'+symbol);
			number=number//system;
		if len(result)==0:
			result='0';
		self.dictionary[str(system)]=result;
		if show:
			print('=> '+result+'\n');
		return result
	
	def check(self,system=1, show=True):
		number=self.dictionary[str(system)];
		index=len(number)-1;
		result=0;
		st='';
		for sym in number:
			result+=self.fromSymbol(sym)*(system**index);
			st+=str(self.fromSymbol(sym))+'*('+str(system)+'^'+str(index)+')'
			if index!=0:
				st+='+';
			else:
				st+='=';
			index-=1;
		st+=str(result);
		if show:
			print('Перевірка цілої частини:  '+st);
		
		
class Fractional:
	def __init__(self,number=0):
		self.dictionary={
			'10':str(number)
		}
		self.toSymbol=toSymbol;
		self.fromSymbol=fromSymbol;
		
	def to(self,system=1, show=True,numbersAfterDot=10):
		result='';
		number=int(self.dictionary['10']);
		max_number_len=len(str(number));
		for j in range(numbersAfterDot):
			value=(10**max_number_len)
			integ=number*system//value;
			symbol=self.toSymbol(integ)
			result=result+symbol;
			number_len=len(str(number));
			toAdd='';
			for i in range(max_number_len-number_len):
				toAdd+=' ';
			if show:
				print(toAdd+'0.'+str(number)+'*'+str(system)+'|'+symbol);
			number=(number*system)%value;
		self.dictionary[str(system)]=result;
		if show:
			print('=> '+result+'\n');
		return result
		
	def check(self,system=1, show=True):
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
		if show:
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
	def to(self,system=0, show=True):
		
		if show:
			print(str(self.array[0])+'.'+str(self.array[1])+'       з 10-ої до '+str(system)+'-ої'+'\n');
		
		integer=self.integer.to(system);
		fractional=self.fractional.to(system);
		
		if show:
			print('Результат: '+integer+'.'+fractional+' ;');
		self.integer.check(system);
		self.fractional.check(system);
		if show:
			print();
			print('----------------------------');
			print();
		
		self.dictionary[str(system)]=self.integer.dictionary[str(system)]+'.'+self.fractional.dictionary[str(system)];
		
	def add_number_in_system(self,numberString='',system=1):
		self.dictionary[str(system)]=numberString;
		numberString_array=numberString.split('.');
		if len(numberString_array)<2:
			numberString_array.append('0');
		self.integer.dictionary[str(system)]=numberString_array[0];
		self.fractional.dictionary[str(system)]=numberString_array[1];
		
		
		
def plus(number1=None,number2=None,show=True):
	stEr='FUNCTION PLUS : ';
	if type(number1)!=Number:
		 raise Exception(stEr+'number1 can not be '+str(type(number1)));
	elif type(number2)!=Number:
		 raise Exception(stEr+'number2 can not be '+str(type(number1)));
	elif (show!=True)and(show!=False):
		raise Exception(stEr+'show can be only True/False');
	else:
		return plus_main(number1,number2,toSymbol,fromSymbol,Number,show);
		
def minus(number1=None,number2=None,show=True):
	stEr='FUNCTION MINUS : ';
	if type(number1)!=Number:
		 raise Exception(stEr+'number1 can not be '+str(type(number1)));
	elif type(number2)!=Number:
		 raise Exception(stEr+'number2 can not be '+str(type(number1)));
	elif (show!=True)and(show!=False):
		raise Exception(stEr+'show can be only True/False');
	else:
		return minus_main(number1,number2,toSymbol,fromSymbol,Number,show);
def multiply(number1=None,number2=None,show=True):
	stEr='FUNCTION MULTIPLY : ';
	if type(number1)!=Number:
		 raise Exception(stEr+'number1 can not be '+str(type(number1)));
	elif type(number2)!=Number:
		 raise Exception(stEr+'number2 can not be '+str(type(number1)));
	elif (show!=True)and(show!=False):
		raise Exception(stEr+'show can be only True/False');
	else:
		return multiply_main(number1,number2,toSymbol,fromSymbol,Number,plus_main,cut_fractional_zeros,show);
def divide(number1=None,number2=None,numbersAfterDot=10,show=True):
	stEr='FUNCTION DIVIDE : ';
	if type(number1)!=Number:
		 raise Exception(stEr+'number1 can not be '+str(type(number1)));
	elif type(number2)!=Number:
		 raise Exception(stEr+'number2 can not be '+str(type(number1)));
	elif (show!=True)and(show!=False):
		raise Exception(stEr+'show can be only True/False');
	elif type(numbersAfterDot)!=type(1):
		raise Exception(stEr+'show can be only integers');
	else:
		return divide_main(number1,number2,toSymbol,fromSymbol,Number,minus_main,plus_main,compare,cut_fractional_zeros,cut_integer_zeros,show,numbersAfterDot);
