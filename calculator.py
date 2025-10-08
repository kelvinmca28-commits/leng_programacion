import tkinter as tk
from tkinter import messagebox, scrolledtext, simpledialog 
import random
import json
import os
from datetime import datetime

# --- Configuración y Constantes ---
ARCHIVO_HISTORIAL = 'historial_matematicas.json'
OPERACIONES = ['+', '-', '*', '/']

# Definición de rangos de dificultad
DIFICULTADES = {
    "Fácil": (1, 20, 5),      # Rango extendido a 20
    "Medio": (1, 150, 3),     # Rango extendido a 150
    "Difícil": (1, 500, 1),   # Rango extendido a 500 (Permite resultados negativos)
    "Experto": (1, 1000, 1)   # Nuevo nivel (Permite resultados negativos)
}

# --- Funciones de Persistencia de Datos ---

def cargar_historial():
    """Carga TODOS los datos de usuarios desde el archivo JSON."""
    if os.path.exists(ARCHIVO_HISTORIAL):
        try:
            with open(ARCHIVO_HISTORIAL, 'r') as f:
                # Se carga la estructura de datos (esperamos un diccionario)
                return json.load(f) 
        except json.JSONDecodeError:
            print("Advertencia: El archivo de historial está corrupto o vacío. Se iniciará un historial nuevo.")
            return {}
    return {}

def guardar_historial(todos_los_datos):
    """Guarda todos los datos de usuarios en el archivo JSON."""
    with open(ARCHIVO_HISTORIAL, 'w') as f:
        json.dump(todos_los_datos, f, indent=4)

# --- Lógica de Generación de Problemas ---

def generar_problema(dificultad):
    """Genera un problema matemático basado en el nivel de dificultad seleccionado."""
    
    # Se utiliza n1_max y n2_max para los rangos de random.randint
    n1_max, n2_max, _ = DIFICULTADES[dificultad]
    
    num1 = random.randint(1, n1_max)
    num2 = random.randint(1, n2_max)
    operador = random.choice(OPERACIONES)
    
    if operador == '-':
        # Corregido: Solo en Difícil/Experto permitimos resultados negativos.
        if dificultad not in ["Difícil", "Experto"] and num1 < num2:
            num1, num2 = num2, num1  
            
    elif operador == '/':
        if num2 == 0: num2 = 1  
        # Asegura que num1 sea un múltiplo de num2 para que el resultado sea entero
        num1 = num1 * num2
        
    problema_str = f"{num1} {operador} {num2}"
    
    try:
        respuesta_correcta = int(eval(problema_str)) 
    except ZeroDivisionError:
        return generar_problema(dificultad)  
        
    return problema_str, respuesta_correcta

# --- Implementación de la Interfaz Gráfica con Tkinter (Clase Principal) ---

