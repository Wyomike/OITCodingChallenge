import argparse

M: int = 1000
D: int = 500
C: int = 100
L: int = 50
X: int = 10
V: int = 5
I: int = 1

def roman_to_decimal(roman: str) -> int:
  total: int = 0
  i: int = 0
  do_last: bool = True
  while (i < len(roman) - 1):
    next: str = roman[i + 1]
    decimal_next: int = single_roman_to_decimal(next)
    decimal_roman: int = single_roman_to_decimal(roman[i])
    if (decimal_roman < decimal_next):
      total += decimal_next - decimal_roman
      i += 1
      do_last = False #Since this jumps, I need to know if this is the last operation
    else:
      total += decimal_roman
      do_last = True #do one more round if not doing a skip
    i += 1
  if (do_last):
    total += single_roman_to_decimal(roman[i])
  return total

def single_roman_to_decimal(roman: str) -> int: #converts a single roman numeral to decimal
  decimal = 0
  if (roman == "M"):
      decimal = M
  elif (roman == "D"):
    decimal = D
  elif (roman == "C"):
    decimal = C
  elif (roman == "L"):
    decimal = L
  elif (roman == "X"):
    decimal = X
  elif (roman == "V"):
    decimal = V
  elif (roman == "I"):
    decimal = I
  return decimal

def decimal_to_roman(decimal: int):
  roman: str = ""
  decimal_str = str(decimal)
  for i in range(len(decimal_str)):
    roman_multiplier: int = int(decimal_str[i]) #The front decimal value used to determine how many times you should repeat the operation
    if (roman_multiplier == 9): #I don't feel like this is a very elegant solution but I was worried about time. Since 4 and 9 are edge cases, handle the separately
      sub_roman: str = single_value_to_roman(1 * 10**(len(decimal_str) - i - 1))
      single_roman: str = single_value_to_roman(1 * 10**(len(decimal_str) - i))
      roman += sub_roman + single_roman
    elif (roman_multiplier == 4):
      sub_roman: str = single_value_to_roman(1 * 10**(len(decimal_str) - i - 1))
      single_roman: str = single_value_to_roman(5 * 10**(len(decimal_str) - i - 1))
      roman += sub_roman + single_roman
    else:
      if (roman_multiplier/5 >= 1):#handle if the front value can be represented with a 5 numeral
        roman_multiplier -= 5
        single_roman: str = single_value_to_roman(5 * 10**(len(decimal_str) - i - 1))
        roman += single_roman
      for j in range(roman_multiplier):
        single_roman: str = single_value_to_roman(1 * 10**(len(decimal_str) - i - 1))
        roman += single_roman
  return roman

def single_value_to_roman(val: int): # designed to take in only ints that can be represented as one roman numeral.
  roman = ""
  if (val == M):
    roman = "M"
  elif (val == D):
    roman = "D"
  elif (val == C):
    roman = "C"
  elif (val == L):
    roman = "L"
  elif (val == X):
    roman = "X"
  elif (val == V):
    roman = "V"
  elif (val == I):
    roman = "I"
  return roman

#just some test stuff.

def main(input_string: str, input_int):
  print(roman_to_decimal(input_string))
  print(decimal_to_roman(input_int))

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Roman Numeral Converter")
    parser.add_argument("-s","--string",type=str,required=True, help="Roman numeral to be converted, IN ALL CAPS")
    parser.add_argument("-d","--int",type=int,required=True, help="Single integer to be converted to roman numeral")
    args = parser.parse_args()
    main(args.string, args.int)
    