import os
import shutil
import time

def create_temp_directory():
    # Crear un directorio temporal en el directorio actual
    temp_dir = "temp_directory"
    os.makedirs(temp_dir, exist_ok=True)
    print(f"Directorio temporal creado: {temp_dir}")
    return temp_dir

def create_files(temp_dir, num_files=5):
    # Crear archivos en el directorio temporal
    for i in range(1, num_files + 1):
        file_path = os.path.join(temp_dir, f"archivo_{i}.txt")
        with open(file_path, "w") as file:
            file.write(f"Este es el contenido del archivo {i}")
        print(f"Archivo creado: {file_path}")

def list_files(temp_dir):
    # Listar archivos en el directorio temporal
    print(f"\nArchivos en {temp_dir}:")
    for file_name in os.listdir(temp_dir):
        print(file_name)

def clean_up(temp_dir):
    # Eliminar el directorio temporal y sus contenidos
    shutil.rmtree(temp_dir)
    print(f"\nDirectorio {temp_dir} eliminado.")

def main():
    # Crear directorio temporal
    temp_dir = create_temp_directory()

    # Crear archivos dentro del directorio
    create_files(temp_dir)

    # Listar los archivos creados
    list_files(temp_dir)

    # Esperar un momento antes de limpiar
    time.sleep(2)

    # Eliminar los archivos y el directorio temporal
    clean_up(temp_dir)

if __name__ == "__main__":
    main()
