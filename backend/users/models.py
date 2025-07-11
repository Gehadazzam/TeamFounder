from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

JOBS = [
    ('frontend', 'Frontend'),
    ('backend', 'Backend'),
    ('fullstack', 'Fullstack'),
    ('mobile', 'Mobile'),
    ('devops', 'DevOps'),
    ('database', 'Database'),
    ('ai', 'AI'),
    ('ml', 'ML'),
    ('ui_ux', 'UI/UX'),
    ('game_dev', 'Game Dev'),
    ('other', 'Other'),
]


class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = PhoneNumberField(unique=True)
    job = models.CharField(max_length=255, choices=JOBS)
    # team = models.ForeignKey(
    #     "Team", on_delete=models.CASCADE, null=True, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['-date_joined']
        verbose_name = 'User'
        verbose_name_plural = 'Users'


# class Team(models.Model):
#     name = models.CharField(max_length=255)
#     leader = models.ForeignKey(User, on_delete=models.CASCADE)
#     members = models.ManyToManyField(User, related_name='teams')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name

#     class Meta:
#         ordering = ['-created_at']
#         verbose_name = 'Team'
#         verbose_name_plural = 'Teams'


class Skills(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='skills')

    python = models.IntegerField(default=0, validators=[
                                 MinValueValidator(0), MaxValueValidator(10)])
    javascript = models.IntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    react = models.IntegerField(default=0, validators=[
                                MinValueValidator(0), MaxValueValidator(10)])
    django = models.IntegerField(default=0, validators=[
                                 MinValueValidator(0), MaxValueValidator(10)])
    flask = models.IntegerField(default=0, validators=[
                                MinValueValidator(0), MaxValueValidator(10)])
    sql = models.IntegerField(default=0, validators=[
                              MinValueValidator(0), MaxValueValidator(10)])
    no_sql = models.IntegerField(default=0, validators=[
                                 MinValueValidator(0), MaxValueValidator(10)])
    java = models.IntegerField(default=0, validators=[
                               MinValueValidator(0), MaxValueValidator(10)])
    c = models.IntegerField(default=0, validators=[
                            MinValueValidator(0), MaxValueValidator(10)])
    cpp = models.IntegerField(default=0, validators=[
                              MinValueValidator(0), MaxValueValidator(10)])
    csharp = models.IntegerField(default=0, validators=[
                                 MinValueValidator(0), MaxValueValidator(10)])
    php = models.IntegerField(default=0, validators=[
                              MinValueValidator(0), MaxValueValidator(10)])
    ruby = models.IntegerField(default=0, validators=[
                               MinValueValidator(0), MaxValueValidator(10)])

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name = 'Skills'
        verbose_name_plural = 'Skills'
