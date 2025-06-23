from django.db import models

class Toy(models.Model):
    AGE_CHOICES = [
        ('0-3', '0-3 роки'),
        ('4-7', '4-7 років'),
        ('8+', '8 років і старші'),
    ]

    name = models.CharField(max_length=100, verbose_name="Назва")
    description = models.TextField(verbose_name="Опис")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Ціна")
    age_group = models.CharField(max_length=10, choices=AGE_CHOICES, verbose_name="Вік")
    available = models.BooleanField(default=True, verbose_name="В наявності")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата додавання")

    def str(self):
        return self.name


class ToyOrder(models.Model):
    customer_name = models.CharField(max_length=100, verbose_name="Ім'я покупця")
    customer_email = models.EmailField(verbose_name="Email")
    toy = models.ForeignKey(Toy, on_delete=models.CASCADE, verbose_name="Іграшка")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Кількість")
    ordered_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата замовлення")

    def str(self):
        return f"Замовлення #{self.id} — {self.customer_name}"

