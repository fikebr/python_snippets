import os
import subprocess

def upscale_image(file_name_full, scale=2):
    exe = "E:\\Programs\\Mmed\\_Image\\RealEsrgan-ncnn-vulkan\\realesrgan-ncnn-vulkan.exe"


    if os.path.exists(file_name_full):
        print(f"UPSCALING: {file_name_full}")
        (name, ext) = os.path.splitext(os.path.basename(file_name_full))
        dir = os.path.dirname(file_name_full)

        new_file = f"{name}_up{scale}{ext}"
        new_file = os.path.join(dir, new_file)

        opt = f'-i "{file_name_full}" -o "{new_file}" -s {scale}'

        # subprocess.Popen(f"{exe} {opt}")
        output = subprocess.run(
            f"{exe} {opt}",
            shell=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
