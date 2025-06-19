class Toy(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва")
    description = models.TextField(verbose_name="Опис")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Ціна")
    available = models.BooleanField(default=True, verbose_name="В наявності")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата додавання")

    def __str__(self):
        return self.name

