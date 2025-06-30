import re

class StringCalculator:
    def __init__(self):
        self.delimiters = [",", "\n"]

    def _extract_numbers(self, numbers: str):
        delimiters = self.delimiters
        custom_delimiter_match = re.match(r'^//(\[.*\]|.)\n', numbers)

        if custom_delimiter_match:
            delimiter_def = custom_delimiter_match.group(1)
            numbers = numbers[custom_delimiter_match.end():]
            if delimiter_def.startswith("[") and delimiter_def.endswith("]"):
                delimiter_def = delimiter_def[1:-1]
            delimiters = [re.escape(delimiter_def)]

        pattern = '|'.join(delimiters)
        num_list = re.split(pattern, numbers)

        parsed_numbers = []
        negatives = []
        for num in num_list:
            if num.strip() == '':
                continue
            n = int(num)
            if n < 0:
                negatives.append(n)
            parsed_numbers.append(n)

        if negatives:
            raise ValueError(f"negative numbers not allowed {','.join(map(str, negatives))}")

        return parsed_numbers

    def add(self, numbers: str) -> int:
        nums = self._extract_numbers(numbers)
        return sum(nums)

    def subtract(self, numbers: str) -> int:
        nums = self._extract_numbers(numbers)
        return nums[0] - sum(nums[1:]) if nums else 0

    def multiply(self, numbers: str) -> int:
        nums = self._extract_numbers(numbers)
        result = 1
        for n in nums:
            result *= n
        return result if nums else 0

    def divide(self, numbers: str) -> float:
        nums = self._extract_numbers(numbers)
        if not nums:
            return 0
        result = nums[0]
        for n in nums[1:]:
            if n == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result /= n
        return result

if __name__ == "__main__":
    calc = StringCalculator()
    try:
        print("Choose operation: add / subtract / multiply / divide")
        operation = input("Enter operation: ").strip().lower()
        user_input = input("Enter numbers (comma or //delimiter\n): ").strip()

        if operation == "add":
            print("Result:", calc.add(user_input))
        elif operation == "subtract":
            print("Result:", calc.subtract(user_input))
        elif operation == "multiply":
            print("Result:", calc.multiply(user_input))
        elif operation == "divide":
            print("Result:", calc.divide(user_input))
        else:
            print("Unsupported operation.")
    except Exception as e:
        print("Error:", e)
