program SimpleCalculator;

uses crt;

var
  num1, num2, result: real;
  operation: char;

begin
  clrscr; { Clears the screen }
  writeln('Simple Calculator');
  writeln('-----------------');
  writeln;
  
  write('Enter the first number: ');
  readln(num1);
  
  write('Enter the operation (+, -, *, /): ');
  readln(operation);
  
  write('Enter the second number: ');
  readln(num2);
  
  case operation of
    '+': result := num1 + num2;
    '-': result := num1 - num2;
    '*': result := num1 * num2;
    '/': 
      if num2 <> 0 then
        result := num1 / num2
      else
      begin
        writeln('Error: Division by zero!');
        halt;
      end;
  else
    begin
      writeln('Invalid operation!');
      halt;
    end;
  end;
  
  writeln;
  writeln('Result: ', result:0:2); { Displays the result with 2 decimal places }
  writeln;
  writeln('Press any key to exit...');
  readkey;
end.
