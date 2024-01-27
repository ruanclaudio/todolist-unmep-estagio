from django.db import models

class Status(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    

class TodoList(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título')
    description = models.CharField(max_length=500, verbose_name='Descrição')
    date = models.DateField(null=True, verbose_name='Data')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, 
                                related_name='status', to_field='id', default='1') 
    
    def __str__(self):
        return self.title