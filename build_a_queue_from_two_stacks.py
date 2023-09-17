import sys


class Queue:
    def __init__(self):
        self.stack_left = []
        self.stack_right = []
        
    def enqueue(self, x:int):
        self.stack_left.append(x)
    
    def dequeue(self) -> int:
        if len(self.stack_right):
            value = self.stack_right[-1] 
            del self.stack_right[-1]
            return value
        
        value = 0
        while len(self.stack_left):
            value = self.stack_left[-1] 
            del self.stack_left[-1]
            self.stack_right.append(value) 
            
        del self.stack_right[-1]
        return value
    
    def print_front(self) -> int:
        if len(self.stack_right):
            sys.stdout.write(str(self.stack_right[-1]) + "\n")
            return
        
        value = 0
        while len(self.stack_left):
            value = self.stack_left[-1] 
            del self.stack_left[-1]
            self.stack_right.append(value)
        sys.stdout.write(str(value) + "\n")
        
        
def main():
    queue = Queue()
    q = int(sys.stdin.readline().rstrip())
    
    for _ in range(q):
        input_ = list(sys.stdin.readline().rstrip().split())
        if len(input_) == 2:
            _, value = input_
            queue.enqueue(int(value))
            continue
        
        operation = input_[-1]
        if operation == "2":
            queue.dequeue()
            continue
            
        queue.print_front()
        
        
if __name__ == "__main__":
    main()