class TutorMatematicasApp:
    def __init__(self, master):
        self.master = master
        
        # 1. Cargar todos los datos y asegurar que sea un diccionario
        self.TODOS_LOS_DATOS = cargar_historial() 
        
        # FIX PRINCIPAL: Si lo cargado NO es un diccionario (e.g., es una lista antigua), lo reiniciamos.
        if not isinstance(self.TODOS_LOS_DATOS, dict):
             print("Historial reestructurado: Se detectó un formato antiguo y se ha reiniciado el historial multi-usuario.")
             self.TODOS_LOS_DATOS = {}

        self.usuario_actual = ""
        
        self.iniciar_sesion() # Llama al cuadro de diálogo de inicio de sesión
        
        # 2. Configurar la aplicación si el usuario inició sesión
        if self.usuario_actual:
            master.title(f"🚀 Tutor de Matemáticas | Usuario: {self.usuario_actual}")
            
            # Obtener el historial específico del usuario actual (o lista vacía si es nuevo)
            # Nota: self.historial ahora solo guarda la referencia del usuario actual.
            self.historial = self.TODOS_LOS_DATOS.get(self.usuario_actual, [])
            
            self.problema_actual = ""
            self.respuesta_correcta = 0
            self.dificultad_seleccionada = tk.StringVar(value="Medio")
            
            self.configurar_widgets()
            self.actualizar_estadisticas()
            self.generar_nuevo_problema()
        else:
            # Cerrar la ventana si el usuario cancela la sesión
            master.destroy()

    def iniciar_sesion(self):
        """Muestra un cuadro de diálogo para que el usuario ingrese su nombre."""
        while True:
            nombre = simpledialog.askstring("Inicio de Sesión", "Ingresa tu nombre de usuario:", 
                                            parent=self.master)
            if nombre:
                # Limpiar y capitalizar el nombre para usarlo como clave única
                self.usuario_actual = nombre.strip().capitalize()
                
                # Si es un nuevo usuario, inicializa su historial en el diccionario global
                if self.usuario_actual not in self.TODOS_LOS_DATOS:
                    # Esta línea ahora es segura porque TODOS_LOS_DATOS es un diccionario
                    self.TODOS_LOS_DATOS[self.usuario_actual] = []
                    
                break
            else:
                # Si el usuario presiona Cancelar, no se inicia la aplicación
                self.usuario_actual = None 
                break

    def configurar_widgets(self):
        """Define y posiciona todos los elementos de la GUI."""
        
        # Frame Superior (Dificultad y Estadísticas)
        frame_top = tk.Frame(self.master)
        frame_top.pack(pady=10, padx=20, fill='x')

        lbl_dif = tk.Label(frame_top, text="Dificultad:", font=('Arial', 10, 'bold'))
        lbl_dif.pack(side=tk.LEFT, padx=(0, 5))
        
        opciones_dif = list(DIFICULTADES.keys())
        menu_dif = tk.OptionMenu(frame_top, self.dificultad_seleccionada, *opciones_dif)
        menu_dif.config(font=('Arial', 10))
        menu_dif.pack(side=tk.LEFT)
        
        self.lbl_stats = tk.Label(frame_top, text="", font=('Arial', 10, 'bold'), fg='#006400')
        self.lbl_stats.pack(side=tk.RIGHT, padx=(10, 0))

        tk.Frame(self.master, height=1, bg='lightgray').pack(fill='x', padx=10, pady=5)
        
        # Etiqueta para el problema
        self.lbl_problema = tk.Label(self.master, text="Presiona 'Nuevo Problema'", font=('Arial', 24, 'bold'), fg='#333333')
        self.lbl_problema.pack(pady=30)

        # Campo de entrada para la respuesta
        self.var_respuesta = tk.StringVar()
        self.entrada_respuesta = tk.Entry(self.master, textvariable=self.var_respuesta, font=('Arial', 20), justify='center', width=10)
        self.entrada_respuesta.pack(pady=10)
        
        # Botones de Acción
        frame_botones = tk.Frame(self.master)
        frame_botones.pack(pady=15)
        
        self.btn_comprobar = tk.Button(frame_botones, text="✔️ Comprobar", command=self.comprobar_respuesta, bg='#4CAF50', fg='white', font=('Arial', 12))
        self.btn_comprobar.pack(side=tk.LEFT, padx=10, ipady=5)
        
        self.btn_nuevo = tk.Button(frame_botones, text="🔁 Nuevo Problema", command=self.generar_nuevo_problema, font=('Arial', 12))
        self.btn_nuevo.pack(side=tk.LEFT, padx=10, ipady=5)

        # Retroalimentación
        self.lbl_feedback = tk.Label(self.master, text="", font=('Arial', 14))
        self.lbl_feedback.pack(pady=15)
        
        # Frame para botones inferiores (Historial y Usuarios)
        frame_inferior_btns = tk.Frame(self.master)
        frame_inferior_btns.pack(pady=(5, 20))
        
        # Botón para el historial DETALLADO del usuario actual
        self.btn_historial = tk.Button(frame_inferior_btns, text="📋 Ver Mi Historial", command=self.mostrar_historial_gui, font=('Arial', 10))
        self.btn_historial.pack(side=tk.LEFT, padx=5)

        # Botón para ver la lista de todos los usuarios (Ahora un selector)
        self.btn_usuarios = tk.Button(frame_inferior_btns, text="👥 Ver Historiales (Admin)", command=self.mostrar_lista_usuarios, font=('Arial', 10))
        self.btn_usuarios.pack(side=tk.LEFT, padx=5)
        
        # Bindings (teclas rápidas)
        self.master.bind('<Return>', lambda event: self.comprobar_respuesta())
        self.dificultad_seleccionada.trace_add("write", lambda *args: self.generar_nuevo_problema())

    def actualizar_estadisticas(self):
        """Calcula y muestra un resumen de las estadísticas en la ventana principal."""
        if not self.historial:
            self.lbl_stats.config(text="Acierto: 0/0 (0.00%)")
            return

        total = len(self.historial)
        correctas = sum(1 for registro in self.historial if registro['es_correcto'])
        porcentaje = f"{correctas/total*100:.2f}%" if total > 0 else "0.00%"
        
        self.lbl_stats.config(text=f"Acierto: {correctas}/{total} ({porcentaje})")

    def generar_nuevo_problema(self):
        """Genera un nuevo problema según la dificultad seleccionada y actualiza la interfaz."""
        dificultad = self.dificultad_seleccionada.get()
        self.problema_actual, self.respuesta_correcta = generar_problema(dificultad)
        
        self.lbl_problema.config(text=f"{self.problema_actual} = ?")
        self.lbl_feedback.config(text="")
        self.var_respuesta.set("")
        self.entrada_respuesta.focus()

    def comprobar_respuesta(self):
        """Verifica la respuesta, da feedback y actualiza el historial."""
        
        try:
            respuesta_usuario = int(self.var_respuesta.get())
        except ValueError:
            self.lbl_feedback.config(text="❌ ¡Error! Ingresa solo números enteros.", fg='red')
            return

        es_correcto = (respuesta_usuario == self.respuesta_correcta)
        dificultad = self.dificultad_seleccionada.get()
        
        # 1. Retroalimentación visual
        if es_correcto:
            feedback_text = "✅ ¡Correcto! ¡Sigue así!"
            color = 'green'
        else:
            feedback_text = f"❌ Incorrecto. La respuesta era {self.respuesta_correcta}."
            color = 'red'
        
        self.lbl_feedback.config(text=feedback_text, fg=color)
        
        # 2. Almacenamiento en el historial
        registro = {
            'problema': self.problema_actual,
            'respuesta_usuario': respuesta_usuario,
            'respuesta_correcta': self.respuesta_correcta,
            'es_correcto': es_correcto,
            'dificultad': dificultad,
            'fecha': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # Añade al historial del usuario actual en memoria
        self.historial.append(registro)
        # Actualiza el diccionario global con el historial modificado
        self.TODOS_LOS_DATOS[self.usuario_actual] = self.historial 
        
        guardar_historial(self.TODOS_LOS_DATOS) # Guarda el diccionario global
        self.actualizar_estadisticas()  

    def guardar_historial_para_imprimir(self, usuario_a_mostrar, contenido):
        """Guarda el contenido del historial en un archivo de texto para que el usuario pueda imprimirlo."""
        try:
            # Crea un nombre de archivo seguro
            nombre_archivo = f"Historial_{usuario_a_mostrar.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            
            # Intenta guardar el archivo en el directorio actual
            with open(nombre_archivo, 'w', encoding='utf-8') as f:
                f.write(contenido)
                
            messagebox.showinfo(
                "Historial Guardado", 
                f"El historial de '{usuario_a_mostrar}' ha sido guardado exitosamente en:\n{os.path.abspath(nombre_archivo)}\n\nPuedes abrir este archivo para imprimirlo."
            )
        except Exception as e:
            messagebox.showerror("Error al Guardar", f"Ocurrió un error al intentar guardar el archivo: {e}")


    def _mostrar_historial_de_usuario(self, usuario_a_mostrar):
        """Muestra el historial detallado para el usuario proporcionado (función universal)."""
        historial_usuario = self.TODOS_LOS_DATOS.get(usuario_a_mostrar, [])
        
        if not historial_usuario:
            messagebox.showinfo("Historial Vacío", f"El usuario {usuario_a_mostrar} no tiene ejercicios registrados.")
            return

        # 1. Crear la nueva ventana
        ventana_historial = tk.Toplevel(self.master)
        ventana_historial.title(f"Historial de Práctica de {usuario_a_mostrar}")
        ventana_historial.geometry("550x500") # Aumentamos la altura para el nuevo botón
        
        # 2. Frame para el área de texto
        frame_historial_area = tk.Frame(ventana_historial)
        frame_historial_area.pack(expand=True, fill='both', padx=10, pady=(10, 5))

        # 2. Crear el widget de texto desplazable
        txt_area = scrolledtext.ScrolledText(frame_historial_area, wrap=tk.WORD, font=('Courier', 10), padx=10, pady=10)
        txt_area.pack(expand=True, fill='both')

        # 3. Generar el contenido del historial
        
        # Contenido de texto que se usará para el guardado/impresión
        contenido_historial_completo = ""
        
        # --- Generar resumen ---
        stats_por_dificultad = {}
        for reg in historial_usuario:
            dif = reg['dificultad']
            if dif not in stats_por_dificultad:
                stats_por_dificultad[dif] = {'total': 0, 'correctas': 0}
            stats_por_dificultad[dif]['total'] += 1
            if reg['es_correcto']:
                stats_por_dificultad[dif]['correctas'] += 1

        resumen_header = "=================================================\n"
        resumen_body = f"        📊 RESUMEN PARA {usuario_a_mostrar.upper()}\n"
        
        contenido_historial_completo += resumen_header + resumen_body + resumen_header
        
        for dif, stats in stats_por_dificultad.items():
            porcentaje = f"{stats['correctas']/stats['total']*100:.2f}%" if stats['total'] > 0 else "0.00%"
            linea_resumen = f"- {dif:<8}: {stats['correctas']}/{stats['total']} aciertos ({porcentaje})\n"
            contenido_historial_completo += linea_resumen
        
        # Generar texto de detalle
        detalle_header = "\n=================================================\n"
        detalle_body = "           📝 REGISTRO COMPLETO\n"
        
        contenido_historial_completo += detalle_header + detalle_body + detalle_header
        
        # Mostrar todo el historial, ordenado por más reciente primero
        for i, registro in enumerate(reversed(historial_usuario)):
            resultado = "✅ CORRECTO" if registro['es_correcto'] else f"❌ INCORRECTO (Era: {registro['respuesta_correcta']})"
            
            linea_detalle = (
                f"[{registro['fecha'].split(' ')[0]}] "
                f"[{registro['dificultad']:<6}] | "
                f"Problema: {registro['problema']:<10} | "
                f"Tu Resp: {registro['respuesta_usuario']:<4} | "
                f"{resultado}\n"
            )
            contenido_historial_completo += linea_detalle

        # Insertar el contenido generado en el área de texto
        txt_area.insert(tk.END, contenido_historial_completo)

        # 4. Deshabilitar edición y mover al inicio
        txt_area.config(state=tk.DISABLED)
        txt_area.yview_moveto(0)
        
        # 5. NUEVO Botón de Imprimir/Guardar
        btn_imprimir = tk.Button(
            ventana_historial, 
            text="🖨️ Guardar para Imprimir", 
            command=lambda: self.guardar_historial_para_imprimir(usuario_a_mostrar, contenido_historial_completo), 
            font=('Arial', 11, 'bold'),
            bg='#ADD8E6',
            fg='#1C1C1C'
        )
        btn_imprimir.pack(pady=10)


    def mostrar_historial_gui(self):
        """Llama a la función universal para mostrar el historial del usuario actual."""
        # Usa la función universal con el usuario logueado actualmente
        self._mostrar_historial_de_usuario(self.usuario_actual)


    def mostrar_lista_usuarios(self):
        """Crea una nueva ventana para mostrar y seleccionar usuarios para ver su historial."""
        
        usuarios = list(self.TODOS_LOS_DATOS.keys())
        
        if not usuarios:
            messagebox.showinfo("Usuarios Registrados", "¡Solo estás tú! No hay otros usuarios en el historial.")
            return

        # 1. Crear la nueva ventana
        ventana_usuarios = tk.Toplevel(self.master)
        ventana_usuarios.title("👥 Seleccionar Usuario para Historial")
        ventana_usuarios.geometry("400x450")
        
        tk.Label(ventana_usuarios, text="Selecciona un usuario:", font=('Arial', 14, 'bold'), fg='#333333').pack(pady=10)
        
        # Listbox para seleccionar usuarios
        listbox_usuarios = tk.Listbox(ventana_usuarios, font=('Arial', 12), height=15, selectmode=tk.SINGLE)
        listbox_usuarios.pack(expand=True, fill='both', padx=20, pady=10)
        
        for u in sorted(usuarios):
            listbox_usuarios.insert(tk.END, u)
            
        # Función para manejar la selección y mostrar el historial
        def ver_historial_seleccionado(event=None):
            seleccion = listbox_usuarios.curselection()
            if seleccion:
                usuario_seleccionado = listbox_usuarios.get(seleccion[0])
                self._mostrar_historial_de_usuario(usuario_seleccionado)
            else:
                messagebox.showerror("Error de Selección", "Por favor, selecciona un usuario de la lista.")

        # Botón para ver el historial del usuario seleccionado
        btn_ver = tk.Button(ventana_usuarios, 
                            text="🔎 Ver Historial Seleccionado", 
                            command=ver_historial_seleccionado, 
                            font=('Arial', 12), 
                            bg='#ADD8E6', 
                            fg='#1C1C1C')
        btn_ver.pack(pady=10)
        
        # Seleccionar el primer elemento por defecto y enlazar doble clic
        if usuarios:
            listbox_usuarios.select_set(0) 
            listbox_usuarios.bind('<Double-Button-1>', ver_historial_seleccionado) # Doble clic también funciona

# --- Ejecución de la Aplicación ---
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x450")
    app = TutorMatematicasApp(root)
    root.mainloop()
