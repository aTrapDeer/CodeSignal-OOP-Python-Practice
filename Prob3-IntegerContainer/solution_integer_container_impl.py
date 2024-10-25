from integer_container import IntegerContainer


class IntegerContainerImpl(IntegerContainer):

    def __init__(self):
        # TODO: implement
        self.container = []
        pass

    # TODO: implement interface methods here
    def add(self, value: int) -> int:
        self.container.append(value)
        return len(self.container)
    def delete(self, value: int) -> bool:
        # need to check within the container for the value
        if value in self.container:
            self.container.remove(value)
            return True
        return False
        
    def get_median(self)-> int | None:
        num_elements = len(self.container)
        if (num_elements % 2 == 0):
            if (num_elements /2 == 0):
                return None
        
        sorted_container = sorted(self.container)

        if (num_elements % 2 == 1):
            half_val = int(num_elements/2)
            return sorted_container[half_val]
        else:
            half_val = int(num_elements/2)
            return sorted_container[half_val -1]

            