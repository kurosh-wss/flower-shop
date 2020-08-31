from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children",
        related_query_name="children",
        db_index=True,
    )
    slug = models.SlugField()

    class MPTTMeta:
        order_insertion_by = ["name"]
    
    class Meta:
        unique_together = (('parent', 'slug',))
        verbose_name_plural = "categories"

    def get_slug_list(self):
        try:
            ancestors = self.get_ancestors(include_self=True)
        except:
            ancestors = []
        else:
            ancestors = [i.slug for i in ancestors]
        
        slugs = []
        for i in range(len(ancestors)):
            slugs.append('/'.join(ancestors[:i+1]))
        return slugs

    @property
    def get_products(self):
        products = list()
        print(*self.get_children())
        for category in self.get_children():
            print('hi')
            products.append(Product.objects.filter(category__name=category.name))
        return products

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, db_index=True)
    category = models.ForeignKey(
        "Category", null=True, blank=True, on_delete=models.CASCADE
    )
    description = models.TextField()
    price = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_cat_list(self):
        k = self.category
        breadcrumb = ["dummy"]
        while k is not None:
            breadcrumb.append(k.slug)
            k = k.parent
        for i in range(len(breadcrumb) - 1):
            breadcrumb[i] = "/".join(breadcrumb[-1 : i - 1 : -1])
        return breadcrumb[-1:0:-1]
