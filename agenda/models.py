from django.db import models

class Empresa(models.Model):
    emp_id = models.AutoField(primary_key=True)
    emp_nombre = models.CharField(max_length=255)
    emp_direccion = models.CharField(max_length=255)
    emp_telefono = models.CharField(max_length=20)
    emp_email = models.EmailField(max_length=255)

    def __str__(self):
        return self.emp_nombre

    class Meta:
        verbose_name_plural = "Empresas"

class Negocio(models.Model):
    neg_id = models.AutoField(primary_key=True)
    neg_emp = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    neg_nombre = models.CharField(max_length=255)
    neg_tipo = models.CharField(max_length=255)
    neg_direccion = models.CharField(max_length=255)
    neg_telefono = models.CharField(max_length=20)
    neg_email = models.EmailField(max_length=255)

    def __str__(self):
        return self.neg_nombre

    class Meta:
        verbose_name_plural = "Negocios"

class Servicio(models.Model):
    srv_id = models.AutoField(primary_key=True)
    srv_neg = models.ForeignKey(Negocio, on_delete=models.CASCADE)
    srv_nombre = models.CharField(max_length=255)
    srv_descripcion = models.TextField()

    def __str__(self):
        return self.srv_nombre

    class Meta:
        verbose_name_plural = "Servicios"

class Usuario(models.Model):
    usu_id = models.AutoField(primary_key=True)
    srv_neg = models.ForeignKey(Negocio, on_delete=models.CASCADE)
    usu_nombre = models.CharField(max_length=255)
    usu_telefono = models.CharField(max_length=20)
    usu_email = models.EmailField(max_length=255)

    def __str__(self):
        return self.usu_nombre

    class Meta:
        verbose_name_plural = "Usuarios"

class Cliente(models.Model):
    cli_id = models.AutoField(primary_key=True)
    cli_nombre = models.CharField(max_length=255)
    cli_telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.cli_nombre

    class Meta:
        verbose_name_plural = "Clientes"

class Cita(models.Model):
    cta_id = models.AutoField(primary_key=True)
    cta_cli = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cta_srv = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    cta_duracion = models.IntegerField()  # Duración en minutos
    cta_fecha_hora = models.DateTimeField()
    cta_imagen = models.ImageField(upload_to='citas/', null=True, blank=True)

    def __str__(self):
        return f"Cita con {self.cta_cli} para {self.cta_srv}"

    class Meta:
        verbose_name_plural = "Citas"

class Notificacion(models.Model):
    ntf_id = models.AutoField(primary_key=True)
    ntf_cli = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    ntf_cta = models.ForeignKey(Cita, on_delete=models.CASCADE)
    ntf_mensaje = models.TextField()
    ntf_fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notificación para {self.ntf_cli}"

    class Meta:
        verbose_name_plural = "Notificaciones"
