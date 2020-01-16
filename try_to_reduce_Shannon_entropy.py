print("\n\n\nСтарт программы...")

# Эта функция подсчитает количества комбинаций '0' и '1',
# а также количества комбинаций '00', '01', '10', '11' в двоичной строке,
# и вернёт эти количества в виде массива с двумя объектами.
def count_null_ones(binary_string):	#binary_string: "011010010...0010010..."

	#	Подcчитаем количества комбинаций '0', '1':
	nulls	=	0;
	ones 	=	0;	
	if(len(binary_string)%2 == 1): binary_string = '0'+binary_string;
	for i in range(0, len(binary_string)):
		if(binary_string[i]=='1'):
			ones	+=	1;
		elif(binary_string[i]=='0'):
			nulls	+=	1;

	#	Подсчитаем количества комбинаций '00', '01', '10', '11':
	null_null	=	0;
	null_one	=	0;
	one_null	=	0;
	one_one		=	0;
	for i in range(0, len(binary_string), 2):
		if		(	binary_string[i] == '0'	and	binary_string[i+1] == '0'	):
			null_null	+=	1;
		elif	(	binary_string[i] == '0'	and	binary_string[i+1] == '1'	):
			null_one	+=	1;
		elif	(	binary_string[i] == '1'	and	binary_string[i+1] == '0'	):
			one_null	+=	1;
		elif	(	binary_string[i] == '1'	and	binary_string[i+1] == '1'	):
			one_one		+=	1;
	return [	#	Вернуть массив с объектами.
				{
					'0': nulls,
					'1': ones
				},
				{
					'00': null_null,
					'01': null_one,
					'10': one_null,
					'11': one_one
				}
	];
#Конец функции

# 	Эта функция перепишет двоичную строку в виде другой строки,
#	биты которой означают изменение или не изменение предыдущего бита изначальной строки.
#	Стартовый бит - '0'
#	01011010	-> 01110101.
#	Обратная операция - обратнейшим образом обратна, и реализуется обратимо - на принципах обратности,
#	но быстрее это делать - используя свойство её обратнизациоаналистичности.
def need_change_bit(bin_x):
	#print("ones in bin_x: ", count_null_ones(bin_x)[0]['1']);
	start_bit = '0';
	need_change = "";
	for i in range(0, len(bin_x)):
		if(bin_x[i] == start_bit):
			need_change += '0';
		else:
			need_change += '1';
			if(start_bit == '0'):
				start_bit = '1';
			else:
				start_bit = '0';
	print("need_change", need_change, ": ", "единиц: ", count_null_ones(need_change)[0]['1'], "бит: ", len(need_change));
	return need_change;

#	Эта функция - экспоненциально ускоряет обратимизициональность супрасверхпрограммного гиперпреобразования.
def return_bits(need_change):
	start_bit = '0';
	bin_x = "";
	for i in range(0, len(need_change)):
		if(need_change[i] == '1'):
			if(start_bit == '0'):
				start_bit = '1';
			else:
				start_bit = '0';
		bin_x += start_bit;
	print("bin_x: ", bin_x, ": ", "единиц: ", count_null_ones(bin_x)[0]['1'], "бит: ", len(bin_x), count_null_ones(bin_x)[0]['1']/len(bin_x), "%");	
	return bin_x;

print("\n\nГенерируем хуету:");
import random;


def gen_rand_byte():
	return bin(random.randrange(0, 256))[2::].zfill(8);
	
def gen_bytes(n):
	bytestring = "";
	for i in range(0, n):
		bytestring += gen_rand_byte();
	return bytestring;



#string1 = bin(random.randrange(0, 10000000000000000000000000000))[2::];
string1 = gen_bytes(4);
#string1 = '00000000'+gen_bytes(3);	#нули - спереди

#Бамп - единицами:
#string1 = '11111111111111111111111111111111111111111';

print("str1,  ", string1, ": ", "единиц: ", count_null_ones(string1)[0]['1'], "бит: ", len(string1));


print("\nПреобразуем в хуергу:");
ones_in_result = need_change_bit(string1);

print("\nВосстанавливаем драгоценную хуету:");
res = return_bits(ones_in_result);

if(res == string1):
	print("\nЗаебись: ", (res == string1) );
else:
	print("\nЧё-т, бля, хуёво: ", (res == string1));

	
print("\nЗациклим поебнятину:");

ones_in_result = need_change_bit(string1);

for i in range(0, 1000):
	if(ones_in_result == string1):
		print("i =", i, "True");
		break;
	ones_in_result = need_change_bit(ones_in_result);

'''
#А что, будет если зациклить наоборот?
for i in range(0, 250):
	res = return_bits(res);
'''


"""
Последовательность преобразований зацикливается, выдавая ту же строку,
через (2^x - 1) шагов, где x - некое число.

Среди двоичных чисел могут быть
как числа с количеством единиц наименьшим, чем в исходной строке,
так и числа с количеством единиц - наибольшим.
Эти, можно подвергнуть негации, задавая один дополнительный бит.


Итак. Алгоритм.
1. Зациклить преобразования с подсчётом бит.
2. Выбрать число, содержащее наименьшее количество единиц, либо число, содержащее наибольшее количество единичных бит.
3. Записать его, и бит либо негации либо не негации. Записать индекс, для восстановления исходных данных.
4. Подвергнуть это всё преобразованию Барроуза-Уилера.
5. Сжать.

"""

print(
	"\n\nОтодвинься назад и поводи глазами по таблице - ты увидишь некие треугольнички из нулей."
	,"\nТакая вот закономерность уменьшения нулей. Это - треугольнички Анонима, гиперкомплексные, трибоначчиевые."
	,"\nНачинаются они - с мест, где дохуя единиц."
	,"\nЗаканчиваются - одним нулём."
	,"\nЭто должно конкретно помочь сжать несжимаемое, и впихнуть его потом - вообще в невпихуемое."
);
