# models.py
from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse


class Navbar(models.Model):
    name = models.CharField(max_length=255, null=True)
    slug = AutoSlugField(populate_from='name', editable=True, always_update=True)
    img = models.URLField(max_length=200,null=True, blank=True)

    class Meta:
        verbose_name_plural = "Navbar"
        db_table = "Navbar"

    def __str__(self):
        return self.name
    def get_url(self):
        return reverse('category_lists', args=[self.slug])


class Category(models.Model):
    navbar = models.ForeignKey(Navbar, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255, null=True)
    slug = AutoSlugField(populate_from='name', editable=False, always_update=True)
    img = models.URLField(max_length=200,null=True, blank=True)

    class Meta:
        verbose_name_plural = "Category"
        db_table = "Category"

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('subcategory_list', args=[self.slug])


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255, null=True)
    slug = AutoSlugField(populate_from='name', editable=True, always_update=True)
    img = models.URLField(max_length=200,null=True, blank=True)
    def get_url(self):
        return reverse('product_list', args=[self.category.slug,self.slug])

    class Meta:
        verbose_name_plural = "SubCategory"
        db_table = "SubCategory"

    def __str__(self):
        return self.name


class Items(models.Model):
    navbar = models.ForeignKey(Navbar, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255, null=True)
    slug = AutoSlugField(populate_from='name', editable=True, always_update=True)
    dis_price = models.DecimalField(max_digits=10, decimal_places=3)
    org_price = models.DecimalField(max_digits=10, decimal_places=3,default=0)
    img = models.URLField(max_length=7000,null=True)
    conditions = models.CharField(max_length=10000)
    offer =   models.CharField(max_length=5000)
    discount = models.DecimalField(max_digits=10, decimal_places=3,default=0)
    description = models.TextField(max_length=10000,default=0)

    class Meta:
        verbose_name_plural = "Items"
        db_table = "Items"
   
    def get_url(self):
        return reverse('product_list', args=[self.category.slug,self.slug])


    def __str__(self):
        return self.name
