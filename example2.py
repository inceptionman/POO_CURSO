from datetime import datetime

# ---- Clase Contenido ----
class Contenido:
    def __init__(self, contenido_id, titulo, tipo, anio, generos, idiomas, clasificacion, temporadas=None, duracion_min=None):
        self.contenido_id = contenido_id
        self.titulo = titulo
        self.tipo = tipo
        self.anio = anio
        self.generos = generos
        self.idiomas = idiomas
        self.clasificacion = clasificacion
        self.temporadas = temporadas
        self.duracion_min = duracion_min


    def mostrar_info(self):
        print(f"{self.titulo} ({self.tipo}) - {self.anio}")
        print(f"Géneros: {', '.join(self.generos)}")
        print(f"Idiomas: {', '.join(self.idiomas)}")
        print(f"Clasificación: {self.clasificacion}")
        if self.temporadas:
            print(f"Temporadas: {self.temporadas}")
        if self.duracion_min:
            print(f"Duración: {self.duracion_min} min")
        print("")

# ---- Clase Dispositivo ----
class Dispositivo:
    def __init__(self, dispositivo_id, tipo, marca, modelo, ultima_fecha, ubicacion):
        self.dispositivo_id = dispositivo_id
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.ultima_fecha = ultima_fecha
        self.ubicacion = ubicacion

# ---- Clase Historial ----
class Historial:
    def __init__(self, contenido, fecha_visto, progreso, dispositivo_usado):
        self.contenido = contenido
        self.fecha_visto = fecha_visto
        self.progreso = progreso
        self.dispositivo_usado = dispositivo_usado

# ---- Clase Perfil ----
class Perfil:
    def __init__(self, perfil_id, nombre, idioma):
        self.perfil_id = perfil_id
        self.nombre = nombre
        self.idioma = idioma
        self.favoritos = []
        self.historial = []

    def agregar_favorito(self, contenido):
        self.favoritos.append(contenido)

    def registrar_visto(self, contenido, progreso, dispositivo):
        registro = Historial(contenido, datetime.now(), progreso, dispositivo)
        self.historial.append(registro)

# ---- Clase Suscripción ----
class Suscripcion:
    def __init__(self, tipo_plan, precio, fecha_inicio, metodo_pago, renovacion):
        self.tipo_plan = tipo_plan
        self.precio = precio
        self.fecha_inicio = fecha_inicio
        self.metodo_pago = metodo_pago
        self.renovacion = renovacion
        self.fecha_vencimiento = self.calcular_fecha_vencimiento()
    def calcular_fecha_vencimiento(self):
        fecha_inicio = datetime.strptime(self.fecha_inicio, "%Y-%m-%d")
        if self.renovacion:
            return fecha_inicio.replace(year=fecha_inicio.year + 1).strftime("%Y-%m-%d")
        else:
            return fecha_inicio.strftime("%Y-%m-%d")
        self_estado = "Activo" if self.renovacion else "Inactivo"
        print(f"Suscripción: {self.tipo_plan} - {self_estado}")

# ---- Clase Usuario ----
class Usuario:
    def __init__(self, usuario_id, nombre, email, suscripcion):
        self.usuario_id = usuario_id
        self.nombre = nombre
        self.email = email
        self.suscripcion = suscripcion
        self.perfiles = []
        self.dispositivos = []

    def agregar_perfil(self, perfil):
        self.perfiles.append(perfil)

    def agregar_dispositivo(self, dispositivo):
        self.dispositivos.append(dispositivo)

# ================== EJEMPLO DE USO ==================

# Contenidos
c1 = Contenido(201, "Stranger Things", "Serie", 2016, ["Ciencia ficción", "Suspenso", "Drama"], ["Español", "Inglés"], "16+", temporadas=4)
c2 = Contenido(202, "El Irlandés", "Película", 2019, ["Drama", "Crimen"], ["Español", "Inglés"], "18+", duracion_min=209)
c3 = Contenido(203, "Falsa identidad", "Serie", 2021, ["Spanish-Language", "Crimen", "Drama"],["Español", "Inglés"], "18+", temporadas=2)

# Suscripción
suscripcion = Suscripcion("Premium", 38900, "2023-05-15", "Tarjeta de crédito", True)

# Usuario
usuario = Usuario(1001, "Yeison", "yeisonhincapie13@gmail.com", suscripcion)

# Dispositivos
d1 = Dispositivo("D001", "Smart TV", "Samsung", "QLED 55\"", "2025-08-10", "Bogotá")
d2 = Dispositivo("D002", "Teléfono", "Apple", "iPhone 14", "2025-08-12", "Medellín")
usuario.agregar_dispositivo(d1)
usuario.agregar_dispositivo(d2)

# Perfiles
perfil1 = Perfil(1, "Yeison", "Español")
perfil2 = Perfil(2, "Yanier", "Inglés")

# Agregar favoritos y registrar historial
perfil1.agregar_favorito(c1)
perfil1.registrar_visto(c1, "100%", d1)
perfil1.registrar_visto(c2, "75%", d2)
perfil2.registrar_visto(c3, "27%", d1 )

# Añadir perfiles al usuario
usuario.agregar_perfil(perfil1)
usuario.agregar_perfil(perfil2)

# Mostrar información
print(f"Usuario: {usuario.nombre}")
print("Perfiles:")
for p in usuario.perfiles:
    print(f" - {p.nombre} ({p.idioma})")
    for h in p.historial:
        print(f"   * Vió {h.contenido.titulo} en {h.dispositivo_usado.tipo} ({h.progreso} completado)")
