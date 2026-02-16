#!/bin/bash                    # Shebang
VAR="value"                   # Variable
echo "Hello $VAR"             # Print with variable
read -p "Enter: " input       # Read input
if [ $VAR -eq 5 ]; then       # Conditional
  echo "Five"
fi
for i in {1..5}; do           # Loop
  echo $i
done
while true; do                # While loop
  sleep 1
done
function myFunc() {           # Function
  echo "Hello"
}
myFunc                        # Call function