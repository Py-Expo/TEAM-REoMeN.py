from PIL import Image

def convert_to_3d(image_path, height_factor=10):
    # Load the 2D image
    img = Image.open("C:\\Users\\harik\\OneDrive\\Desktop\\pyexpo check 3\\bat logo.jpg")
    img = img.convert('L')  # Convert to grayscale

    # Get pixel values as a 2D array
    pixel_values = list(img.getdata())
    width, height = img.size

    # Create a height map from pixel values
    height_map = [[pixel_values[i * width + j] for j in range(width)] for i in range(height)]

    # Extrude the height map to create a 3D model
    vertices = []
    faces = []

    for i in range(height):
        for j in range(width):
            vertices.append((j, i, height_map[i][j] * height_factor))

    for i in range(height - 1):
        for j in range(width - 1):
            # Define faces using vertex indices
            faces.append((i * width + j, i * width + j + 1, (i + 1) * width + j + 1, (i + 1) * width + j))

    return vertices, faces

def save_obj_file(vertices, faces, output_path='model.obj'):
    with open(output_path, 'w') as f:
        for vertex in vertices:
            f.write(f"v {vertex[0]} {vertex[1]} {vertex[2]}\n")

        for face in faces:
            f.write(f"f {face[0] + 1} {face[1] + 1} {face[2] + 1} {face[3] + 1}\n")

if __name__ == "__main__":
    image_path ="C:\\Users\\harik\\OneDrive\\Desktop\\pyexpo check 3\\bat logo.jpg"
    vertices, faces = convert_to_3d(image_path)
    save_obj_file(vertices, faces, output_path='model1.obj')
    
def export_texture(model_path, output_path):
    # Open the 2D model image
    model_image = Image.open(model_path)

    # Save the model image as a texture file
    model_image.save(output_path)