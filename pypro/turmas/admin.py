from django.contrib import admin

from pypro.turmas.models import Turma


class Matricula_Inline(admin.TabularInline):
    model = Turma.alunos.through
    extra = 1
    readonly_fields = ('data',)
    autocomplete_fields = ('usuario',)
    ordering = ('-data',)


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    inlines = [Matricula_Inline]
    list_display = ('nome', 'slug', 'inicio', 'fim')
    prepopulated_fields = {'slug': ('nome',)}
    ordering = ('-inicio',)
