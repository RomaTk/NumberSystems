import numberSystems

####################################################################################
"""
	Example of using numberSystems library
	
	Problems:
		1. THIS LIBRARY CAN WORK ONLY WITH NUMBERS WHICH ARE GREATER THAN ZERO AND ZERO
		2.IT DOES NOT CHECK ALL PARAMETRS
	
	The copied text of result is in example 27.txt
	
"""
ch1=numberSystems.Number('891.334');
ch1.to(2);
ch1.to(8);
ch1.to(16);

ch2=numberSystems.Number('567.88');
ch2.to(2);
ch2.to(8);
ch2.to(16);

ch3=numberSystems.Number('277.881');
ch3.to(2,10);
ch3.to(8,10);
ch3.to(16);

ch4=numberSystems.Number('8.4');
ch4.to(2,10);
ch4.to(8,10);
ch4.to(16,10);

ch5=numberSystems.Number('4.23');
ch5.to(2,10);
ch5.to(8,10);
ch5.to(16,10);

ch2=numberSystems.plus(ch1,ch2,True);
ch3=numberSystems.minus(ch2,ch3,True);
ch4=numberSystems.multiply(ch3,ch4,True);
ch5=numberSystems.divide(ch4,ch5,10,True);
ch1=numberSystems.create_number_from_string('12.11',10);
