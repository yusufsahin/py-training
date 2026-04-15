from django.db import models


class Contact(models.Model):
    name = models.CharField("Ad Soyad", max_length=120)
    email = models.EmailField("E-posta")
    subject = models.CharField("Konu", max_length=200)
    message = models.TextField("Mesaj")
    created_at = models.DateTimeField("Oluşturulma", auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "İletişim kaydı"
        verbose_name_plural = "İletişim kayıtları"

    def __str__(self) -> str:
        return f"{self.name} — {self.subject}"
