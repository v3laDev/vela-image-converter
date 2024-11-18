import os
import sys
from PIL import Image

def convert_image(input_file, output_format):
    try:
        # Convertir a ruta absoluta
        input_file = os.path.abspath(input_file)
        
        # Verificar si el archivo existe
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"File not found: {input_file}")

        # Obtener nombre base del archivo y definir ruta de salida
        project_folder = os.path.dirname(os.path.abspath(__file__))
        base_name = os.path.splitext(os.path.basename(input_file))[0]
        output_file = os.path.join(project_folder, f"{base_name}.{output_format.lower()}")

        # Abrir y guardar la imagen
        img = Image.open(input_file)
        img.save(output_file, output_format.upper())
        print(f"Image converted successfully and saved in the project folder: {output_file}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    if len(sys.argv) < 2:
        print("Please provide an image file.")
        return

    input_file = sys.argv[1]
    print("In what format do you want to convert the file?")
    print("1. PNG")
    print("2. JPG")
    print("3. WEBP")
    
    choice = input("> ")

    if choice == "1":
        convert_image(input_file, "PNG")
    elif choice == "2":
        convert_image(input_file, "JPG")
    elif choice == "3":
        convert_image(input_file, "WEBP")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
