from django.contrib.auth.models import User
from django.db import models

from SIGPE.settings import MEDIA_URL, STATIC_URL


# Create your models here.
class Project(models.Model):
    STATES = [
        ('aprobado','Aprobado'),
        ('pendiente', 'Pendiente'),
        ('finalizado', 'Finalizado'),
    ]
    EVALUATIONS = [
        ('Mal','Mal'),
        ('Regular','Regular'),
        ('Bien','Bien'),
        ('Excelente','Excelente'),
    ]
    AREAS = [
        ('Agromercado La Arboleda', 'Agromercado La Arboleda'),
        ('Aguas de la Habana', 'Aguas de la Habana'),
        ('Banco Metropolitano', 'Banco Metropolitano'),
        ('CALISOFT', 'CALISOFT'),
        ('Orlando López', 'Orlando López'),
        ('COPEXTEL', 'COPEXTEL'),
        ('Cadena Cubana del Pan', 'Cadena Cubana del Pan'),
        ('Cafetería "Doble Clic"', 'Cafetería "Doble Clic"'),
        ('Cafetería "El Paraíso"', 'Cafetería "El Paraíso"'),
        ('Cafetería "La Piscina"', 'Cafetería "La Piscina"'),
        ('Cafetería "Las Frituras"', 'Cafetería "Las Frituras"'),
        ('Cafetería "Quiosco Rectorado"', 'Cafetería "Quiosco Rectorado"'),
        ('Cafetería "Tiempo Café"', 'Cafetería "Tiempo Café"'),
        ('Cafetería “Las Delicias”', 'Cafetería “Las Delicias”'),
        ('Centro Nacional de Educación a Distancia', 'Centro Nacional de Educación a Distancia'),
        ('Centro de Estudio de Matemática y Computación', 'Centro de Estudio de Matemática y Computación'),
        ('Centro de Gobierno Electrónico', 'Centro de Gobierno Electrónico'),
        ('Centro de Idiomas', 'Centro de Idiomas'),
        ('Centro de Informatización de Entidades', 'Centro de Informatización de Entidades'),
        ('Centro de Informatización de la Gestión Documental', 'Centro de Informatización de la Gestión Documental'),
        ('Centro de Informática Médica', 'Centro de Informática Médica'),
        ('Centro de Innovación y Calidad en la Educación', 'Centro de Innovación y Calidad en la Educación'),
        ('Centro de Innovación y Desarrollo de Internet', 'Centro de Innovación y Desarrollo de Internet'),
        ('Centro de Representación y Análisis de Datos', 'Centro de Representación y Análisis de Datos'),
        ('Centro de Software Libres', 'Centro de Software Libres'),
        ('Centro de Soporte Tecnológico', 'Centro de Soporte Tecnológico'),
        ('Centro de Tecnologías Interactivas', 'Centro de Tecnologías Interactivas'),
        ('Centro de Tecnologías para la Formación', 'Centro de Tecnologías para la Formación'),
        ('Departamento de Enseñanza Militar', 'Departamento de Enseñanza Militar'),
        ('Dirección Complejo Alimentos 1', 'Dirección Complejo Alimentos 1'),
        ('Dirección Complejo Alimentos 2', 'Dirección Complejo Alimentos 2'),
        ('Dirección Complejo Alimentos 3', 'Dirección Complejo Alimentos 3'),
        ('Dirección Complejo Residencial', 'Dirección Complejo Residencial'),
        ('Dirección General de Logística', 'Dirección General de Logística'),
        ('Dirección General de Servicios', 'Dirección General de Servicios'),
        ('Dirección General de Alimentos', 'Dirección General de Alimentos'),
        ('Dirección General de Economía', 'Dirección General de Economía'),
        ('Dirección General de Tecnología', 'Dirección General de Tecnología'),
        ('Dirección Jurídica', 'Dirección Jurídica'),
        ('Dirección Servicios de Protocolo', 'Dirección Servicios de Protocolo'),
        ('Dirección de Almacenes', 'Dirección de Almacenes'),
        ('Dirección de Calidad de Software', 'Dirección de Calidad de Software'),
        ('Dirección de Ciencia, Tecnología e Innovación', 'Dirección de Ciencia, Tecnología e Innovación'),
        ('Dirección de Compras', 'Dirección de Compras'),
        ('Dirección de Comunicación Institucional', 'Dirección de Comunicación Institucional'),
        ('Dirección de Contabilidad y Finanzas', 'Dirección de Contabilidad y Finanzas'),
        ('Dirección de Control Interno', 'Dirección de Control Interno'),
        ('Dirección de Cuadros', 'Dirección de Cuadros'),
        ('Dirección de Defensa y Seguridad', 'Dirección de Defensa y Seguridad'),
        ('Dirección de Deportes', 'Dirección de Deportes'),
        ('Dirección de Educación de Posgrado', 'Dirección de Educación de Posgrado'),
        ('Dirección de Extensión Universitaria', 'Dirección de Extensión Universitaria'),
        ('Dirección de Formación de PregradoDirección de Gestión Tecnológica',
         'Dirección de Formación de PregradoDirección de Gestión Tecnológica'),
        ('Dirección de Historia y Marxismo Leninismo', 'Dirección de Historia y Marxismo Leninismo'),
        ('Dirección de Información Científico Técnica', 'Dirección de Información Científico Técnica'),
        ('Dirección de Informatización', 'Dirección de Informatización'),
        ('Dirección de Inversiones y Mantenimiento', 'Dirección de Inversiones y Mantenimiento'),
        ('Dirección de Panadería y Dulcería', 'Dirección de Panadería y Dulcería'),
        ('Dirección de Planificación', 'Dirección de Planificación'),
        ('Dirección de Producción de Software', 'Dirección de Producción de Software'),
        ('Dirección de Proyectos Especiales', 'Dirección de Proyectos Especiales'),
        ('Dirección de Recursos Humanos', 'Dirección de Recursos Humanos'),
        ('Dirección de Redes y Servicios Telemáticos', 'Dirección de Redes y Servicios Telemáticos'),
        ('Dirección de Relaciones Internacionales', 'Dirección de Relaciones Internacionales'),
        ('Dirección de Residencia', 'Dirección de Residencia'),
        ('Dirección de Seguridad Informática', 'Dirección de Seguridad Informática'),
        ('Dirección de Servicios Generales', 'Dirección de Servicios Generales'),
        ('Dirección de Transferencia de Tecnología', 'Dirección de Transferencia de Tecnología'),
        ('Dirección de Transporte', 'Dirección de Transporte'),
        ('ETECSA S.A. Empresa de Telecomunicaciones de Cuba', 'ETECSA S.A. Empresa de Telecomunicaciones de Cuba'),
        ('Facultad 1', 'Facultad 1'),
        ('Facultad 2', 'Facultad 2'),
        ('Facultad 3', 'Facultad 3'),
        ('Facultad 4', 'Facultad 4'),
        ('Facultad de Ciencias y Tecnologías Computacionales', 'Facultad de Ciencias y Tecnologías Computacionales'),
        ('Facultad de Tecnologías Educativas', 'Facultad de Tecnologías Educativas'),
        ('Fábrica de Helado', 'Fábrica de Helado'),
        ('Gastronomía', 'Gastronomía'),
        ('Guarapera La Piscina', 'Guarapera La Piscina'),
        ('Mercadito El Ideal', 'Mercadito El Ideal'),
        ('Mercado Artesanal Industrial', 'Mercado Artesanal Industrial'),
        ('Ministerio de Industrias', 'Ministerio de Industrias'),
        ('Parque Científico Tecnológico', 'Parque Científico Tecnológico'),
        ('Peluquería-Barbería', 'Peluquería-Barbería'),
        ('Pescadería', 'Pescadería'),
        ('Policlínico-Hospital', 'Policlínico-Hospital'),
        ('SEPCOM', 'SEPCOM'),
        ('SOFTEL', 'SOFTEL'),
        ('Secretaría General', 'Secretaría General'),
        ('Servicios a la Comunidad', 'Servicios a la Comunidad'),
        ('Subdirección de Residencia 1', 'Subdirección de Residencia 1'),
        ('Subdirección de Residencia 2', 'Subdirección de Residencia 2'),
        ('Subdirección de Residencia de Trabajadores', 'Subdirección de Residencia de Trabajadores'),
        ('Tienda Panamericana', 'Tienda Panamericana'),
        ('UCI-MININT', 'UCI-MININT'),
        ('UNIDAD-MININT', 'UNIDAD-MININT'),
        ('Vicerrectoría Primera', 'Vicerrectoría Primera'),
        ('Vicerrectoría de Extensión Universitaria', 'Vicerrectoría de Extensión Universitaria'),
        ('Vicerrectoría de Formación', 'Vicerrectoría de Formación'),
        ('Vicerrectoría de Investigación y Posgrado', 'Vicerrectoría de Investigación y Posgrado'),
        ('Zapatería-Atelier', 'Zapatería-Atelier'),
        ('Área de Atención FAR', 'Área de Atención FAR'),
    ]

    name = models.CharField(verbose_name='Nombre', max_length=150, null=False)
    area = models.CharField(verbose_name='Área', max_length=150, choices = AREAS, null=False)
    state = models.CharField(verbose_name='Estado',max_length=10, choices=STATES)
    start_date = models.DateField(verbose_name='Fecha de inicio', null=False)
    end_date = models.DateField(verbose_name='Fecha de fin', null=True, blank=True)
    fundamentation = models.TextField(verbose_name='Fundamentación',null=True, blank=True)
    evaluation = models.TextField(verbose_name='Evaluación',choices=EVALUATIONS, null=True, blank=True)
    conclution = models.TextField(verbose_name='Conclución',null=True, blank=True)
    recomendation = models.TextField(verbose_name='Recomendación',null=True, blank=True)
    image = models.ImageField(upload_to='images/projects/%Y/%m/%d', null=True, blank=True)

    # estado(aprobado, pendiente, finalizado)
    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        db_table = 'Project'

    def __str__(self):
        return "%s" % (self.name)
    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'dist/img/empty_project.png')