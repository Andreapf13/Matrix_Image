import numpy
numpy.random.randint
import PIL

def calculate_element_destination_matrix(i,j,origin_matrix):
    value = origin_matrix[i][j]
    average = value
    count = 1 
    if i != 0:
        i_above = i - 1 
        j_above = j
        value_above = origin_matrix[i_above][j_above]
        average = average + value_above
        count = count + 1 
    if i != (len(origin_matrix) - 1 ):
        i_below =  i + 1 
        j_below = j
        value_below =  origin_matrix[i_below][j_below]
        average = average + value_below 
        count = count + 1 
    if j != 0:
        i_left = i
        j_left =  j - 1
        value_left =  origin_matrix[i_left][j_left]
        average = average + value_left
        count = count + 1 
    if j != len(origin_matrix[i]) - 1:
        i_right = i 
        j_right = j + 1 
        value_right = origin_matrix[i_right][j_right]
        average = average + value_right
        count = count + 1 
    return round((average / count),2)

def process_matrix(origin_matrix):
    destination_matrix = []
    for  i in range(len(origin_matrix)):
        i_destination = []
        for j in range(len(origin_matrix[i])):
            element_destination =  calculate_element_destination_matrix (i,j,origin_matrix)
            i_destination.append(element_destination)
        destination_matrix.append(i_destination)
    return destination_matrix


long_save = int(input("Tell me how long you want the original matrix to be "))
wide_save = int(input("Tell me how wide you want the original matrix to be "))

origin_matrix = numpy.random.randint(0,10,(long_save,wide_save)) #This allows us to create random numbers from 0 to 10.
print(origin_matrix)

def matrix_representation(origin_matrix):
    a = ""
    for long in range(len(origin_matrix)):
        for wide in range(len(origin_matrix[-1])):
            a += str(origin_matrix[long][wide]) + "\t" 
        a += "\n"
    print("THIS IS ORIGIN MATRIX:" "\n" "\n" + a)
    process_matrix_representation = process_matrix(origin_matrix)
    b = ""
    for long in range(len(process_matrix_representation)):
        for wide in range(len(process_matrix_representation[-1])):
            b+= str(process_matrix_representation[long][wide]) + "\t" 
        b += "\n"   
    print("THIS IS DESTINATION MATRIX:" "\n" "\n"+ b)
matrix_representation(origin_matrix)
from re import L
from PIL import Image
print('Pillow Version:', PIL.__version__)         # Load and show an image with Pillow
image = Image.open('IMG_9033.JPG').convert("L")   # Open the image form working directory
print(image.format)                               # Summarize some details about the image
print(image.size)                                 # Summarize some details about the image
print(image.mode)
image.show()                                      # Summarize some details about the image
data = numpy.asarray(image).tolist()              # Convert image to numpy array and get black and white to reduce each pixel to a number 
print(data)
processed_data = process_matrix(data)
processed_image = Image.fromarray(numpy.array(processed_data))
print("This is your picture processed! He is my dog , Baloo. Wish you enjoy that practice. Thanks for visit")