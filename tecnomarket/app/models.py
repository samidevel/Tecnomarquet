from django.db import models

class UserProfile(models.Model):
	name = models.CharField(max_length=100)
	#username = 


class Marca(models.Model):
	nombre = models.CharField(max_length=50)

	def __str__(self):
		return self.nombre

class Producto(models.Model):
	nombre      = models.CharField(max_length=50)
	precio      = models.IntegerField()
	descripcion = models.TextField()
	nuevo       = models.BooleanField()
	marca       = models.ForeignKey(Marca, on_delete=models.PROTECT)
	imagen      = models.ImageField(upload_to="productos", null=True)
	#fecha_fabricacion = models.DateField()
	
	def __str__(self):
		return self.nombre


opciones_consultas = [

	[0, 'consulta'],
	[1, 'reclamo'],
	[2, 'sugerencias'],
	[3, 'felicitaciones']
]

class Contacto(models.Model):
	nombre        = models.CharField(max_length=50)
	correo        = models.EmailField()
	tipo_consulta = models.IntegerField(choices=opciones_consultas)
	mensaje       = models.TextField()
	avisos        = models.BooleanField()

	def __str__(self):
		return self.nombre, 