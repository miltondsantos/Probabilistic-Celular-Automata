import numpy
import time
import matplotlib.pyplot as plt


#rulein = 30

rulein = input('Regra do CA sem Ruido:')

output_pattern = [int(x) for x in numpy.binary_repr(rulein, width=8)]
output_pattern

input_pattern = numpy.zeros([8, 3])
for i in range(8):
    input_pattern[i, :] = [int(x) for x in numpy.binary_repr(7-i, width=3)]

input_pattern

columns = 501
rows = int(columns/2)+1

canvas = numpy.zeros([rows, columns+2])
canvas[0, int(columns/2)+1] = 1

for i in numpy.arange(0, rows-1):
    for j in numpy.arange(0, columns):
        for k in range(8):
            if numpy.array_equal(input_pattern[k, :], canvas[i, j:j+3]):
                canvas[i+1, j+1] = output_pattern[k]

plt.imshow(canvas[:, 1:columns+1], cmap='Greys', interpolation='nearest')
plt.title("Regra do CA sem Ruido {}".format(rulein))
plt.show()
start_time1 = time.time()
print("Tempo de execucao da Regra sem ruido = %s seconds" % (time.time() - start_time1))


bin(numpy.uint8(rulein))

comruido = bin(~numpy.uint8(rulein))

int(comruido,2)

ruleout = int(comruido,2)
print 'Regra do CA com Ruido:', ruleout

output_pattern = [int(x) for x in numpy.binary_repr(ruleout, width=8)]

output_pattern

input_pattern = numpy.zeros([8, 3])
for i in range(8):
    input_pattern[i, :] = [int(x) for x in numpy.binary_repr(7-i, width=3)]

input_pattern

columns = 501
rows = int(columns/2)+1

canvas = numpy.zeros([rows, columns+2])
canvas[0, int(columns/2)+1] = 1

for i in numpy.arange(0, rows-1):
    for j in numpy.arange(0, columns):
        for k in range(8):
            if numpy.array_equal(input_pattern[k, :], canvas[i, j:j+3]):
                canvas[i+1, j+1] = output_pattern[k]

plt.imshow(canvas[:, 1:columns+1], cmap='Greys', interpolation='nearest')
plt.title("Regra do CA com Ruido {}".format(ruleout))
plt.show()
start_time2 = time.time()
print("Tempo de execucao da Regra apos o ruido = %s seconds" % (time.time() - start_time2))
print
print ("Diferenca de tempo de execucao da Regra  =", start_time2 - start_time1)