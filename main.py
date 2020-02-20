class Pizza:
    def __init__(self, m, n):
        self.max_slices = m
        self.pizzas = n
        self.slices = []

    def orderPizza(self):
        # calculate the maximum number of pizzas to order
        output = [3, [1, 3, 4]]
        return output

"""
    Prepare Input/Output
"""
def readInput(file):
    lines = [line.rstrip('\n') for line in open(file)]
    # extract the number of pizzas and the max number of slices
    numbers = lines[0].split(" ")
    pizza = Pizza(numbers[0], numbers[1])
    # prepare the number of slices per pizza
    pizza.slices = [ int(num) for num in lines[1].split(" ")]
    return pizza

def writeOutput(filename, output):
    outF = open(filename, 'w+')
    # write the number of pizzas to order
    outF.write(str(output[0]) + '\n')
    # write the types of pizzas
    for line in output[1]:
        outF.write(str(line) + ' ')
    outF.write('\n')


if __name__ == "__main__" :
    file_names= ['a_example.in',"b_small.in", 'c_medium.in', 'd_quite_big.in', 'e_also_big.in' ]
    for file in file_names:
        pizza = readInput("Input_Files/"+file)
        print(pizza.max_slices, pizza.pizzas, pizza.slices)
        output = pizza.orderPizza()
        file = 'Output_Files/sortie_' + file
        writeOutput(file, output)