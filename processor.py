import argparse
import operator


class StatsObject:
    LIMIT = 1000

    def __init__(self, captured_elements: list) -> None:
        self.stats_items = captured_elements

    def between(self, input_range: list) -> int:
        result = 0
        for item in self.stats_items:
            if input_range[0] <= item <= input_range[1]:
                result += 1
        return result

    def greater(self, number: int) -> int:
        return self._gt_lt_dispatcher('greater', number)

    def less(self, number: int) -> int:
        return self._gt_lt_dispatcher('less', number)
    
    def _gt_lt_dispatcher(self, input_op: str, number: int) -> int:
        operator_dispatcher = lambda input_op: operator.gt if input_op == 'greater' else operator.lt
        selected_operator = operator_dispatcher(input_op)
        
        result = 0

        for counter in range(self.LIMIT): 
            try:
                if selected_operator(self.stats_items[counter], number):
                    result += 1
            except IndexError:
                break
        return result


class DataCapture:
    captured_elements = []

    def add(self, number: int) -> None:
        self.captured_elements.append(number)
    
    def build_stats(self) -> StatsObject:
        return StatsObject(self.captured_elements)


if __name__ == "__main__":
    CLI = argparse.ArgumentParser()
    CLI.add_argument(
        "--collection",  
        nargs="*", 
        type=int,
        default=[3, 9, 3, 4, 6],  #Default values are excercise examples
    )

    args = CLI.parse_args()
   
    main_collection = DataCapture()

    [main_collection.add(item) for item in args.collection]

    operation = input("Write the operation that you want to execute over your collection: ")
    value = input("Write the value you want to compute (or 2 comma separated values for 'between' operation): ")
    
    if ',' in value:
        value = [int(value) for value in value.split(',')]
    else:
        value = int(value)
    
    stats = main_collection.build_stats()

    operation_dispatcher = {
        'greater': stats.greater,
        'less': stats.less,
        'between': stats.between
    }

    result = operation_dispatcher[operation](value)

    print(f"Data collection: {args.collection}")
    print(f"Operation selected: {operation}")
    print(f"Value to compute: {value}")
    print(f"Result: {result}")