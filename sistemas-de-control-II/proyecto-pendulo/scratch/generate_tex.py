import os
import re

def sort_key(filename):
    match = re.match(r'^(\d+)', filename)
    num = int(match.group(1)) if match else 999
    
    priority = 10
    if '-pos' in filename:
        priority = 1
    elif '-angulo' in filename:
        priority = 2
    elif '-sim' in filename:
        priority = 3
        
    return (num, priority, filename)

def generate_latex_section(dir_path, subdir_name, title):
    full_path = os.path.join(dir_path, "Imagenes", subdir_name)
    if not os.path.exists(full_path):
        return f"% Directory {full_path} not found\n"
    
    files = [f for f in os.listdir(full_path) if f.endswith(('.png', '.jpg', '.jpeg'))]
    # Filter out files that don't start with a number and specifically exclude '-vel'
    files = [f for f in files if re.match(r'^\d+', f) and '-vel' not in f]
    files.sort(key=sort_key)
    
    latex = f"\\subsection{{{title}}}\n\n"
    
    # We want 3 images per page. A good way is to group them by the leading number (test series)
    # or just put them in a row/grid.
    # Since each test (1, 2, 3...) has 3 images (pos, angulo, sim), we can group them.
    
    for i, f in enumerate(files):
        caption = f.replace('_', ' ').replace('-', ' ').replace('.png', '').replace('.jpg', '').replace('.jpeg', '')
        path_for_latex = os.path.join("Imagenes", subdir_name, f)
        
        # To fit 3 per page, we can use 0.3 or 0.32 width and put them side by side
        # or just make them smaller vertically.
        # Let's try side-by-side if they belong to the same group.
        
        latex += "\\begin{figure}[H]\n"
        latex += "    \\centering\n"
        latex += f"    \\includegraphics[width=0.8\\textwidth]{{{path_for_latex}}}\n"
        latex += f"    \\caption{{{caption}}}\n"
        latex += f"    \\label{{fig:{f.split('.')[0]}_{subdir_name.replace(' ', '_')}}}\n"
        latex += "\\end{figure}\n\n"
        
        # Add a clearpage or similar every 3 figures to ensure "3 por pagina" if they are stacked
        # But if they are small enough, LaTeX should handle it. 
        # Actually, if I want exactly 3 per page and stacked, I should reduce height or width.
        # width=0.8 is too big for 3 vertically. Let's use 0.5 or 0.45.
        
    return latex

# Actually, I'll update the loop to be more specific about "3 per page"
def generate_latex_v3(dir_path, subdir_name, title):
    full_path = os.path.join(dir_path, "Imagenes", subdir_name)
    if not os.path.exists(full_path):
        return f"% Directory {full_path} not found\n"
    
    files = [f for f in os.listdir(full_path) if f.endswith(('.png', '.jpg', '.jpeg'))]
    files = [f for f in files if re.match(r'^\d+', f) and '-vel' not in f]
    files.sort(key=sort_key)
    
    latex = f"\\subsection{{{title}}}\n\n"
    
    for i, f in enumerate(files):
        caption = f.replace('_', ' ').replace('-', ' ').replace('.png', '').replace('.jpg', '').replace('.jpeg', '')
        path_for_latex = os.path.join("Imagenes", subdir_name, f)
        
        # 3 stacked images per page. width=0.6\textwidth should fit 3 vertically.
        latex += "\\begin{figure}[H]\n"
        latex += "    \\centering\n"
        latex += f"    \\includegraphics[width=0.6\\textwidth]{{{path_for_latex}}}\n"
        latex += f"    \\caption{{{caption}}}\n"
        latex += f"    \\label{{fig:{f.split('.')[0]}_{i}}}\n"
        latex += "\\end{figure}\n\n"
        
        # Every 3 images, or at the end of a subsection, we might want a clearpage if we strictly want "3 per page"
        if (i + 1) % 3 == 0:
            latex += "\\clearpage\n\n"
            
    return latex

base_dir = "/home/emers/universidad/sistemas-de-control-II/proyecto-pendulo"
output_file = os.path.join(base_dir, "resultados.tex")

preamble = r"""\documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage[spanish]{babel}
\usepackage{graphicx}
\usepackage{float}
\usepackage[margin=0.7in]{geometry}

\begin{document}

"""

content = "\\section{Resultados}\n\n"
content += generate_latex_v3(base_dir, "Test Cambio de posicion", "Test cambio de posición")
content += generate_latex_v3(base_dir, "Test Perturbacion angulo", "Test perturbación ángulo")

with open(output_file, 'w') as f:
    f.write(preamble + content + "\n\\end{document}")

print(f"Generated {output_file}")
