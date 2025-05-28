# usuario/decoradores.py
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied

def grupos(nombre_grupo):
    def decorador(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated and request.user.groups.filter(name=nombre_grupo).exists():
                return view_func(request, *args, **kwargs)
            raise PermissionDenied  # Retorna error 403 si no pertenece al grupo
        return _wrapped_view
    return decorador

# Atajos para cada grupo
admin_required = grupos('admin')
entrenador_required = grupos('entrenador')
atleta_required = grupos('atleta')